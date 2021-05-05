lower =int(input("Enter the lower value"))
upper=int(input("Enter the upper value"))
for num in range(lower,upper):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
