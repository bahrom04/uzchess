from pprint import pprint

from eskiz.client import SMSClient


client = SMSClient(
    api_url="https://notify.eskiz.uz/api/",
    email="magdiyevbahrom@gmail.com",
    password="Bahrom1357",
)

resp = client._send_sms(
    phone_number="998996166018",
    message="Hello from Python❤️"
)
# resp = client._auth()

pprint(resp)