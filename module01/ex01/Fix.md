## วิธีป้องกัน XXE

1. ปิดการใช้งาน DTD และ External Entity ใน XML parser
2. ใช้ secure parser configuration (disallow-doctype)
3. Validate schema ของ XML
4. ใช้ allowlist สำหรับ tag ที่อนุญาต
5. อัปเดต library ที่ใช้ parse XML ให้เป็นเวอร์ชันล่าสุด

## แนวคิดตัวอย่าง

ตั้งค่า parser ให้ไม่รองรับ DOCTYPE และ SYSTEM entity
เพื่อไม่ให้โหลด resource ภายนอก

## วิธีทดสอบหลังแก้ไข

1. ส่ง payload เดิมทั้งหมดอีกครั้ง
2. ตรวจสอบว่า:
   - DOCTYPE ถูกปฏิเสธ
   - entity ไม่ถูกแทนที่
   - ไม่สามารถอ่านไฟล์ได้
3. หน้าเว็บต้องแสดง error หรือแสดง XML เป็นข้อความธรรมดา

## สรุป

หลังจากปิด external entity และ DTD แล้ว
ไม่สามารถ inject XML entity ได้อีก
จึงลดความเสี่ยงจาก XXE
