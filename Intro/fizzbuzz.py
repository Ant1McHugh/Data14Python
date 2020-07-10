# Start at 1
# End at 100
# print each number in turn
# if divisable by 3, say fizz
# if divisible by 5, say buzz
# if divisible by both, say fizzbuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)