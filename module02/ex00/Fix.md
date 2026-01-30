# วิธีป้องกันช่องโหว่ Insecure Deserialization

## แนวทางหลัก

### 1. หลีกเลี่ยงการใช้ pickle กับข้อมูลจากผู้ใช้

ไม่ควรใช้ `pickle.loads()` กับ input ที่มาจาก client โดยเด็ดขาด

---

### 2. ใช้ format ที่ปลอดภัยกว่า

เช่น

- JSON
- XML (พร้อมปิด external entity)
- MessagePack (แบบจำกัด schema)

---

### 3. หากจำเป็นต้อง deserialize จริงๆ

- ใช้ custom Unpickler
- จำกัด class ที่อนุญาต (allowlist)
- ห้ามเรียก function อันตราย

---

### 4. ตรวจสอบ input เสมอ

- validation
- schema checking
- length checking

---

### 5. จำกัดสิทธิ์ของแอปพลิเคชัน

- ห้ามรันด้วย root
- ใช้ user สิทธิ์ต่ำ
- แยก container

---

### 6. เพิ่มการตรวจจับ

- logging
- monitoring
- alert เมื่อมีพฤติกรรมผิดปกติ

---

## สรุป

ต้นเหตุของปัญหาคือ

"การเชื่อข้อมูลจากผู้ใช้มากเกินไป"

แนวทางแก้คือ

- ไม่ deserialize มั่ว
- ไม่ trust client
- ไม่รันเว็บด้วยสิทธิ์สูง

เพียงเท่านี้ก็ลดความเสี่ยง RCE ได้อย่างมาก
