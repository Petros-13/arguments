def cube(number):
    return number*number*number

def by_three(number):
    if number%3==0:
        print(cube(number))
    else:
        print("Number is not divisible by 3")

number=int(input("Enter the number: "))
by_three(number)