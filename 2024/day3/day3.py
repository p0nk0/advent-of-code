f = open("input.txt","r")

total = 0 
enabled = True

for line in f.readlines():
    for i in range(len(line)):
        if enabled and line[i:i+4] == "mul(":
            nums = line[i+4:i+12].strip(")").split(",")
            if len(nums) >= 2:
                X = nums[0]
                Y = "".join(filter(lambda x: x.isdigit(), nums[1]))
                if line[i+5+len(X)+len(Y)] == ")":
                    total += int(X)*int(Y)
        elif line[i:i+4] == "do()":
            enabled = True
        elif line[i:i+7] == "don't()":
            enabled = False

print(total)

