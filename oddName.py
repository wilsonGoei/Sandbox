"""Wilson Goei Gujatno"""
name = str(input("Please input your name:\n>>> "))
while name == "":
    print("Input cannot be blank")
    name = str(input("Please input your name:\n>>> "))
print(name[0::2])