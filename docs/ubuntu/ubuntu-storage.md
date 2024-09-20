# Kiểm tra thông tin về dung lượng ổ cứng:
## Hiển thị dung lượng sử dụng của các phân vùng theo cách dễ đọc (tính bằng GB/MB)
```cmd
df -h
```

## Hiển thị danh sách các ổ đĩa và phân vùng của hệ thống.
```cmd
lsblk
```

# Kiểm tra thông tin chi tiết về ổ cứng:
## Hiển thị thông tin chi tiết về phân vùng và ổ cứng.
```cmd
fdisk -l
```

# Kiểm tra nhiệt độ và tình trạng của ổ cứng:
## Cài đặt gói `smartmontools`:
```cmd
sudo apt install smartmontools
```

## Kiểm tra tình trạng ổ cứng:
```cmd
sudo smartctl -a /dev/sda
```

# Mở rộng logical volume (LVM)
## 1. Kiểm tra xem còn bao nhiêu dung lượng trống trong Volume Group (ubuntu-vg) 
```cmd
vgdisplay
```
Tìm dòng `Free PE / Size` để xem có bao nhiêu dung lượng trống còn lại.

## 2. Mở rộng Logical Volume
Sử dụng lệnh `lvextend` để mở rộng Logical Volume (ubuntu-lv) với toàn bộ dung lượng trống trong Volume Group.
```cmd
sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
```
ệnh này sẽ mở rộng logical volume ubuntu-lv với toàn bộ không gian trống còn lại.

## 3. Mở rộng filesystem
Sau khi mở rộng logical volume, em cần mở rộng filesystem để nó nhận ra không gian mới. Nếu em đang sử dụng `ext4`, hãy dùng lệnh sau:
```cmd
sudo resize2fs /dev/ubuntu-vg/ubuntu-lv
```
Nếu em đang sử dụng xfs (kiểm tra bằng lệnh df -T), hãy sử dụng lệnh này thay thế:
```cmd
sudo xfs_growfs /
```

## 4. Kiểm tra lại dung lượng
Sau khi hoàn thành các bước trên, em có thể kiểm tra dung lượng mới của hệ thống bằng lệnh `df -h`:
```
df -h
```
Dung lượng mới của phân vùng root / sẽ được cập nhật với toàn bộ dung lượng ổ đĩa.