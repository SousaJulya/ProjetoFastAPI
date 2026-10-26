import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZXhwIjoxNzg3NzA2NjQ3fQ.zAdeN0-S1J06lnHTch3CWnRLK0VzWpRjkulrbjb6wOA"
}

requisicao = requests.get("http://127.0.0.1:8000/auth/refresh", headers = headers)
print(requisicao)
print(requisicao.json())