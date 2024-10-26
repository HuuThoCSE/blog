# Driver
- CP210x
- [Tải driver](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads)
- Chọn `CP210x Windows Drivers`

# Thêm ESP32 Board vào Arduino IDE
Mặc định Arduino IDE không hỗ trợ ESP32, nên bạn cần thêm board ESP32 vào IDE:
1. Mở Arduino IDE.
2. Vào File > Preferences.
3. Tại mục Additional Boards Manager URLs, thêm đường dẫn sau:
```
https://dl.espressif.com/dl/package_esp32_index.json
```
4. Nhấn OK để lưu lại.

# Cài đặt ESP32 Board
1. Vào Tools > Board > Boards Manager.
2. Tìm kiếm esp32 trong Boards Manager.
3. Chọn esp32 by Espressif Systems và nhấn Install.

# Nạp code thì đè nút BOOT trước khi nạp code