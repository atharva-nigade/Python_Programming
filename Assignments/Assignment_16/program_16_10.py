# write a program which display first 10 even numbers 
# output: 2 4 6 8 10 12 14 16 18 20
def display():
    i = 1
    EvenCount = 0
    while(EvenCount < 10):
        if(i % 2 == 0):
            print(i, end="\t")
            EvenCount = EvenCount + 1
        i = i+1

def main():
    display()

if __name__ == "__main__":
    main()