from logic import command_parse 
with open("test.txt", "r") as testf:
    tests = [i.rstrip("\n") for i in testf.readlines() if i[0] != '#'] 
    for test in tests:
        print(command_parse(test))
