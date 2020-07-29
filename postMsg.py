import requests

base_url = "https://webexapis.com/v1"
endpoint = "/messages"
header = {"authorization": "Bearer ZjZmN2EyOGQtZjVkOC00NjBhLWFhMjMtZmNhMWFlMjg1N2NmNDUyMGI4MTMtNjQz_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"}
body = {"roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGQ1MjFiNDEtYTA0OC0zODg2LWI3ZTQtMzQ0NjE3MjU4YzRh",
        "text": "Hello I'm Cert Bot"
        }

resp = requests.post(url=base_url+endpoint , headers=header, data=body)
print(resp.status_code)
print(resp.json())