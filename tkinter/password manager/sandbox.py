try:
    file = open("some_file.txt")
    a_dict = {"key":"value"}
    print(a_dict["sssss"])
except:
    file = open("some_file.txt", "w")
    file.write("Something")
    # print("File does not exist.")