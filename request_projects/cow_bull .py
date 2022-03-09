import random
print("Hello welcome to cow bull game")
list1=[0,1,2,3,4,5,6,7,8,9]
list2=random.sample(list1,5)
print(list2)
def cow_bull():
    i=0
    while i<len(list2): 
        j=0
        list3=[] 
        list4=[]
        while j<5:
            sec=int(input("enter your secret number!...."))
            possition=int(input("enter your possition number!...."))
            if list2[possition]==sec:
                if sec not in list3:
                    list3.append(sec)
                    print(list3)
                    print(".....bull.....")
                else:
                    print("....already exixst.....")  
            elif list2[possition]!=sec:
                list4.append(sec)
                print(list4)
                print(".....cow.....")
            else:
                print("....notexist....")
            j+=1
        i+=1
        index=0
        while index<len(list2):
            if list2[index]==list3[index]:
                index+=1
            print("you won the match")
        break
            
cow_bull()

                                                                                                                     


        