import requests
import json

url = "https://management.azure.com/subscriptions/f10b6d16-24b3-4827-82b2-4abaddb09199/resourcegroups/resgroup1?api-version=2021-04-01"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSIsImtpZCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYS8iLCJpYXQiOjE3MDAxNDgwNjMsIm5iZiI6MTcwMDE0ODA2MywiZXhwIjoxNzAwMTUyMzk3LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFZBQUFBOU9oNlhINFhSOWppVCtLdmlxY3JmNkNnSXJTZmM1K2M0MGtpOFBoRUlXbWNtd0t3aTVSN2ZBUGoyRVBMUHBnSGZ3UDRMeTJYUTVwVDVyeHljUnRnR05pblBLckIzTFZLUU5jb0hNVVo4TVk9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiTXVsaG9sbGFuZCIsImdpdmVuX25hbWUiOiJKb2UiLCJncm91cHMiOlsiODEwOGM1MDMtZDY1Ni00MmNmLThlZTQtODk0NGFlZjBmYWRlIiwiOTdhZjgxMmQtOTZlOS00ZjAxLThhMTEtNzU4MDMzNzYyMTdhIiwiODdmNjAwM2QtOTQ3MC00MzhmLWJmZWYtODEzYjM3ZmMyYjY4IiwiODM4YTI4OWEtODRhNC00Y2E4LWFlZWMtYjMxZWMxZDcxZDRhIiwiNGRjMDNiOWYtMWI2Yy00NDE1LWFjMDUtODI0MjcxM2M3NTIwIiwiNWFkN2Q2YjQtYWRhZi00YjlkLTk1N2YtMGYzYjYxNGJlZTYwIiwiOGFjMTU0ZGQtZDQ1Zi00YzQ2LTk0ZTUtYmI3OGZlZmEzYWVmIiwiOGM4MTg2ZWEtNDJhNC00NGFmLThhNzgtYWU5MTQwMTFlNmI0IiwiZDJhNmE4ZWYtNGQyNi00ZDk1LWJkMTEtYWExZWM2MTlmODE4IiwiYWJkNDlkZmQtY2VmYi00YzM2LWFkNjctMjVmZDlmZmQzMzdmIl0sImlkdHlwIjoidXNlciIsImlwYWRkciI6IjE0Ny4yNTIuMTkuMTgwIiwibmFtZSI6IkMyMTQwNDE2MiBKb2UgTXVsaG9sbGFuZCIsIm9pZCI6IjRkNDQ1NDRlLTlkNjAtNDAxNy05MjE2LWU0NmQ0Y2Q1MGEwNSIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS00MDIyOTg4NDktMTczNDcwNTEzMS0zMTIwMDI0MDAxLTQ0MTUxIiwicHVpZCI6IjEwMDMyMDAxN0RBNDU2NUYiLCJyaCI6IjAuQVRFQXl4ZGpka2pwWDA2TTdOcThqaV9WMmtaSWYza0F1dGRQdWtQYXdmajJNQk14QUdvLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6InIzSmRsRk02LUh5R1BGMGIza3AzUnNBczlNbTN6dGx4R1VfUDdlRmtmc2MiLCJ0aWQiOiI3NjYzMTdjYi1lOTQ4LTRlNWYtOGNlYy1kYWJjOGUyZmQ1ZGEiLCJ1bmlxdWVfbmFtZSI6IkMyMTQwNDE2MkBteXR1ZHVibGluLmllIiwidXBuIjoiQzIxNDA0MTYyQG15dHVkdWJsaW4uaWUiLCJ1dGkiOiJGd25ZSFBPUDUwcXc0bzZYTWIwWkFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NhZSI6IjEiLCJ4bXNfdGNkdCI6MTUyNTMzODk0MX0.vAKa6TlQe9Mc25jDpIrhu7uAzwq5dwBIvH48Qee541mVwJ55VcRaaQtxEhk6ksuq_-Nb7BpJnvX60SdL8d6qwfYxt4JHcC9OlFeQOg5WAJ7lPhp0GQOd19xUKAmbchm6woAvH1AfQ8aDiKZkpyI2iTpj_-_0aZfRs1Eom1GNdE7w1XMxXkMQR43se4S8bcHvw6AjH5AH3TPb9JVcb8CJfjTFXf6dqRfXkJ9N436pzIJxgmcX_HDdcoZeqmfu0KfrHn687IPlzshwoivMU3ffthm0Wff-Kxsac4BfBkDjCARALhMb0n3478dwCORC1RMp4zicEbar3i9uh-EKGA3EHQ',
}

data = {

    'location': "westeurope"

}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())