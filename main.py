print("client list are given below")
c1="farhan"
c2="rehan"
c3="kashan"
print(c1)
print(c2)
print(c3)

# date and time function
def getdate():
    import datetime
    return datetime.datetime.now()

#log function
def log_diet_excercize():
    """"in this function you can log or enter your daily excercise or diet """
    n=int(input("press 1 for farhan ,2 for rehan and 3 for kashan :"))

    de=int(input(" enter 1 for Diet and 2 for Excercise :"))

    if n==1:
        if de==1:
            print(c1, "diet routine")
            khana=input("kia khaya ?\n")
            f=open("farhandiet.txt","r+")
            f.write(str([str(getdate())])+ ":"+ khana+"\n")
            print("added")
            f.close()
        elif de==2:
            print(c1, "excercize routine")
            warzish=input("konsi excercise ki ?\n")
            f=open("farhanexc.txt","r+")
            f.write(str([str(getdate())])+":"+ warzish+"\n")
            print("added")
            f.close()
        else:
            print("please enter right inforamation")
    if n==2:
        if de==1:
            print(c2, "diet routine")
            khana=input("kia khana khaya ?\n")
            with open("rehandiet.txt","r+") as f:
                f.write(str([str(getdate())])+":"+khana+"\n")
                print("added")
        elif de==2:
            print(c2, "excercize routine")
            warzish=input("konsi excercize ki ?\n")
            with open("rehanexc.txt","r+") as f:
                f.write(str([str(getdate())])+" :"+warzish+"\n")
                print("added")
        else:
            print("plz enter correct information")

    if n == 3:

        if de == 1:
            print(c3,"diet routine")
            khana = input("kia khana khaya ?\n")
            with open("kashandiet.txt.txt", "r+") as f:
                f.write(str([str(getdate())]) + ":" + khana + "\n")
                print("added")
        elif de == 2:
            print(c3, "excercize routine")
            warzish = input("konsi excercize ki ?\n")
            with open("kashanexc.txt", "r+") as f:
                f.write(str([str(getdate())]) + " :" + warzish + "\n")
                print("added")
        else:
            print("plz enter correct information")


#read function
def read_report():
    """"here you can read client daily routine """
    print("konse client report dekhni ? \n")
    n = int(input("press 1 for farhan ,2 for rehan and 3 for kashan :"))
    de=int(input("enter 1 for diet and 2 for excercize :"))

    if n==1:
        if de==1:
         print(c1,"diet report :\n")
         with open("farhandiet.txt") as f:
             print(f.read(), "\n")
        elif de==2:
            print(c1," excercize report :\n")
            with open("farhanexc.txt") as f:
                print(f.read(),"\n")
        else:
            print("plz enter correct inforamtion :")

    if n==2:
        if de==1:
         print(c2,"diet report :\n")
         with open("rehandiet.txt") as f:
             print(f.read(), "\n")
        elif de==2:
            print(c2," excercize report :\n")
            with open("rehanexc.txt") as f:
                print(f.read(), "\n")
        else:
            print("plz enter correct inforamtion :")

    if n==3:
        if de==1:
         print(c3,"diet report :\n")
         with open("kashandiet.txt") as f:
             print(f.read(), "\n")
        elif de==2:
            print(c3," excercize report :\n")
            with open("kashanexc.txt.txt") as f:
                print(f.read(),"\n")
        else:
            print("plz enter correct inforamtion :")

#what funtion you want to run

fun = int(input("enter 1 for log inforamtion and 2 for see/read client report : "))

if fun == 1:
    log_diet_excercize()
elif fun == 2:
    read_report()
else:
    print("plz give right information ")
print("today date is 25-10-21")
