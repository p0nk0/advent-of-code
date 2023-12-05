f = open("input.txt","r")

total = 0

for line in f.readlines():
    rounds = line.split(":")[1].split(";")
    red, blue, green = float("-inf"), float("-inf"), float("-inf")
    for r in rounds:
        colors = r.split(",")
        for c in colors:
            c = c.strip().split(" ")

            n = int(c[0])
            color = c[1]
            
            if color == "red":
                red = max(n,red)
            elif color == "green":
                green = max(n,green)
            elif color == "blue":
                blue = max(n,blue)
            
    total += red*green*blue

print(total)
