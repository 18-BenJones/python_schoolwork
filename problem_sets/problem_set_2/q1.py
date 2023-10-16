def index(letter):
    id = 0
    cols = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for i in range(0, len(cols)-1):
        if letter.capitalize() ==  cols[i]:
            id = i
    return(id)

inp = input("Please enter the position in the form column row, eg 'a1'\n")

if (index(inp[0]) % 2 == 1) and (int(inp[1]) % 2 == 1):
    print("The Square is Black")
elif(index(inp[0]) % 2 == 0) and (int(inp[1]) % 2 == 0):
    print("The Square is black")
else:
    print("The square is white")