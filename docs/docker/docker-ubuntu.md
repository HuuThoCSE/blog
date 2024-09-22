# Xác định container ID hoặc tên của container
```bash
sudo docker ps -a
```

# Khởi động lại container nếu nó đã dừng
```bash
sudo docker start <container-id>
```

# Vào lại container
Sau khi container đã chạy hoặc đang chạy, sử dụng lệnh sau để kết nối lại với container:
```bash
sudo docker exec -it <container-id> bash
```
Hoặc nếu muốn vào container đã chạy nhưng bị dừng ở trước đó:
```bash
sudo docker attach <container-id>
```
Lưu ý:
- `docker exec -it` cho phép em mở một terminal mới trong container, ngay cả khi container đang chạy một lệnh khác.
- `docker attach` cho phép em nối lại phiên làm việc với container, nhưng nếu container không ở chế độ tương tác, em có thể không thấy đầu ra.

# Để thoát mà không dừng container
Sử dụng tổ hợp phím `Ctrl + P` và `Ctrl + Q`

# Các trạng thái container
Exited: trạng thái dừng

# kết thúc làm việc
```bath
exit
```

## Makefine
```
DOCKER_NETWORK = docker-hadoop_default
ENV_FILE = hadoop.env
current_branch := 2.0.0-hadoop3.2.1-java8

build:
        docker build -t bde2020/hadoop-base:$(current_branch) ./base
        docker build -t bde2020/hadoop-namenode:$(current_branch) ./namenode
        docker build -t bde2020/hadoop-datanode:$(current_branch) ./datanode
        docker build -t bde2020/hadoop-resourcemanager:$(current_branch) ./resourcemanager
        docker build -t bde2020/hadoop-nodemanager:$(current_branch) ./nodemanager
        docker build -t bde2020/hadoop-historyserver:$(current_branch) ./historyserver
        docker build -t bde2020/hadoop-submit:$(current_branch) ./submit

wordcount:
        docker build -t hadoop-wordcount ./submit
        docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} bde2020/hadoop-base:$(current_branch) hdfs dfs -mkdir -p /input/
        docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} bde2020/hadoop-base:$(current_branch) hdfs dfs -copyFromLocal -f /opt/hadoop-3.2.1/README.txt /input/
        docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} hadoop-wordcount
        docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} bde2020/hadoop-base:$(current_branch) hdfs dfs -cat /output/*
        docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} bde2020/hadoop-base:$(current_branch) hdfs dfs -rm -r /output
        docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} bde2020/hadoop-base:$(current_branch) hdfs dfs -rm -r /input
```