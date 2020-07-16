# zerodivision error
# indentation error
# name error
# syntax error
# type error
# key error
# attribute error
# index error
# assertion error
# recursion error

# try:
#     print("Trying to open file...")
#     file = open("order.txt.txt")
#     print("Success.")
# except FileNotFoundError as errmsg:
#     print("Error!")
#     print(errmsg)
#     raise
# finally:
#     print("FINALLY IT HAS HAPPENED TO ME!")
#
# # print("This is the end")
#
# r = Read mode (default)
# w = Write mode (If no file, creates, if there is file, truncates)
# x = Create new file (If already exists, fails)
# a = Append file (If no file, creates instead)
# t = Text mode
# b = Binary mode
# + = Read and Write

def open_and_print(filename):
    try:

        with open(filename) as opened_file:
            file_line_list = opened_file.readlines()

            for line in file_line_list:
                print(line.rstrip("\n"))

    except FileNotFoundError:
        print("That file can not be found")
        raise

open_and_print("order.txt")

# with open("order.txt", "w") as opened_file:
#     opened_file.write("burger\nsalad\nstuffed pasta")
