import requests

auth = "ZjZmN2EyOGQtZjVkOC00NjBhLWFhMjMtZmNhMWFlMjg1N2NmNDUyMGI4MTMtNjQz_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
base_url = "https://webexapis.com/v1"
endpoint = "/rooms"
param = "?sortBy=lastactivity"

header = {'authorization': 'Bearer ZjZmN2EyOGQtZjVkOC00NjBhLWFhMjMtZmNhMWFlMjg1N2NmNDUyMGI4MTMtNjQz_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'}

resp = requests.get(url=base_url+endpoint+param, headers=header)
print(resp.status_code)
print(resp.json())