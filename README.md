##Automation Pipeline Report

 Project thiết kế để tự động hóa xử lý email và đẩy dữ liệu từ các file xlsx đính kèm vào trong database. Nó sử dụng các thư viện và module Python để thực hiện các chức năng của nó. Dưới đây là một tổng quan về các thành phần chính của dự án và mục đích của chúng.

### Các thành phần

1. **apscheduler**:
   - Import class `BlockingScheduler` từ module `apscheduler.schedulers.blocking`.
   - Import class `CronTrigger` từ module `apscheduler.triggers.cron`.
   - Các thư viện này được sử dụng để lập lịch và chạy các nhiệm vụ theo khoảng thời gian cụ thể.

2. **automation_mail**:
   - Import các hàm `main_auto_mail` và `history_auto_mail` từ module `automation_mail`.
   - Những hàm này đảm nhận việc gửi và xử lý email tự động.

3. **database_dump**:
   - Import hàm `main_componentdb_dump` từ module `database_dump`.
   - Hàm này xử lý quá trình sao lưu dữ liệu vào cơ sở dữ liệu.

4. **gmail_attach**:
   - Import hàm `main_gmail_attachments` từ module `gmail_attach`.
   - Hàm này xử lý việc đính kèm tệp tin vào Gmail.

### Thực thi

Thực thi chính của chương trình được xử lý bởi hàm `execute`. Nó thực hiện các nhiệm vụ sau:

1. In thời gian hiện tại sử dụng module `datetime`.
2. Gọi hàm `main_gmail_attachments` hai lần để xử lý đính kèm email. Nếu xảy ra ngoại lệ, in ra thông báo cho biết email không được tìm thấy.

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
# Automation-Pipeline-Report
