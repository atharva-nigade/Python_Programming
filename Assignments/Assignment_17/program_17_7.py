# write a program which accept one number and display below Pattern
# input:5
# output:12345
#        12345
#        12345
#        12345
#        12345

def pattern(value):
    for i in range(1,value):
        for j in range(1,value+1):
            print(j,end="\t")
        print()
def main():
    no = 0
    no = int(input("Enter the pattern: "))
    pattern(no)

if __name__ == "__main__":
    main()