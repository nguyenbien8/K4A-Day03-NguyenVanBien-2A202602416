# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Nguyễn Văn Biển  
> **Mã Sinh Viên / Mã Học viên:** 2A202602416
> **Chủ đề Lựa chọn:** Trợ lý Tư vấn Sức khỏe Vinmec

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 5 / 5 | Agent có thể xác định chuyên khoa, tra cứu bác sĩ và lịch làm việc, sau đó đặt lịch khám. |
| **2. Tool Interaction** | 5 / 5 | Agent cần sử dụng Tool tra cứu lịch bác sĩ và Tool đặt lịch khám thông qua MCP Server. |
| **3. Dynamic Decision** | 5 / 5 | Việc đặt lịch phụ thuộc vào kết quả tra cứu bác sĩ, chuyên khoa và khung giờ phù hợp. |
| **4. Long Horizon Goal** | 4 / 5 | Agent duy trì mục tiêu từ lúc tiếp nhận nhu cầu khám đến khi hoàn tất đặt lịch, nhưng bài mô phỏng chỉ có vài bước. |
| **TỔNG ĐIỂM AGENTIC FIT** | **19 / 20** | Bài toán phù hợp cao với Agentic System vì có tra cứu, quyết định và hành động. |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dưới đây là đoạn trace tiêu biểu của `TC04`, được sinh ra từ Gemini API thật:

```json
[
  {
    "step": 1,
    "query": "Tôi muốn khám da liễu vào lúc 14:00 ngày 21/09/2026. Hãy tìm bác sĩ da liễu đang làm việc phù hợp rồi đặt lịch cho bệnh nhân Lê Thị Hoa.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "doctor_schedule_query",
    "arguments": {
      "specialty": "Da liễu"
    },
    "observation": {
      "status": "SUCCESS",
      "data": {
        "doctor_name": "Phạm Thu Hà",
        "specialty": "Da liễu",
        "hospital": "Vinmec Central Park",
        "available_slots": [
          "14:00 21/09/2026",
          "15:30 21/09/2026"
        ]
      }
    },
    "latency_ms": 1364.52
  },
  {
    "step": 2,
    "action_type": "TOOL_EXECUTION",
    "tool_name": "book_appointment",
    "arguments": {
      "patient_name": "Lê Thị Hoa",
      "specialty": "Da liễu",
      "doctor_name": "Phạm Thu Hà",
      "datetime_str": "14:00 21/09/2026"
    },
    "observation": {
      "status": "SUCCESS",
      "booking_id": "VM-20260920-001",
      "patient_name": "Lê Thị Hoa",
      "doctor_name": "Phạm Thu Hà",
      "specialty": "Da liễu",
      "datetime": "14:00 21/09/2026"
    },
    "latency_ms": 1972.69
  },
  {
    "step": 3,
    "action_type": "FINAL_ANSWER",
    "output": "Đặt lịch khám thành công cho bệnh nhân Lê Thị Hoa với bác sĩ Phạm Thu Hà vào lúc 14:00 21/09/2026.",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên Gemini API thật.
- **Tổng số Test Cases đã chạy thành công:** **5 / 5 test cases**.
- **Số lượt gọi Tool qua MCP Server chính xác:** **5 lượt**.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
