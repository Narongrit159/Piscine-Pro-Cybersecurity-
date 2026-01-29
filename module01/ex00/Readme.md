# Exercise 00 - Server-Side Template Injection (SSTI)

## ประเภทของช่องโหว่

Server-Side Template Injection (SSTI)

## คำอธิบาย

SSTI เกิดจากการนำ input ของผู้ใช้ไป render ผ่าน template engine
โดยไม่มีการ sanitize หรือจำกัด context อย่างเหมาะสม

ผู้โจมตีสามารถใส่ expression ของ template engine ลงไป
ทำให้ server ประมวลผลโค้ดแทนที่จะเป็นข้อความธรรมดา

ในแลปนี้ ช่อง input ถูกส่งเข้า template โดยตรง
จึงสามารถประเมิน expression และเข้าถึง object ภายใน runtime ได้

## หลักการทำงานโดยย่อ

1. ผู้ใช้ส่ง input
2. Server ส่ง input เข้า template engine
3. Engine ประมวลผล expression
4. ผู้โจมตีสามารถใช้ความสามารถของ engine เพื่อเข้าถึงข้อมูลภายในระบบ

## ผลกระทบ

- อ่านไฟล์ภายในเครื่อง
- เปิดเผยข้อมูลลับ
- ในบางกรณีอาจนำไปสู่ Remote Code Execution
