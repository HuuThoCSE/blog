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