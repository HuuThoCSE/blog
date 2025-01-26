
# ThoCSE-Laravel

## Link
[Create new Project](create-new-project.md)
[Code with Codespace](code-with-codespace.md)


## Tải laravel
https://github.com/laravel/laravel
- Chọn release

# Tải file composer.phar
https://getcomposer.org/download/
- Paste vào thư mục folder

## Tải PHPStorm

## Tải phpComposer 
https://getcomposer.org/download/

## Tải MAMP

## Coi phiên bản PHP phù hợp
- Vào folder laravel
- Mở Composer.json, check phần require > php

## Tải laragon

# Lỗi
## Lỗi ssl
Bước 1
```
composer config -g -- disable-tls true
```

Bước 2
```
; https://php.net/extension-dir
;extension_dir = "./"
; On windows:
;extension_dir = "ext"
```
to
```
; https://php.net/extension-dir
;extension_dir = "./"
; On windows:
extension_dir = "ext"
```

## Lỗi: could not find driver
Vào php.init
```cmd
;extention=pdo_mysql
```
thành 
```cmd
extention=pdo_mysql
```

## Vào folder laravel
```cmd
$php -v
$php composer.phar install
```

## 
```cmd
Code Create Project Laravel: composer create-project laravel/laravel "tên thư  mục"
Code ignore platform: composer install --ignore-platform-reqs
Code up date ignore platform: composer update --ignore-platform-reqs
php artisan serve
```

## Vào file thư mục chứa php.init
Chỉnh
```cmd
;extension=fileinfo
```

thành
```cmd
extension=php_fileinfo.dll

```


# Copy file .env.example thành .env

## Tạo token 
```cmd
php artisan key:generate
```

## Tạo controller
```cmd
php artisan make:controller HomeController
```

## Tạo model
```cmd
php artisan make:model SinhVienModel
```

## Kết nối database
- Nhập thông tin ở file `.env`
Sau đó chạy code:
```cmd
php artisan migrate
```

# Database
## Tạo migrate
```
php artisan make:migration create_farms_table
```

## Tạo seeder
```
php artisan make:seeder GoatTableSeeder
```

## Tạo cả table và seeder
```
php artisan migrate:fresh --seed
```

# Network
Khởi động toàn cục trong cùng một mạng nội bộ
```
php artisan serve --host=0.0.0.0
```