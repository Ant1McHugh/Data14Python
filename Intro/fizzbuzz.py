# Start at 1
# End at 100
# print each number in turn
# if divisable by 3, say fizz
# if divisible by 5, say buzz
# if divisible by both, say fizzbuzz
fizzinput = input("Please choose an alternative to Fizz\n")
buzzinput = input(("Please choose an alternative to Buzz\n"))

while True:
    try:
        startpoint = int(input("Choose a starting number\n"))
    except ValueError:
        print("That is not a valid number, please try again!")
        startpoint = int(input("Choose a starting number\n"))

while True:
    try:
        endpoint = int(input("Choose where to end the cycle\n"))
    except ValueError:
        print("That is not a valid number, please try again!")
        endpoint = int(input("Choose where to end the cycle\n"))

while endpoint <= startpoint:
    print("Your end point must be greater than the start point, please try again!")
    endpoint = input("Choose where to end the cycle\n")

for number in range(startpoint, endpoint):
    if number % 3 == 0 and number % 5 == 0:
        print(str(fizzinput) + str(buzzinput))
    elif number % 3 == 0:
        print(str(fizzinput))
    elif number % 5 == 0:
        print(str(buzzinput))
    else:
        print(number)