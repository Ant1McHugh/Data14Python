# Start at 1
# End at 100
# print each number in turn
# if divisable by 3, say fizz
# if divisible by 5, say buzz
# if divisible by both, say fizzbuzz

fizz_input = input("Please choose an alternative to Fizz\n")

buzz_input = input("Please choose an alternative to Buzz\n")

start_point = input("Choose a starting number\n")

while not start_point.isnumeric():
    print("Please enter a valid number")
    start_point = input("Choose a starting number\n")

end_point = input("Choose where to end the cycle\n")

while not end_point.isnumeric():
    print("Please enter a valid number")
    end_point = input("Choose where to end the cycle\n")

while end_point <= start_point:
    print("Your end point must be greater than the start point, please try again!")
    end_point = input("Choose where to end the cycle\n")

while not end_point.isnumeric():
    print("Please enter a valid number")
    end_point = input("Choose where to end the cycle\n")

for number in range(int(start_point), int(end_point)):
    if number % 3 == 0 and number % 5 == 0:
        print(f"{fizz_input}{buzz_input}")
    elif number % 3 == 0:
        print(f"{fizz_input}")
    elif number % 5 == 0:
        print(f"{buzz_input}")
    else:
        print(number)