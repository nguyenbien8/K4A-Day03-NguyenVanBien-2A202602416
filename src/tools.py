"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    {
        "name": "doctor_schedule_query",
        "description": "Tra cứu thông tin bác sĩ, chuyên khoa và lịch làm việc tại Vinmec.",
        "parameters": {
            "type": "object",
            "properties": {
                "doctor_name": {
                    "type": "string",
                    "description": "Tên bác sĩ cần tra cứu"
                },
                "specialty": {
                    "type": "string",
                    "description": "Tên chuyên khoa cần tra cứu, ví dụ Tim mạch hoặc Da liễu"
                }
            },
            "required": []
        }
    },
    {
        "name": "book_appointment",
        "description": "Đặt lịch khám bệnh tại Vinmec với bác sĩ và thời gian cụ thể.",
        "parameters": {
            "type": "object",
            "properties": {
                "patient_name": {
                    "type": "string",
                    "description": "Họ tên bệnh nhân"
                },
                "doctor_name": {
                    "type": "string",
                    "description": "Tên bác sĩ muốn đặt lịch"
                },
                "specialty": {
                    "type": "string",
                    "description": "Chuyên khoa cần khám"
                },
                "datetime_str": {
                    "type": "string",
                    "description": "Thời gian khám, ví dụ: 09:00 20/09/2026"
                }
            },
            "required": ["patient_name", "doctor_name", "specialty", "datetime_str"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DOCTORS = {
    "BS001": {
        "doctor_name": "Nguyễn Minh Anh",
        "specialty": "Tim mạch",
        "hospital": "Vinmec Times City",
        "available_slots": ["09:00 20/09/2026", "10:30 20/09/2026"]
    },
    "BS002": {
        "doctor_name": "Phạm Thu Hà",
        "specialty": "Da liễu",
        "hospital": "Vinmec Central Park",
        "available_slots": ["14:00 21/09/2026", "15:30 21/09/2026"]
    }
}


def execute_doctor_schedule_query(doctor_name: str = "", specialty: str = "") -> str:
    """Tra cứu bác sĩ theo tên hoặc chuyên khoa."""
    doctor_name = doctor_name.strip().casefold()
    specialty = specialty.strip().casefold()
    matches = [
        doctor for doctor in MOCK_DOCTORS.values()
        if ((not doctor_name or doctor_name in doctor["doctor_name"].casefold())
            and (not specialty or specialty in doctor["specialty"].casefold()))
    ]

    if matches:
        return json.dumps({
            "status": "SUCCESS",
            "data": matches[0]
        }, ensure_ascii=False)

    return json.dumps({
        "status": "NOT_FOUND",
        "message": "Không tìm thấy bác sĩ hoặc lịch làm việc phù hợp."
    }, ensure_ascii=False)


def execute_book_appointment(
    patient_name: str,
    doctor_name: str,
    specialty: str,
    datetime_str: str
) -> str:
    """Đặt lịch sau khi xác thực bác sĩ, chuyên khoa và khung giờ."""
    requested_doctor = doctor_name.strip().casefold()
    requested_specialty = specialty.strip().casefold()
    doctor = next(
        (
            item for item in MOCK_DOCTORS.values()
            if item["doctor_name"].casefold() == requested_doctor
        ),
        None
    )

    if doctor is None:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy bác sĩ '{doctor_name}'."
        }, ensure_ascii=False)

    if doctor["specialty"].casefold() != requested_specialty:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Bác sĩ {doctor_name} không thuộc chuyên khoa {specialty}."
        }, ensure_ascii=False)

    if datetime_str not in doctor["available_slots"]:
        return json.dumps({
            "status": "SLOT_UNAVAILABLE",
            "message": f"Khung giờ {datetime_str} hiện không có trong lịch của bác sĩ {doctor_name}."
        }, ensure_ascii=False)

    return json.dumps({
        "status": "SUCCESS",
        "booking_id": "VM-20260920-001",
        "patient_name": patient_name,
        "doctor_name": doctor_name,
        "specialty": specialty,
        "datetime": datetime_str,
        "message": f"Đặt lịch khám thành công cho bệnh nhân {patient_name} với bác sĩ {doctor_name} vào lúc {datetime_str}."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "doctor_schedule_query": execute_doctor_schedule_query,
    "book_appointment": execute_book_appointment
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
