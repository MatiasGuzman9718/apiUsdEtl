import requests
import json

url = 'https://api.estadisticasbcra.com/usd'
token = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzQ3MTA2NzAsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJmZDkxMzUxMkBnbWFpbC5jb20ifQ.eKVpt1Uwxvsde_Kf2kLW6CHvK3F74kw-9f3U_cJ376ebemQ2bztEJkvEZk6UeSGln3SZV2nR2YtAC4RlN7myVw"

headers = {
    "Authorization" : f"BEARER {token}"
}

try:

    response = requests.get(url , headers= headers)
    response = response.json()
    #print(response)
    data = response
except Exception as ex: 
    print(f"El error que se genero es: {ex}")

print(data)