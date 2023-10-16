def divisor(n):
# all numbers that divide an integer, n
    numlist = []
    for i in range(n, 0, -1):
        print(i)
        if n % i != 0:
            numlist.append(i)

x = divisor(int(10))
print(x)