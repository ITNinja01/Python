import requests

response = requests.get("https://api.ipify.org")
public_ip = response.text
print(f"Your public IP address is: {public_ip}")