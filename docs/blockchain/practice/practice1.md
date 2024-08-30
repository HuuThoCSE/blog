# Smart Contract (Hợp đồng thông minh)
## Các bước thực hiện
- Bước 1: Viết Hợp Đồng Thông Minh Trong Remix
- Bước 2: Biên Dịch Hợp Đồng
- Bước 3: Triển Khai Hợp Đồng Trên Mạng Thử Nghiệm
- Bước 4: Tương Tác Với Hợp Đồng Thông Minh
- Bước 5: Kiểm Tra Kết Quả

## Bước 1: Viết Hợp Đồng Thông Minh Trong Remix
1. Mở Remix IDE
- Truy cập Remix IDE trên trình duyệt của bạn.
2. Tạo Một Tệp Hợp Đồng Mới
- Trong Remix IDE, chọn **File Explorer** (biểu tượng thư mục ở góc trên bên trái).
- Nhấp vào biểu tượng "New File" và đặt tên tệp của bạn, ví dụ: **StudentStorage.sol**.
3. Viết Hợp Đồng Thông Minh

- Mã hợp đồng mẫu:
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentStorage {
    // Khai báo một cấu trúc sinh viên để lưu trữ thông tin sinh viên
    struct Student {
        string student_code;
        string student_fullname;
        string university_name;
        string major;  // Thuộc tính mới: ngành học
    }

    // Biến để lưu trữ sinh viên
    Student private student;

    // Hàm để lưu trữ thông tin sinh viên
    function setStudent(
        string memory _student_code, 
        string memory _student_fullname, 
        string memory _university_name,
        string memory _major  // Thêm tham số cho ngành học
    ) public {
        student.student_code = _student_code;
        student.student_fullname = _student_fullname;
        student.university_name = _university_name;
        student.major = _major;  // Lưu ngành học
    }

    // Hàm để lấy thông tin sinh viên
    function getStudent() public view returns (
        string memory, 
        string memory, 
        string memory,
        string memory  // Thêm ngành học vào kết quả trả về
    ) {
        return (
            student.student_code, 
            student.student_fullname, 
            student.university_name,
            student.major  // Trả về ngành học
        );
    }
}

```

## Bước 2: Biên Dịch Hợp Đồng
- Chuyển đến tab Solidity Compiler (biểu tượng với dấu kiểm) ở bên trái.
- Chọn phiên bản compiler phù hợp với phiên bản Solidity mà bạn đã sử dụng (0.8.0).
- Nhấp vào nút **Compile StudentStorage.sol**. Nếu không có lỗi, bạn sẽ thấy thông báo biên dịch thành công.

## Bước 3: Triển Khai Hợp Đồng Trên Mạng Thử Nghiệm
1. Chọn Môi Trường Triển Khai:
- Trong tab Deploy & Run Transactions, chọn Injected Web3 nếu bạn đang sử dụng MetaMask hoặc chọn Remix VM để triển khai trên môi trường máy ảo cục bộ.
2. Triển Khai Hợp Đồng:
- Bạn sẽ thấy hợp đồng StudentStorage xuất hiện dưới mục CONTRACT.
- Nhấp vào nút Deploy để triển khai hợp đồng.
- MetaMask sẽ mở một cửa sổ yêu cầu xác nhận giao dịch. Kiểm tra chi tiết giao dịch và nhấp Confirm.
3. Chờ Xác Nhận Giao Dịch:
- Sau khi giao dịch được xác nhận, bạn sẽ thấy hợp đồng của mình được triển khai trong phần Deployed Contracts ở dưới cùng của tab.

## Bước 4: Tương Tác Với Hợp Đồng Thông Minh
1. Sử Dụng Hàm setStudent để Lưu Trữ Thông Tin Sinh Viên:
- Trong phần **Deployed/Unpinned Contracts**, bạn sẽ thấy các hàm setStudent và getStudent.
- Nhập thông tin sinh viên vào các trường tương ứng trong hàm **setStudent**:
    student_code: "21022008"
    student_fullname: "Nguyen Huu Tho"
    university_name: "Vinh Long University of Technology Education"
    major: "Computer Science"
- Nhấp vào nút **transact** để lưu trữ thông tin. MetaMask sẽ yêu cầu xác nhận giao dịch. Nhấp Confirm.

2. Sử Dụng Hàm **getStudent** để Truy Xuất Thông Tin Sinh Viên:
- Nhấp vào nút getStudent để truy xuất thông tin sinh viên đã lưu trữ.
- Bạn sẽ thấy các thông tin chi tiết của sinh viên (mã sinh viên, tên đầy đủ, và tên trường đại học) hiển thị trong Remix.

## Bước 5: Kiểm Tra Kết Quả
- Đảm bảo rằng thông tin được lưu trữ chính xác và hàm **getStudent** trả về thông tin đúng như bạn đã nhập.
- Bạn có thể thử nhập các giá trị khác nhau vào hàm **setStudent** để kiểm tra tính linh hoạt của hợp đồng.
