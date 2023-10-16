def end_of_month(initial):
    months = { "1": 31, "2":28, "3":31, "4":30, "5":31, "6":30, "7": 31, "8":31, "9":30, "10":31, "11":30, "12":31}
    if months[str(initial[1])] == initial[2]:
        return(True)
    else:
        return(False)

initial = []
succesion =  []
initial.append(int(input("Please enter the Year:\n")))
initial.append(int(input("Please enter the Month:\n")))
initial.append(int(input("Please enter the Day:\n")))

for item in initial:
    succesion.append(item)

if  (initial[0] % 4 == 0) and (initial[1] == 2) and (initial[2] == 28): # Leap year
    succesion[2] = 29
elif (initial[1] == 12) and (initial[2] == 31): # New year
    succesion[0] = initial[0] + 1
    succesion[1] = 1
    succesion[2] = 1
elif end_of_month(initial): # end of the month
    succesion[1] = succesion[1] + 1
    succesion[2] = 1
else: # next day of month
    initial[2] = initial[2] + 1


print("The date is:\n", succesion[0], "-", succesion[1], "-", succesion[2], "\n", end="")