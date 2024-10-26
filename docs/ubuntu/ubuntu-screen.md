# Tạo một phiên với tên cụ thể
```bash
screen -S <tên phiên>
```

# Tách phiên screen (detach)
```
Ctrl + A rồi D
```

# Liệt kê các phiên screen đang chạy
```
screen -ls
```

# Quay lại một phiên screen đã tách
```
screen -r <ID_hoặc_tên_phiên>
```

# Đóng phiên
## Tắt tất cả các phiên screen:
```
screen -wipe
```

## Xóa một phiên screen cụ thể:
```
screen -S <ID_hoặc_tên_phiên> -X quit
```