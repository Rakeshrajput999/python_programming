def arithmatic(x,y, operation=["+","-"]):
    if (operation=="+"):
        return x+y
    elif(operation=="-"):
        return x-y
    else :
        return "apply valid operation"

print(arithmatic(2,3,"-"))