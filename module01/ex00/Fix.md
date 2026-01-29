# Fix

## วิธีป้องกัน Template Injection

1. ห้าม render user input ตรงๆ ใน template
2. ใช้ escaping หรือ auto-escaping ของ template engine
3. แยก logic ออกจาก template
4. ใช้ allowlist สำหรับตัวแปรที่อนุญาตให้แสดง
5. หลีกเลี่ยงการใช้ eval-like feature ของ engine
6. อัปเดต template engine ให้เป็นเวอร์ชันล่าสุด

---

## ตัวอย่างแนวทาง

แทนที่จะ render input ตรงๆ:

render(user_input)

ให้เปลี่ยนเป็น:

render(escape(user_input))

หรือส่งเป็น plain text เท่านั้น

---

## วิธีทดสอบหลังแก้

1. ใส่ payload เดิมทั้งหมด
2. ตรวจสอบว่า:
   - expression ไม่ถูกประเมิน
   - แสดงเป็นข้อความธรรมดา
   - ไม่สามารถเข้าถึง object ภายในได้
3. refresh หน้าเว็บซ้ำ

หาก expression ไม่ถูกคำนวณ แสดงว่าแก้ไขสำเร็จ

---

## สรุป

หลังจาก sanitize input และจำกัด context ของ template
ไม่สามารถ inject expression ได้อีก
จึงลดความเสี่ยงจาก SSTI
