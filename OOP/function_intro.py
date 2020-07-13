# def print_something():
#     print("Something")
#
#
# print_something()
#
# def print_something_multiply(something, number_of_times):
#     string_to_print = something * number_of_times
#     print(string_to_print)
#
#
# print_something_multiply("woohoo", 3)

# def addition(number_one, number_two=3):
#     return number_one + number_two
#
#
# print(addition(1))

# def find_stock(*multiargs):
#     if len(multiargs) < 1:
#         return None
#     else:
#         product = 1
#         for number in multiargs:
#             product = product * number
#         return product
#
#
# print(find_stock(1, 2, 3, 4, 5))