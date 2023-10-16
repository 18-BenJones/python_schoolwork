arr = []
tmp = ""
for i in range(0,4):
    print("Please enter digit ", i+1, ":")
    tmp = input()
    try:
        tmp = (int(tmp))
    except:
        print("All inputs to this programs must be numeric!")
        print("Please enter digit ", i+1, ":")
        tmp = input()
    else:
        arr.append(int(tmp))
tmp = 0
for i in range(0, len(arr)):
    if i == len(arr) - 1:
        print(arr[i], end=" = ")
    else:
        print(arr[i], end=" + ")
    tmp += arr[i]
print(tmp)