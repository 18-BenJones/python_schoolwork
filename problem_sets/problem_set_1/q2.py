def final_temp_calc(airtemp, windspeed):
    # Uses deg. celcius for temp and mph for wind, corrected for in the input stage
    final_temp = 0
    final_temp = airtemp - (windspeed * 0.7)
    final_temp = round(final_temp, 0)
    return(final_temp)

tmp = ""
airtemp = 0
windspeed = 0
print("Are you using metric (M) or imperial (I) mesurments?")
tmp = input()
if tmp.capitalize() == "M":
    print("Please enter the air temprature in degrees celcius:")
    tmp = input()
    airtemp = float(tmp)
    print("Please enter the air speed in meters per second (M/S): ")
    tmp = input()
    windspeed = float(tmp) * 2.237
    print("The wind-chill temprature is: ", final_temp_calc(airtemp, windspeed), " Degrees")
elif tmp.capitalize() == "I":
    print("Now Please enter the air temprature in degrees fahrenheight:")
    tmp = input()
    airtemp = (float(tmp) -32) * 5/9
    print("Please Enter the windspeed in miles per hour (MPH):")
    tmp = input()
    windspeed = float(tmp)
    print("The wind-chill temprature is: ", (final_temp_calc(airtemp, windspeed)*9/5)+32, " Degrees")
else:
    print("You have entered an invalid input!\nPlease Restart the program and try again!")

