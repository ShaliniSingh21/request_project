import json   
import os 
print("1.Signup/n 2.login")

user=int(input("enter your choice="))

list=[]
dict={"user":list}
dict1={}
if user==1:
    username=input("enter name=")
    password1=input("enter  password=")
    password2=input("enter password again=")
    if password1==password2:
        digit=0
        special_chr=0
        upper=0
        lower=0
        for i in password1:
            if (i.isupper()):
                upper+=1
            if (i.isdigit()): 
                digit+=1 
            if (i.islower()):   
                lower+=1
            if(i=='@'or i=='$' or i=='_' or i=='#' or i=="!" or i=="%" or i=="^" or i=="&" or i=="*" or i=="(" or i==")"):
                special_chr+=1
        if upper>=1 and digit>=1 and lower>=1 and special_chr>=1:   
            if os.path.exists("details json")==True:
                with open ("details json") as file_1:
                    m=json.load(file_1)
                    n=m["user"]
                    for i in m:
                        if i["username"]==username:
                            print("gnjkfdkjj")
                            break
                        else:
                            print("congrats!", username,"you sucessfully registered")
                            birthdate = input("enter your birthdate = ")
                            hobbies = input("enter your hobbiees = ")
                            gender = input("enter your gender = ")
                            dict1={"password":password1,"username":username,"birthdate":birthdate,"hobbies":hobbies,"gender":gender}

                            if os.path.exists("details.json")==True:
                                with open("details.json") as file:
                                    k=json.load(file)
                                    l=k["user"]
                                    l.append(dict1)
                                    dict1["user"]=l
                                    with open("details.json","w") as file1:
                                        json.dump(dict,file1,indent=4)
                                        break
                            else:
                                list.append(dict1)
                                k=open("details.json","w")
                                json.dump(dict,k,indent=4)
                                break
            else:
                print("congrats!", username,"you sucessfully registered")
                birthdate = input("enter your birthdate = ")
                hobbies = input("enter your hobbiees = ")
                gender = input("enter your gender = ")
                dict1["password"]=password1
                dict1["username"]=username
                dict1["birthdate"]=birthdate
                dict1["hobbies"]=hobbies
                dict1["gender"]=gender

                if os.path.exists("userdetails.json")==True:
                    with open("userdetails.json") as file:
                        k=json.load(file)
                        l=k["user"]
                        l.append(dict1)
                        dict1["user"]=l
                        with open("details.json","w") as file1:
                            json.dump(dict,file1,indent=4)
                else:
                    list.append(dict1)
                    k=open("details.json","w")
                    json.dump(dict,k,indent=4)
        else:
            print("at least password should contain one special character,number,lowercase and uppercase character")

    else:
        print("both password are not same")
                            
                
                            
   # url,https,http,api,slug,request,response,rest api, (get,post,put, delete, upadte)