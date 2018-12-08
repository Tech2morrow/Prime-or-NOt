# function to test prime or not

def prime(n):
    if(n==2):
        print("Prime : ) ")
    elif n<2:
        print("2")
        exit()
    elif n%2 == 0:
        print("Not a Prime : ( ")


    else:
        print("Prime : ) ")


try:
    x = int(input("Enter Number : "))

    prime(x)


except ValueError:
    print("Enter an integer")