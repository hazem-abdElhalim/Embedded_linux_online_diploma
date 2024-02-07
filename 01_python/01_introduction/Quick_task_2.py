passDict = {
    "Ahmed": 1394,
    "Ali": 6078,
    "Amr": 9354
}

x = input("Please enter your username\n").capitalize()
y = input("Please enter your password\n")

if x in passDict:
    if int(y) == passDict[x]:
        print(f"welcome {x} !\n")
    else:
        print("wrong password !\n")
else:
    print("wrong username !\n")