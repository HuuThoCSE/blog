```
sudo apt update
```

```
sudo apt --fix-broken install
```

```
mkdir node_test
cd node_test
```

## Khởi tạo tệp `package.json`:
```
npm init -y
```

## Cài đặt express để tạo ứng dụng web đơn giản:
```
npm install express
```

## Tạo tệp `app.js`:
Tạo một file app.js với nội dung sau để khởi chạy một server Node.js đơn giản:
```
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello World from Docker!');
});

app.listen(port, () => {
  console.log(`App running at http://localhost:${port}`);
});
```

## Tạo tệp Dockerfile
Trong thư mục dự án của em, tạo một tệp có tên Dockerfile. Đây là file Docker cấu hình để xây dựng image.
```
# Sử dụng Node.js image chính thức
FROM node:14

# Thiết lập thư mục làm việc
WORKDIR /usr/src/app

# Sao chép file package.json và package-lock.json
COPY package*.json ./

# Cài đặt các phụ thuộc (bao gồm express)
RUN npm install

# Sao chép toàn bộ mã nguồn
COPY . .

# Expose cổng 8080
EXPOSE 8080

# Chạy ứng dụng
CMD ["node", "app.js"]
```

## Tạo tệp `.dockerignore`
Tạo tệp `.dockerignore` để bỏ qua những file không cần thiết khi build Docker image:
```bash
node_modules
npm-debug.log
```

## Xây dựng Docker image
Trong thư mục dự án, chạy lệnh sau để xây dựng Docker image từ Dockerfile:
```bash
docker build -t my-node-app .
```

## Chạy Docker container
Sau khi đã tạo Docker image, em có thể chạy container từ image vừa tạo:
```
docker run -p 8080:8080 my-node-app
```

Lệnh này sẽ tạo một Docker image với tên my-node-app.