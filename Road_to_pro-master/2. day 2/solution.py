def reverse(x):
    sign =-1 if x<0 else 1
    x=abs(x)
    result =0
    while x>0:
        digit = x%10
        result = result *10 +digit
        x//=10
    result*=sign 
    if result<-2**31 or result>2**31-1:
        return 0;
    else:
        return result
def main():
    num =int(input("enter the number you want to reverse: "))
    reversed_num = reverse(num)
    print("the reversed number is:",reversed_num)

main()
 
            
        