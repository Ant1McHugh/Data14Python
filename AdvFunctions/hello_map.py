data14 = ["Katie", "Juxhen", "Joe"]


# for i in range(len(data14)):
#     data14[i] = data14[i].upper()
#
# print(data14)

# data14_upper = map(str.upper, data14)
#
# print(list(data14_upper))
#
# numbers = list(range(1, 100))
# numbers2 = list(range(11, 21))
#
# def square_plus(number, add):
#     square = number * number
#     plus = square + add
#     return plus
#
#
# num_map = map(square_plus, numbers, numbers2)
#
# print(list(num_map))

# students = ["DAVID", "Lee", "RICHARD"]
#
# result = filter(str.isupper, students)
#
# print(list(result))

# def the_truth(number):
#     return number % 3 == 0 and number % 2 == 0
#
#
# numbers = list(range(1, 100))
#
# print(list(filter(the_truth, numbers)))

# def add(n1, n2):
#     return n1 + n2
#
# print(add(2, 2))
#
# add_lambda = lambda n1, n2: n1 + n2
#
# print(add_lambda(2, 2))
#
#
# numbers = [1, 2, 3, 4, 5]
#
# result = map(lambda x: x * x + 3, numbers)
# print(list(result))
#
# savings = [234.00, 555.00, 674.00, 78.00]
#
# bonus = map(lambda x: round(x * 1.1, 2), savings)
# print(list(bonus))
#
# even = list(filter(lambda x: x % 2 == 0, savings))
# print(even)

age = 17

# if age >= 18:
#     print("Go ahead!")
# else:
#     print("Go away!")

print("Go ahead!" if age >= 18 else "Go away!")

print(("Go away!", "Go ahead!")[age >= 18])