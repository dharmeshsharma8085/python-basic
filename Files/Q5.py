with open("number.txt","r") as f:
    data=f.read()
    print(data)
    
    num=""
    for i in range(len(data)):
        if(data[i]=="'"):
            print(num)
            num=""
        else:
            num+=data[i]
            