# Payloads

## ขั้นที่ 1: ตรวจสอบ SSRF

ใส่ URL ปกติ เช่น

http://example.com

ผลลัพธ์:
ระบบ fetch เนื้อหาจาก URL และแสดงผลได้
ยืนยันว่า server เป็นคนทำ request

---

## ขั้นที่ 2: ทดสอบ LFI ผ่าน file protocol

```text
file:///etc/passwd
```
