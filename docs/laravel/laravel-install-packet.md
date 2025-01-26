## Cài đặt Thư viện Tạo PDF
```
composer require barryvdh/laravel-dompdf
```


##  Xuất bản Cấu hình (Tùy chọn)
```
php artisan vendor:publish --provider="Barryvdh\DomPDF\ServiceProvider"
```

```
composer dump-autoload

php artisan config:clear
php artisan cache:clear
php artisan view:clear
```

