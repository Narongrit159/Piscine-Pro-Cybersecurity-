# Exercise 01 - Cross-Site Request Forgery (CSRF)

## ประเภทของช่องโหว่

Cross-Site Request Forgery (CSRF)

## คำอธิบาย

CSRF คือช่องโหว่ที่ทำให้ attacker สามารถบังคับให้ browser ของเหยื่อ
ส่ง request ไปยังเว็บเป้าหมายโดยที่เหยื่อไม่รู้ตัว

เพราะว่า browser จะส่ง cookie/session ไปพร้อม request โดยอัตโนมัติ
ทำให้ server คิดว่าเป็นคำสั่งที่มาจากผู้ใช้จริง

ในแลปนี้ ระบบไม่มีการตรวจสอบ CSRF token และไม่ validate origin
ทำให้สามารถสร้าง request ภายนอกเพื่อสั่งโอนเงินได้

## หลักการทำงาน

1. ผู้ใช้ login อยู่แล้ว
2. attacker สร้างหน้า HTML ที่ส่ง request ไปยังเว็บเป้าหมาย
3. เมื่อเหยื่อเปิดหน้านั้น browser จะส่ง request พร้อม session
4. server ดำเนินการโอนเงินทันที

## ผลกระทบ

- โอนเงินโดยไม่ได้รับอนุญาต
- เปลี่ยนข้อมูลบัญชีผู้ใช้
- ดำเนิน action สำคัญแทนเหยื่อได้
