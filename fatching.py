import requests 

url='https://vgmlinks.fun/thcmvj000333327/'

response=requests.post(url)

data=response.text



with open("m0.txt", "w", encoding="utf-8") as f:
    f.write(data)
