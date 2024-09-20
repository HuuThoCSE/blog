# Cập nhật danh sách gói
```
sudo apt update
```
# Cài đặt các phụ thuộc cần thiết
```
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

# Thêm Docker's official GPG key
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

# Thêm Docker's repository
Sử dụng lệnh sau để thêm repository chính thức của Docker:
```
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

# Cập nhật danh sách gói lần nữa
```
sudo apt update
```

# Cài đặt Docker
```
sudo apt install docker-ce docker-ce-cli containerd.io
```

# Kiểm tra phiên bản Docker
```
docker --version
```

# Chạy Docker mà không cần quyền `sudo` (Tùy chọn)
Mặc định, cần dùng lệnh `sudo` để chạy Docker. Nếu em muốn chạy Docker mà không cần sử dụng sudo, thêm user của em vào nhóm docker:
```
sudo usermod -aG docker $USER
```
Sau đó, đăng xuất và đăng nhập lại để thay đổi có hiệu lực.

# Playing with Ubuntu
## Chạy một container Ubuntu
```
sudo docker run -it ubuntu bash
```

## Liệt kê các container đang chạy
```
sudo docker ps
```

## Để xem tất cả các container, bao gồm cả những container đã dừng, sử dụng:
```
sudo docker ps -a
```

## Xóa container đã dừng
```
sudo docker rm <container-id>
```


