import math
tmp = ""
p = [[],[]] #point 1 lat and long, point 2 lat and long 
Rad = 6371000
a = 0.0
c = 0.0

print("Use negative for south/west")

for i in range(0,2):
    print("Please enter the latitude for point ", i+1)
    tmp = input()
    try:
        p[i].append(float(tmp))
    except:
        print("All inputs to this programs must be numeric! Last Warning!")
        print("Please enter the latitude for point ", i+1)
        tmp = input()
        p[i].append(float(tmp))

for i in range(0,2):
    print("Please enter the longtidue for point ", i+1)
    tmp = input()
    try:
        p[i].append(float(tmp))
    except:
        print("All inputs to this programs must be numeric! Last Warning!")
        print("Please enter the longditude for point ", i+1)
        tmp = input()
        p[i].append(float(tmp))


a = ((math.sin()) ** 2)
# use harversine