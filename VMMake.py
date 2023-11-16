import requests
import json

url = "https://management.azure.com/subscriptions/f10b6d16-24b3-4827-82b2-4abaddb09199/resourceGroups/resgroup1/providers/Microsoft.Compute/virtualMachines/vmpython?api-version=2023-07-01"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSIsImtpZCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYS8iLCJpYXQiOjE3MDAxNTE0MzAsIm5iZiI6MTcwMDE1MTQzMCwiZXhwIjoxNzAwMTU1OTg2LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFZBQUFBc2RTemhhbExBSjRlbkFTVnhBSW9Mb0NlcTJUMXBjNDZuSHJHOXViYUdsZkpGQ2hsL0hGOXdrUWh2UTM5Q0JuMm1yZ2F4L2JzNDliWjBFWWk4NHU1cWFHMmZZZENUVHF2a2hNT2RwM1prWmc9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiTXVsaG9sbGFuZCIsImdpdmVuX25hbWUiOiJKb2UiLCJncm91cHMiOlsiODEwOGM1MDMtZDY1Ni00MmNmLThlZTQtODk0NGFlZjBmYWRlIiwiOTdhZjgxMmQtOTZlOS00ZjAxLThhMTEtNzU4MDMzNzYyMTdhIiwiODdmNjAwM2QtOTQ3MC00MzhmLWJmZWYtODEzYjM3ZmMyYjY4IiwiODM4YTI4OWEtODRhNC00Y2E4LWFlZWMtYjMxZWMxZDcxZDRhIiwiNGRjMDNiOWYtMWI2Yy00NDE1LWFjMDUtODI0MjcxM2M3NTIwIiwiNWFkN2Q2YjQtYWRhZi00YjlkLTk1N2YtMGYzYjYxNGJlZTYwIiwiOGFjMTU0ZGQtZDQ1Zi00YzQ2LTk0ZTUtYmI3OGZlZmEzYWVmIiwiOGM4MTg2ZWEtNDJhNC00NGFmLThhNzgtYWU5MTQwMTFlNmI0IiwiZDJhNmE4ZWYtNGQyNi00ZDk1LWJkMTEtYWExZWM2MTlmODE4IiwiYWJkNDlkZmQtY2VmYi00YzM2LWFkNjctMjVmZDlmZmQzMzdmIl0sImlkdHlwIjoidXNlciIsImlwYWRkciI6IjE0Ny4yNTIuMTkuMTgwIiwibmFtZSI6IkMyMTQwNDE2MiBKb2UgTXVsaG9sbGFuZCIsIm9pZCI6IjRkNDQ1NDRlLTlkNjAtNDAxNy05MjE2LWU0NmQ0Y2Q1MGEwNSIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS00MDIyOTg4NDktMTczNDcwNTEzMS0zMTIwMDI0MDAxLTQ0MTUxIiwicHVpZCI6IjEwMDMyMDAxN0RBNDU2NUYiLCJyaCI6IjAuQVRFQXl4ZGpka2pwWDA2TTdOcThqaV9WMmtaSWYza0F1dGRQdWtQYXdmajJNQk14QUdvLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6InIzSmRsRk02LUh5R1BGMGIza3AzUnNBczlNbTN6dGx4R1VfUDdlRmtmc2MiLCJ0aWQiOiI3NjYzMTdjYi1lOTQ4LTRlNWYtOGNlYy1kYWJjOGUyZmQ1ZGEiLCJ1bmlxdWVfbmFtZSI6IkMyMTQwNDE2MkBteXR1ZHVibGluLmllIiwidXBuIjoiQzIxNDA0MTYyQG15dHVkdWJsaW4uaWUiLCJ1dGkiOiJLLWhtdjMwVGlVR3llamd4RjlBakFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NhZSI6IjEiLCJ4bXNfdGNkdCI6MTUyNTMzODk0MX0.R7hh99bAt6sxY-zBFCfhfnhaCSEjcwwXf4wAbar7oTSnTcFaD3ObW8xw-Hzt-ThjbR3vHkzLCM1ciNQ0L-MAyCCXXb-9SfhULFkmZdruvZWUIGOHbJUhjdyuBDL7qt9Ttk-Jj0JULiXGP5yp5wGan-dv7VqhW8I2-BosjHMzUJjbL_FGiRZzXVj4qP4dQbW7BiQS3yepglVeMwrcj6TyP8BjzHNPre9sSpVGq0Qg0T7n7QBDXhT6hSFAFTArl7D5eo8Hvi7yQbMMa1ICOHKuKLC8mfHWhhQCYjfPJmNmcfXaKIgcMoay7m9y_e8TsoNznHk94_ogPVsZCSUDqZZRZQ',
}

data = {
  "id": "/subscriptions/f10b6d16-24b3-4827-82b2-4abaddb09199/resourceGroups/resgroup1/providers/Microsoft.Compute/virtualMachines/vmpython",
  "type": "Microsoft.Compute/virtualMachines",
  "properties": {
    "osProfile": {
      "adminUsername": "azureuser",
      "secrets": [
        
      ],
      "computerName": "vmpython",
      "linuxConfiguration": {
        "ssh": {
          "publicKeys": [
            {
              "path": "/home/azureuser/.ssh/authorized_keys",
              "keyData":"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCXA3w1YrwCxMuggsTG67Lg9AIIWsHqfBbKuMD7vFnj3l3mjsVysg8xppYhgijtnagwrOyqv0Qx0bDw1oaJ5EDg1ChgW9xGe0lOp56gNddg3pVOz2unshiFgS4JIsTwy2MjxoevRLSYr0uH5KQVtKm90irCTo63M4qOVRV3LBioLRhqNXzj34Cu/Jqtwk3t5TkYEnxo4in+26yYLh/++AZ4scNBsThiz6/wYGVkEmFJOPa7RJ7BWHIAtCH3XJFvFftMuT/CZjTpgoxqpknD006n5fQlEQo5VKGYqGmlQr90G6OF0ERtnJxYx/9Z4fG0UU2tgsg/NhPF3+dhPhkOCrhstZ1wowAbvm/xA9Kpzqi9gjNauK49e+QvOT8xUrf0TpoqiJieTAfDCxTrQL6s7rhxs/YapyBCPU7EUE7edtUrzvUVzdKfm91uOkH9SbGXc3zpSJe5gjTnCtruslssZzj4lzp6WzIPwtb3HXec6XdZxgMoFaqoDFYVHMo3ea3U/RU= drenf@LAPTOP-ROI2CO31"
            }
          ]
        },
        "disablePasswordAuthentication": True
      }
    },
    "networkProfile": {
      "networkInterfaces": [
        {
          "id": "/subscriptions/f10b6d16-24b3-4827-82b2-4abaddb09199/resourceGroups/resgroup1/providers/Microsoft.Network/networkInterfaces/ni1",
          "properties": {
            "primary": True
          }
        }
      ]
    },
    "storageProfile": {
      "imageReference": {
        "sku": "16.04-LTS",
        "publisher": "Canonical",
        "version": "latest",
        "offer": "UbuntuServer"
      },
      "dataDisks": [
        
      ]
    },
    "hardwareProfile": {
      "vmSize": "Standard_D1_v2"
    },
    "provisioningState": "Creating"
  },
  "name": "vmpython",
  "location": "westeurope"
}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())