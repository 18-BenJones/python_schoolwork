import math
tmp = ""
lat = [] 
long = [] 
RAD = 6371000 #radius in metres
tmp2 = 0.0 # used to store the input for the arcsine to make code look clearer
dist = 0.0

print("Use negative for south/west")

for i in range(0,2):
    print("Please enter the latitude for point ", i+1)
    tmp = input()
    try:
        lat.append(float(tmp))
    except:
        print("All inputs to this programs must be numeric! Last Warning!")
        print("Please enter the latitude for point ", i+1)
        tmp = input()
        lat.append(float(tmp))

for i in range(0,2):
    print("Please enter the longtidue for point ", i+1)
    tmp = input()
    try:
        long.append(float(tmp))
    except:
        print("All inputs to this programs must be numeric! Last Warning!")
        print("Please enter the longditude for point ", i+1)
        tmp = input()
        long.append(float(tmp))

# haversine formula solving for distance; https://en.wikipedia.org/wiki/Haversine_formula
# math.asin() is the arcsine trig function
tmp2 = (math.sin((lat[1]-lat[0])/2) ** 2) + (math.cos(lat[0]) * math.cos(lat[1])* (math.sin((long[1]-long[0])/2) ** 2))
tmp2 = math.sqrt(tmp2)
dist = 2 * RAD * (math.asin(tmp2))
print("The distance between the 2 points is: \n", dist//1000, " KM")

