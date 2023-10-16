inp = ""
height = 0
v = 0
print("Please enter the height of the object when it is dropped in Meters:")
tmp = input()
try:
    height = float(tmp)
except:
    print("All inputs to this programs must be numeric! Last Warning!")
    print("Please enter the height of the object when it is dropped in Meters:")
    tmp = input()
    height = float(tmp)
else:
    height = float(tmp)

v = 9.8 * height
print("The speed of the object the instant before it hits the ground is ", v, " Meters per second")