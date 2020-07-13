# Start at 1
# End at 100
# print each number in turn
# if divisable by 3, say fizz
# if divisible by 5, say buzz
# if divisible by both, say fizzbuzz

def numeric_check(value):
    while not value.isnumeric():
        value = input("Please enter a valid number\n")
    return value


fizz_input = input("Please choose an alternative to Fizz\n")

buzz_input = input("Please choose an alternative to Buzz\n")

start_point = input("Choose a starting number\n")

start_point = int(numeric_check(start_point))

end_point = input("Choose where to end the cycle\n")

end_point = int(numeric_check(end_point))

while end_point <= start_point:
    print("Your end point must be greater than the start point, please try again!")
    end_point = input("Choose where to end the cycle\n")


def fizzbuzz_game(start, end):
    for number in range(int(start), int(end)):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{fizz_input}{buzz_input}")
        elif number % 3 == 0:
            print(f"{fizz_input}")
        elif number % 5 == 0:
            print(f"{buzz_input}")
        else:
            print(number)


print(fizzbuzz_game(start_point, end_point))