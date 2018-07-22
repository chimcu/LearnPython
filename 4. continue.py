i =0
while True:
    i = i +1
    if i ==2:
        print(("Skipping ") + str(i))
        continue
    if i ==5:
        print(("Breaking at ") + str(i))
        break
    print(i)
print("Finished")