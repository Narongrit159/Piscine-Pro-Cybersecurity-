## วิธีป้องกัน SSRF

1. ใช้ allowlist domain ที่อนุญาตให้ fetch เท่านั้น
2. block protocol อันตราย เช่น file://
3. ตรวจสอบ IP ปลายทาง (ห้ามเข้าถึง localhost และ private network)
4. ตั้ง timeout และจำกัด response size

---

## วิธีป้องกัน LFI

1. ห้ามรับ path จากผู้ใช้โดยตรง
2. ใช้ path ที่กำหนดไว้ล่วงหน้าเท่านั้น
3. ใช้ realpath เพื่อตรวจสอบ directory traversal
4. จำกัดสิทธิ์ของ process ให้อ่านไฟล์ได้น้อยที่สุด

---

## วิธีทดสอบหลังแก้ไข

1. ใส่ payload เดิมทั้งหมดอีกครั้ง
2. ตรวจสอบว่า:
   - file:///etc/passwd ไม่ถูก fetch
   - server ปฏิเสธ URL ภายใน
3. ทดลอง URL ปกติ ต้องยังใช้งานได้

---

## สรุป

หลังจาก validate URL และจำกัด protocol แล้ว
ไม่สามารถอ่านไฟล์ระบบหรือเข้าถึง resource ภายในได้อีก
จึงลดความเสี่ยงจาก SSRF และ LFI
