import requests

base_url = "https://webexapis.com/v1"
endpoint = "/webhooks"
header = {"authorization": "Bearer ZjZmN2EyOGQtZjVkOC00NjBhLWFhMjMtZmNhMWFlMjg1N2NmNDUyMGI4MTMtNjQz_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"}
body = {
        "name": "My Awesome Webhook",
        "targetUrl": "https://b57d6bb16a32.ngrok.io",
        "resource": "messages",
        "event": "created"
        }

resp = requests.post(url=base_url+endpoint, headers=header, data=body)
print(resp.status_code)
print(resp.json())