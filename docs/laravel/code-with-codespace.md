```
php composer.phar install
```

## Tìm vị trí file php.ini
```cmd
php --ini
```


## Bước 0: Cập nhật lại OS
```cmd
sudo apt-get update
```

## Sử dụng kho lưu trữ PPA
```cmd
sudo add-apt-repository ppa:ondrej/php
```

## Cài đặt lại extension
```
sudo apt-get install php8.2-mysql
```

## Bước 1: Tìm vị trí file
```cmd
sudo find / -name pdo_mysql.so
```

## Kiểm tra lại ví trí của các extension
```cmd
php -i | grep extension_dir
```

## Bước 2: Copy file pdo_mysql.so đến nơi php hoạt động
```
sudo cp /usr/lib/php/20220829/pdo_mysql.so /opt/php/8.2.14/lib/php/extensions/no-debug-non-zts-20220829/
```

## Code run project
```cmd
php artisan serve --host=0.0.0.0 --port=8000
```

## Clear cache and route
```cmd
php artisan config:clear & php artisan route:clear
```