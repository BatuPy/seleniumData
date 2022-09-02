import requests


class Github:
    def __init__(self):
        self.apiURL="https://api.github.com"
        self.token="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"
        
        
    def getUser(self,username):
        response=requests.get(self.apiURL+"/users/"+username)
        return response.json()
    
    
    def getRepositories(self,username):
        response=requests.get(self.apiURL+"/users/"+username+"/repos")
        return response.json()
    
    def CreateRepository(self,name): ##BURAYA KADAR HEP BİLGİLERİ ÇEKMİŞTİK GET İLE AMA ARTIK BİLGİYİ ÇEKMEK YERİNE YOLLICAZ
        response=requests.post(self.apiURL+"/user/repos?acces_token="+self.token,json={
            "name":name,
            "description":"This is your first repository",
            "homepage":"https://github.com",
            "private":False,
            "has_issues":True,
            "has_projects":True,
            "has_wiki":True
            })
        return response.json()
    
github=Github()
        


while True:
    secim=input("1-Find User\n2-Get Repositories\nCreate Repository\n4-Exit\nSeçiminizi yapınız: ")
    
    if secim=="4":
        break
    
    else:
        if secim=="1":
            username=input("Kullanıcı adı giriniz: ")
            result=github.getUser(username)
            #print(result)
            print(result["location"])
            print(result["followers"])
        
        elif secim=="2":
            username=input("Kullanıcı adı giriniz: ")
            result=github.getRepositories(username)
            for repo in result:
                print(repo["name"])
                print("*/*/*/*/*/*/*/*/*/*/**/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/**/*/")
                print("*/*/*/*/*/*/*/*/*/*/**/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/**/*/")
                
    
        elif secim=="3":
            name=input("Repository name: ")
            result=github.CreateRepository(name)
            print(result)
        
        else:
            print("YANLIŞ SEÇİM")
            
            
    