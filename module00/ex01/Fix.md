## วิธีป้องกัน

1. ใช้ CSRF Token ทุก request ที่มีการเปลี่ยน state
2. ตรวจสอบ Origin / Referer header
3. ไม่ใช้ GET กับ action สำคัญ
4. เพิ่ม confirmation step สำหรับธุรกรรม
