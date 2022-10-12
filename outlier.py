a=int(input("Please input first number:"))
b=int(input("Please input second number:"))
c=int(input("Please input third number:"))
maxN=max(a,b,c)
minN=min(a,b,c)
mid =a+b+c-(maxN+minN)
if (maxN-mid)>(mid-minN):
    print("The outlier is: ",maxN)
elif(mid-minN)>(maxN-mid):
    print("The outlier is: ",minN)
else:
    print("There is no outlier")