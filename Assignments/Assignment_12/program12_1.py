# Write a program which accpects one character and checks whether it is vowel or consonant 


def vowel(value):
    if (value == 'a' and 'e 'and 'i' and 'o'and 'u'):
        return True
    else:
        return False


def main():
    ret = ''
    print("enter one character:")
    char = input()
    ret = vowel(char)

    if ( ret == True):
        print("it is a vowel")
    else:
        print("it is a consonant")


if __name__ == "__main__":
    main()