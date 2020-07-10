# shopping_list = ["eggs", "bacon", "sausages", "bread"]
# colours = ["blue", "yellow", "green"]
#
# for badass in shopping_list:
#     for colour in colours:
#         print(badass, colour)

# menu = {
#     1: {"dish": "egg fried rice", "price": 5.99},
#     2: {"dish": "chicken chow mein", "price": 12.99},
#     3: {"dish": "duck pancakes", "price": 8.99},
#     4: {"dish": "spring rolls", "price": 6.99}
# }
#
# for key in menu:
#     choice = input(f"Would you like to order the {menu[key]['dish']}?\n")
#     if choice == "yes":
#         print(f"That will be {menu[key]['price']}!")
#     else:
#         print("That is fine!")

age = ""

while not age.isnumeric():
    age = input("Enter your age:\n")
    if not age.isnumeric():
        print("That's not a number, try again!")

age = int(age)
print(f"You are {age} years old!")