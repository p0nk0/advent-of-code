f = open("input.txt","r")

total = 0

for line in f.readlines():

    nums = line
    nums = nums.replace("one","o1e")
    nums = nums.replace("two","t2o")
    nums = nums.replace("three","t3e")
    nums = nums.replace("four","f4r")
    nums = nums.replace("five","f5e")
    nums = nums.replace("six","s6x")
    nums = nums.replace("seven","s7n")
    nums = nums.replace("eight","e8t")
    nums = nums.replace("nine","n9e")

    nums = "".join((filter(str.isdigit,nums)))

    print(line, nums)

    total += 10*int(nums[0])
    total += int(nums[-1])

print(total)

