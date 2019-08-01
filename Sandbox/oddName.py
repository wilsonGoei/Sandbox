"""Wilson Goei Gujatno"""
name = str(input("Please input your name: "))
while name == "":
    print("Input cannot be blank")
    name = str(input("Please input your name: "))
print(name[0::2])