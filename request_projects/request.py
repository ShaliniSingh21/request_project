import json
import requests
url = "http://saral.navgurukul.org/api/courses" 
res=requests.get(url)
# print(type(a))
data_text=res.json()
# print(type(data_text))
with open ("requests.json","w") as f:
        json.dump(data_text,f,indent=4)
  
def course():
        index=0
        for i in data_text["availableCourses"]:
                print(index+1, i["name"],i["id"])
                index=index+1
        # for c in data_text["availableCourses"]:   
        course=int(input("select your course:")) 
        c=0
        for j in data_text["availableCourses"]: 
                c+=1
                if c==course:
                        var=requests.get("https://saral.navgurukul.org/api/courses/"+j["id"]+"/exercises")
                        data2=var.json()
                        for k in data2:
                                a=data2[k]
                                count=0
                                for x in  a:
                                        count+=1
                                        print(count,x["name"])
                                c1=0
                                user2=int(input("enter serial number for slug= "))
                                for y in a:
                                        c1+=1
                                        if user2==c1:
                                                var2=requests.get("http://saral.navgurukul.org/api/courses/"+j["id"]+"/exercise/getBySlug?slug="+y["slug"])
                                                data3=var2.json()
                                                print(data3)

course()
      
                 



 
                