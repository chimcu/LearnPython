file = open("D:\\Python\\Hello.py", "r")
print(file.readline())
#    print(line)
file.close()

#file = open("D:\\Python\\Hello.py", "r")
#for line in file:
#    print(line)
#file.close()

x = len(open("test.txt").readlines())
print(x)