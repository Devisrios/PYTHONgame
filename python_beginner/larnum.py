def main():
    a=int(input("Enter a number"))
    b=int(input("Enter second number"))
    c=int(input("Enter third number"))
    if(a>=b and a>=c):
        print(str(a) +"is a largest number among three numbers")
    elif(b>=a and b>=c):
        print(str(b) +"is a largest number among three numbers")
    else:
        print(str(c) +"is a largest number among three numbers")


if __name__ == '__main__':
    main()
