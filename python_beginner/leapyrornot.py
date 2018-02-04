def main():
    a=int(input("Enter a year"))
    if(a%4==0):
        if(a%100==0):
            if(a%400==0):


                print("yes"+str(a)+"is a leap year")
            else:
                print("no"+str(a)+"is not a leap year")
        else:
            print("yes"+str(a)+"is a leap year")
    else:
        print("no"+str(a)+"is not a leap year")


if __name__ == '__main__':
    main()
