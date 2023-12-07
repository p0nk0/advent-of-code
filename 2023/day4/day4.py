f = open("input.txt","r");

total = 0
counts = [1 for _ in range(211)]

for line in f.readlines():
    cur_card = int(line.split(":")[0].split(" ")[-1])
    cur_count = counts[cur_card-1]
    line = line[8:].strip().split("|")
    winning_nums = list(filter(lambda x: x != "", line[0].split(" ")))
    all_nums = list(filter(lambda x: x != "", line[1].split(" ")))
    all_nums.sort()

    card_total = 0
    for n in winning_nums:
        if n in all_nums:
            card_total += 1
    
    for i in range(cur_card, cur_card + card_total):
        counts[i] += cur_count

    print(f"card {cur_card}: {cur_count} copies, {card_total} winning numbers")
    print(counts)


print(sum(counts))
    