import base64

with open("/Volumes/Macintosh HD - Données/WCS/qip/private_key.pem", "rb") as f:
    key_data = f.read()
    encoded_key = base64.b64encode(key_data).decode('utf-8')

print(encoded_key)
