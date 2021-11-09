try:
    file = open("some_file.txt")
    a_dict = {"key":"value"}
    print(a_dict["sssss"])
except FileNotFoundError:
    file = open("some_file.txt", "w")
    file.write("Something")
    # print("File does not exist.")
except KeyError:
    print("Value does not exist.")