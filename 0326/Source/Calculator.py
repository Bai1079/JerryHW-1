from Source import func
x=input("請輸入你要做的動作(+,-,*,/): ")
n1=int(input("請輸入第一個數: "))
n2=int(input("請輸入第二個數: "))
if x == "+":
    print(func.addfunc(n1,n2))
elif x == "-":
    print(func.minusfunc(n1,n2))
elif x == "*":
    print(func.multiplyfunc(n1,n2))
else:
    print(func.dividefunc(n1,n2))
    
