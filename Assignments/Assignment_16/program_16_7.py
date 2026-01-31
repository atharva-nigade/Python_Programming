# write a program which accepts number from user and check whether that number is positive or negative or zero 
# input:11 output:positive number
# input:-11 output:negative number
# input:0 output:zero

def ChkNum(value):
    if ( value > 0):
      return "Positive Number"
    elif(value<0):
      return"Negative Number"
    else:
       return"zero"
      
 
def main():
    ret=0
    No=int(input("Enter the number: "))
    ret = ChkNum(No)
    print(ret)
 
if __name__ == "__main__":
    main()