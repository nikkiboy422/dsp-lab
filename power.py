x=int(input("enter the base value="))
n=int(input('enter the power value'))
def power(x,n):
    if n==0:
        return 1
    else:
        return(x*power(x,n-1))
print(power(x,n))
