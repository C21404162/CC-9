import requests
import json

url = "https://management.azure.com/subscriptions/f10b6d16-24b3-4827-82b2-4abaddb09199/resourceGroups/resgroup1/providers/Microsoft.Network/networkInterfaces/ni1?api-version=2023-05-01"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSIsImtpZCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYS8iLCJpYXQiOjE3MDAxNDkwMzQsIm5iZiI6MTcwMDE0OTAzNCwiZXhwIjoxNzAwMTU0NDU3LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFZBQUFBY0dEb0Rwb3RQTWFpeTlKVVBPTGFYUHFFTVNVdXFaRXp5Z2ZRakRzb3hubmZmL3BLM3pjM3RkaStpY0VucDJldklGUmEvc3BkdGpGUXNUdzEyMnRVZG80Mks2dWxHVXdWSXhnN2ZQOFFWQWc9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiTXVsaG9sbGFuZCIsImdpdmVuX25hbWUiOiJKb2UiLCJncm91cHMiOlsiODEwOGM1MDMtZDY1Ni00MmNmLThlZTQtODk0NGFlZjBmYWRlIiwiOTdhZjgxMmQtOTZlOS00ZjAxLThhMTEtNzU4MDMzNzYyMTdhIiwiODdmNjAwM2QtOTQ3MC00MzhmLWJmZWYtODEzYjM3ZmMyYjY4IiwiODM4YTI4OWEtODRhNC00Y2E4LWFlZWMtYjMxZWMxZDcxZDRhIiwiNGRjMDNiOWYtMWI2Yy00NDE1LWFjMDUtODI0MjcxM2M3NTIwIiwiNWFkN2Q2YjQtYWRhZi00YjlkLTk1N2YtMGYzYjYxNGJlZTYwIiwiOGFjMTU0ZGQtZDQ1Zi00YzQ2LTk0ZTUtYmI3OGZlZmEzYWVmIiwiOGM4MTg2ZWEtNDJhNC00NGFmLThhNzgtYWU5MTQwMTFlNmI0IiwiZDJhNmE4ZWYtNGQyNi00ZDk1LWJkMTEtYWExZWM2MTlmODE4IiwiYWJkNDlkZmQtY2VmYi00YzM2LWFkNjctMjVmZDlmZmQzMzdmIl0sImlkdHlwIjoidXNlciIsImlwYWRkciI6IjE0Ny4yNTIuMTkuMTgwIiwibmFtZSI6IkMyMTQwNDE2MiBKb2UgTXVsaG9sbGFuZCIsIm9pZCI6IjRkNDQ1NDRlLTlkNjAtNDAxNy05MjE2LWU0NmQ0Y2Q1MGEwNSIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS00MDIyOTg4NDktMTczNDcwNTEzMS0zMTIwMDI0MDAxLTQ0MTUxIiwicHVpZCI6IjEwMDMyMDAxN0RBNDU2NUYiLCJyaCI6IjAuQVRFQXl4ZGpka2pwWDA2TTdOcThqaV9WMmtaSWYza0F1dGRQdWtQYXdmajJNQk14QUdvLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6InIzSmRsRk02LUh5R1BGMGIza3AzUnNBczlNbTN6dGx4R1VfUDdlRmtmc2MiLCJ0aWQiOiI3NjYzMTdjYi1lOTQ4LTRlNWYtOGNlYy1kYWJjOGUyZmQ1ZGEiLCJ1bmlxdWVfbmFtZSI6IkMyMTQwNDE2MkBteXR1ZHVibGluLmllIiwidXBuIjoiQzIxNDA0MTYyQG15dHVkdWJsaW4uaWUiLCJ1dGkiOiItV0g3a3ROMjIwU1VCV1QxaW4waUFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NhZSI6IjEiLCJ4bXNfdGNkdCI6MTUyNTMzODk0MX0.OHFeWuCVBL7PcO5hVR0LL8fpsQRtCc-KQ57l1-M0XDxFdoPD1Ylh459kd-STn67uCuN05UZg39HfZTlvexHkCcbHQo4fEKRdyovMcWSJ7PAXRuAL97Tsi3gaoLInY2J2umwHq-2S9QkYH6ZVnZctVkeKlLuuSp63aZEbOeKZf4nANjgzPXFTiuzpGHyBIAdo2zMNXt3pbqCX_bTP6zSwtB4fWiGFiOLBSTxs8Exl-EHLqJhIvjpmqUArvSX2cxiK8LM5kHFo986oboUPKKAXKF22yyRU5XRIbEMGyZPKlyneuu3nz593QRnsoqp6PV8eI7cEwj5fK3z8uQMGZpvgQQ',
}

data = {
  "properties": {
    "ipConfigurations": [
      {
        "name": "ipconfig1",
        "properties": {
          "publicIPAddress": {
            "id": "/subscriptions/f10b6d16-24b3-4827-82b2-4abaddb09199/resourceGroups/resgroup1/providers/Microsoft.Network/publicIPAddresses/ips1"
          },
          "subnet": {
            "id": "/subscriptions/f10b6d16-24b3-4827-82b2-4abaddb09199/resourceGroups/resgroup1/providers/Microsoft.Network/virtualNetworks/vn1/subnets/subnet1"
          }
        }
      }
    ]
  },
  "location": "westeurope"
}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())