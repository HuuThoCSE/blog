# Kiểm tra tường lửa
```bash
sudo ufw status
```

# Kiểm tra tường lửa
```bash
sudo ufw allow 1883/tcp
```

# Kiểm tra cổng
```bash
sudo ss -tuln | grep 1883
```
Trong đó:
- `-t`: Hiển thị các cổng TCP.
- `-u`: Hiển thị các cổng UDP.
- `-l`: Hiển thị các cổng đang lắng nghe (listening).
- `-n`: Hiển thị địa chỉ IP và cổng dưới dạng số (không chuyển đổi sang tên).


# Tắt luôn tường lửa
```
sudo ufw disable
```