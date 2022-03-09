import json

from click import password_option
print("1.signup")
print("2.Login")
no_1="signup"
no_2="login"
no=int(input("enter the no"))
if no_1=="signup":
    print(no_1)
    print("you choose signup")
    name=(input("enter you username"))
        # with open("details.json","w") as f:
        #     f.write(name)
        # if name in (details.json):
        #     print("this name is already exist you have to choose another one")
        
    pas1=input("enter your password_1......")
    if len(pas1)>=4 and "@" in pas1 or "#"  in pas1:
        if pas1>='a' or pas1<='z':
            if pas1>='A'and pas1<='Z':
                r=["0","1","2","3","4","5","6","7","8","9"]
                i=0
                while i<len(r):
                    if r[i] in pas1:
                        print("your password is strong password")
                        pas2=(input("enter your passsword_2"))
                        print("both password should be the same")
                        if pas1!=pas2:
                            print(" error, because your both password are not same")
                        print("CONGRATS----",name,"YOU ARE SIGNEDUP SUCESSFULLY------")
                        dict={}
                        dict2={}
                        lis=[]
                        dict["name"]=name
                        lis.append(dict)
                        dict2["password"]=pas1
                        lis.append(dict2)
                        with open("detail.json","w") as file:
                            json.dump(lis,file,indent=0)
                    else:
                        print("num is not found ")
                        break
                    i=i+1
                else:
                    print("num is found ")
            else:
                print("capital alphabet is not found")
        else:
            print("small charcter is found")
    else:
        print("your simble is not found ")
        # pas2=(input("enter your passsword_2"))
        # print("both password should be the same")
        # if pas1!=pas2:
        #     print(" error, because your both password are not same")
        # print("CONGRATS----",name,"YOU ARE SIGNEDUP SUCESSFULLY------")
        # dict={}
        # dict2={}
        # lis=[]
        # dict["name"]=name
        # lis.append(dict)
        # dict2["password"]=pas1
        # lis.append(dict2)
        # with open("detail.json","w") as file:
        #     json.dump(lis,file,indent=0)
        
        
    
    if no_2=="login": 
        print(no_2) 
        username=(input("enter the username----"))
        password_=(input("enter the password")) 
        if len(pas1)>=4 and "@" in pas1 or "#"  in pas1:
            if pas1>='a' or pas1<='z':
                if pas1>='A'and pas1<='Z':
                    r=["0","1","2","3","4","5","6","7","8","9"]
                    i=0
                    while i<len(r):
                        if r[i] in pas1:
                            print("your password is strong password")
                            break
                        else:
                            print("num is not found ")
                            break
                        i=i+1
                    else:
                            print("num is found ")
                else:
                        print("capital alphabet is not found")
            else:
                    print("small charcter is found")
        else:
            print("your simble is not found ")
        
    else:
        print("sorry you have to choose only 1 or 2")
        
                           