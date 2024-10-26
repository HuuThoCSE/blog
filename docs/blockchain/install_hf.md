# Cài đặt Hyperledger Fabric

# Lưu ý
- Chạy docker thì không dùng `sudo`

## Tạo group `docker`
```bash
sudo groupadd docker
```

## Thêm người dùng hiện tại $USER vào group `docker`
```bash
sudo usermod -aG docker $USER
```

## Kiểm tra xem người dùng đã được thêm vào nhóm `docker`
```bash
cat /etc/group | grep docker 
```

## Cập nhật danh sách gói cài đặt và nâng cấp các gói phần mềm hiện tại
```bash
sudo apt-get update && sudo apt-get -y upgrade 
```
Sẽ tìm nạp danh sách các gói cho tất cả các kho lưu trữ và PPA của bạn và đảm bảo rằng hệ thống đã cập nhật.)

## Cài đặt các yêu cầu trước cho Hyperledger Composer
```bash
curl -sSLO https://raw.githubusercontent.com/hyperledger/fabric/main/scripts/install-fabric.sh && chmod +x install-fabric.sh
```