# Exercise 01 - XML External Entity (XXE)

## ประเภทของช่องโหว่

XML External Entity (XXE)

## คำอธิบาย

XXE เกิดจากการที่ XML parser อนุญาตให้ใช้ External Entity
ทำให้ผู้โจมตีสามารถกำหนด entity ที่อ้างอิงไฟล์หรือ resource ภายนอกได้

เมื่อ server parse XML ดังกล่าว
ค่าของ entity จะถูกแทนที่ด้วยเนื้อหาจริงของไฟล์

ในแลปนี้ แอปพลิเคชันรับ XML จากผู้ใช้และ parse โดยไม่ได้ปิด external entity
จึงสามารถอ่านไฟล์ภายในเครื่อง server ได้

## หลักการทำงานโดยย่อ

1. ผู้ใช้ส่ง XML ที่มี DOCTYPE และ external entity
2. XML parser โหลด entity ตามที่กำหนด
3. เนื้อหาไฟล์ถูกแทนที่ลงใน XML
4. server ส่งผลลัพธ์กลับมาให้ผู้ใช้

## ผลกระทบ

- อ่านไฟล์ภายในระบบ
- เปิดเผยข้อมูลลับ
- อาจนำไปสู่ SSRF หรือ RCE ในบางกรณี
