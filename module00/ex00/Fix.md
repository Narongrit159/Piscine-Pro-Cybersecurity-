## วิธีป้องกัน

1. ห้ามใช้ innerHTML กับข้อมูลจากผู้ใช้ ให้ใช้ textContent แทน
2. ไม่ควรสร้าง script จาก input ของผู้ใช้โดยตรง
3. ตรวจสอบและ validate input ก่อนนำไปใช้งาน
4. ตั้งค่า cookie เป็น HttpOnly เพื่อป้องกันการถูกอ่านด้วย JavaScript
5. Escape output ทำให้ข้อมูลที่จะแสดงผล กลายเป็นข้อความธรรมดา ทุกครั้งก่อน render บนหน้าเว็บ

## ตัวอย่างการแก้ไข

จาก:

document.getElementById("output").innerHTML = userInput;

แก้เป็น
document.getElementById("output").textContent = userInput;
