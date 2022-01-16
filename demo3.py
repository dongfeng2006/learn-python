while True:
    s = input("请输入一个名字，按Q退出")
    if s == "Q":
        break
    for c in s:
        if c == "E":
            break
        print(c, end='')
print("程序退出")
