# Cài đặt docker
```bash
sudo apt update
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
```

# Tải Mosquitto Docker Image
```bash
sudo docker pull eclipse-mosquitto
```

# Chạy Mosquitto MQTT Broker bằng Docker
```
sudo docker run -it -p 1883:1883 -p 9001:9001 eclipse-mosquitto
```

# Tùy chỉnh cấu hình Mosquitto
## Tạo thư mục chứa tệp cấu hình:
```bash
mkdir mosquitto_config
```

## Tạo tệp cấu hình `mosquitto.conf` bên trong thư mục này:
```bash
touch mosquitto_config/mosquitto.conf
```

## Ví dụ nội dung của tệp mosquitto.conf:
```bash
listener 1883
allow_anonymous true
persistence true
persistence_location /mosquitto/data/
log_dest file /mosquitto/log/mosquitto.log
```
Tệp cấu hình trên cho phép Mosquitto lắng nghe trên cổng 1883 và cho phép các kết nối ẩn danh.
- `listener` 1883: Lắng nghe trên cổng 1883 cho mọi giao diện (IPv4 và IPv6).
- `allow_anonymous` true: Cho phép các client kết nối mà không cần xác thực.
- `persistence`: Đảm bảo rằng dữ liệu sẽ được lưu khi Mosquitto hoạt động.
- `persistence_location`: Đường dẫn đến thư mục nơi Mosquitto sẽ lưu dữ liệu.
- `log_dest`: Đường dẫn để ghi log của Mosquitto.

## Chạy Mosquitto với tệp cấu hình tùy chỉnh:
```
sudo docker run -it -p 1883:1883 -p 9001:9001 -v $(pwd)/mosquitto_config:/mosquitto/config eclipse-mosquitto
```
Lệnh trên sẽ ánh xạ thư mục `mosquitto_config` từ máy chủ của bạn vào thư mục `/mosquitto/config` trong container.

## Chạy lại file cấu hình mới
```
sudo docker restart <container_id>
```

## Kiểm tra Mosquitto MQTT Broker
- Sau khi Mosquitto đã chạy trong Docker, bạn có thể kiểm tra kết nối bằng cách sử dụng công cụ Mosquitto Client hoặc bất kỳ client MQTT nào khác.
- Nếu đã cài đặt Mosquitto Client, bạn có thể kiểm tra với các lệnh sau:
    - Publish một tin nhắn lên topic `test`:
    ```bash
    mosquitto_pub -h localhost -t test -m "Hello from MQTT"
    ```

    - Subscribe để nhận tin nhắn từ topic `test`:
    ```bash
    mosquitto_sub -h localhost -t test
    ```
# Lưu trữ dữ liệu MQTT (Persistent Storage)
Nếu bạn muốn lưu trữ các dữ liệu log hoặc dữ liệu bền vững của Mosquitto, bạn có thể ánh xạ một thư mục trên máy chủ vào container bằng cách sử dụng tùy chọn -v để ánh xạ volume.
```bash
sudo docker run -it -p 1883:1883 -p 9001:9001 \
  -v $(pwd)/mosquitto_data:/mosquitto/data \
  -v $(pwd)/mosquitto_log:/mosquitto/log \
  -v $(pwd)/mosquitto_config:/mosquitto/config \
  eclipse-mosquitto
```
- `mosquitto_data`: Lưu trữ dữ liệu.
- `mosquitto_log`: Lưu trữ file log của Mosquitto.
- `mosquitto_config`: Thư mục cấu hình.

# Chạy Mosquitto trong chế độ nền (detached mode)
Nếu bạn không muốn Mosquitto chạy trong chế độ tương tác mà muốn nó chạy trong chế độ nền, bạn có thể thêm tùy chọn `-d`:
```bash
docker run -d -p 1883:1883 -p 9001:9001 eclipse-mosquitto
```

# cài đặt Mosquitto
```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients
```

# khởi động Mosquitto
```bash
sudo systemctl start mosquitto
```

# Cấu hình ESP32 để giao tiếp với MQTT
```c++
#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

// Cấu hình Wi-Fi
const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";

// Địa chỉ của MQTT broker (đổi thành địa chỉ của broker của bạn)
const char* mqtt_server = "broker.hivemq.com";

// Cấu hình cảm biến DHT
#define DHTPIN 4
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

// MQTT client
WiFiClient espClient;
PubSubClient client(espClient);

// Hàm kết nối Wi-Fi
void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Đang kết nối với ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("Kết nối Wi-Fi thành công");
}

// Hàm callback khi nhận dữ liệu từ broker
void callback(char* topic, byte* message, unsigned int length) {
  Serial.print("Nhận dữ liệu từ topic: ");
  Serial.println(topic);
  String messageTemp;

  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
    messageTemp += (char)message[i];
  }
  Serial.println();

  // Xử lý dữ liệu từ topic
  if (String(topic) == "esp32/output") {
    Serial.print("Nội dung tin nhắn: ");
    Serial.println(messageTemp);
  }
}

// Hàm kết nối với MQTT broker
void reconnect() {
  while (!client.connected()) {
    Serial.print("Đang kết nối với MQTT...");
    if (client.connect("ESP32Client")) {
      Serial.println("Kết nối thành công!");
      client.subscribe("esp32/output");
    } else {
      Serial.print("Lỗi kết nối. Mã lỗi: ");
      Serial.print(client.state());
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

  dht.begin();
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Đọc dữ liệu cảm biến và gửi lên MQTT topic
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  if (!isnan(temperature) && !isnan(humidity)) {
    String payload = "Temperature: " + String(temperature) + "°C, Humidity: " + String(humidity) + "%";
    Serial.print("Đang gửi dữ liệu: ");
    Serial.println(payload);

    client.publish("esp32/temperature", String(temperature).c_str());
    client.publish("esp32/humidity", String(humidity).c_str());
  }

  delay(2000); // Gửi dữ liệu mỗi 2 giây
}
```

# Tạo subscribe trên docker với topic `test`
```bash
sudo docker run -it --rm eclipse-mosquitto mosquitto_sub -h 192.168.0.110 -t "test"
```
Nếu có tài khoản
```bash
sudo docker run -it --rm eclipse-mosquitto mosquitto_sub -h 192.168.0.110 -t "test" -u "huuthocse" -P "123456"
```

# Kết nối lại với phiên làm việc của container hiện tại
```bash
sudo docker attach <container_id>
```

# Cài đặt người dùng
## Cài đặt Mosquitto
```bash
sudo apt update &&
sudo apt install mosquitto mosquitto-clients
```

## Kiểm tra cài đặt Mosquitto và `mosquitto_passwd`
```bash
mosquitto_passwd
```

## Tạo file mật khẩu với `mosquitto_passwd`
```bash
sudo mosquitto_passwd -c /path/to/passwordfile <username>
```
Ví dụ:
```bash
sudo mosquitto_passwd -c mosquitto_config/passwd huuthocse
```

## Sử dụng file mật khẩu trong Mosquitto
Sau khi tạo file mật khẩu, bạn cần cấu hình Mosquitto để sử dụng file này. Mở file cấu hình `mosquitto.conf` và thêm dòng:
```bash
allow_anonymous false
password_file /mosquitto/config/passwd
```

## Khởi động lại Mosquitto
```bash
sudo systemctl restart mosquitto
```

## Kiểm tra sử dụng cổng
### Kiểm tra cổng 1883 dịch vụ nào sử dụng
```bash
sudo lsof -i :1883
```

### Dừng dịch vụ mosquitto
```bash
sudo systemctl stop mosquitto
```

