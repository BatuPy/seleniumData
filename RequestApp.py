import requests
import json

result=requests.get("https://jsonplaceholder.typicode.com/todos")
result=json.loads(result.text)


#print(result)
print(result[0]["title"])
print(result[0])


for i in result:
    #print(i["title"])
    print(i["userId"])
    print(i) 
    
    
    
#Exchange API

import requests
import json

apiURL="https://api.apilayer.com/exchangerates_data/latest?base="
headers= {
  "apikey": "x6EDEGcMAEnjtl5i8voOpVcxgvAf48cs"
}

bozulanDoviz=input("Bozulan Döviz Türü: ")
alinanDoviz=input("Alınan Döviz Türü: ")
miktar=int(input(f"Ne kadar {bozulanDoviz} bozdurmak istiyorsunuz? "))


result=requests.get(apiURL+bozulanDoviz,headers=headers)
result=json.loads(result.text)
karsilik=result["rates"][alinanDoviz]*miktar
print(f"1 {bozulanDoviz} = {result['rates'][alinanDoviz]}  ")
print(f" Bozdurdugunuz miktarın {alinanDoviz} olarak karşılığı {karsilik} {alinanDoviz}'dir.")
























