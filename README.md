### Automation Pipeline Report

 Project thiết kế một luồng cronjob để tự động hóa xử lý email và đẩy dữ liệu từ các file xlsx đính kèm vào trong database. Nó sử dụng các thư viện và module Python để thực hiện các chức năng của nó. Dưới đây là một tổng quan về các thành phần chính của dự án và mục đích của chúng.

### Các thành phần

1. **cronjob**:
   - sử dụng package:  **apscheduler**
   - import các thư viện **BlockingScheduler**, **CronTrigger**này được sử dụng để lập lịch và chạy các nhiệm vụ theo khoảng thời gian cụ thể.

2. **automation_mail.py**:
   - sử dụng package **email.mime**
   tự động gửi email chứa thông tin đơn hàng, khách hàng hoặc lịch sử mua hàng cho các nhân viên với dữ liệu từ API.

3. **database_dump**:
   - Hàm này xử lý quá trình sao lưu dữ liệu thu được từ file excel vào cơ sở dữ liệu.

4. **gmail_attach**:
   - Lấy các tệp đính kèm được gửi trong email

### Thực thi

Thực thi chính của chương trình được xử lý bởi hàm `execute`. Nó thực hiện các nhiệm vụ sau:

Các nhiệm vụ được lập lịch sử dụng class `BlockingScheduler` từ `apscheduler`. Các công việc sau được thêm vào lịch trình:

1. **Công việc "execute"**:
   - Chạy hàm `execute` vào lúc 13:00 và 14:00 hàng ngày.
   - Kích hoạt bởi biểu thức `CronTrigger.from_crontab(expr="00 13,14 * * *")`.

2. **Công việc "main_auto_mail"**:
   - Chạy hàm `main_auto_mail` vào lúc 14:00 và 15:00 hàng ngày.
   - Kích hoạt bởi biểu thức `CronTrigger.from_crontab(expr="00 14,15 * * *")`.

3. **Công việc "history_auto_mail"**:
   - Chạy hàm `history_auto_mail` vào lúc 15:00 và 16:00 hàng ngày.
   - Kích hoạt bởi biểu thức `CronTrigger.from_crontab(expr="00 15,16 * * *")`.

Sau khi lập lịch các công việc, chương trình cố gắng thực thi các hàm `execute` và `main_auto_mail` một lần ngoài các khoảng thời gian được lập lịch. Nếu xảy ra ngoại lệ, nó sẽ được in ra.

Cuối cùng, lập lịch trình được khởi động bằng câu lệnh `scheduler.start()`, khởi động thực thi các công việc đã lập lịch dựa trên các khoảng thời gian được chỉ định.



4. python cronjob.py

