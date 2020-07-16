import csv
# scores = []
#
# with open("some_data.csv") as csvfile:
#     csvreader = csv.reader(csvfile)
#     headers = list(map(str.lstrip, next(csvreader)))

#     for row in csvreader:
#         scores.append(int((row[-1])))
#
#
# data_to_write = [["Alex", 1], ["Tim", 2], ["Jane", 4]]
#
# with open("some_data.csv", "a") as csvfile:
#     csv_writer = csv.writer(csvfile)
#
#     csv_writer.writerows(data_to_write)

def read_file(filename):
    with open(filename, "r") as csvfile:
        csv_reader = csv.reader(csvfile)

        return list(csv_reader)

read_file("iris.csv")
iris_headers = 

def find_mean(values):
    mean = sum(values) / len(values)
    return mean




# def means_file(filename):
#
#     find_mean("iris.csv")
#     with open(filename, "w") as csv_file:
#         csv_file.write()
#
#
# means_file("new_file")
