f = open("input.txt","r")

total = 0

for line in f.readlines():
    A,B = line.strip().split(",")
    A = A.split("-")
    A[0], A[1] = int(A[0]),int(A[1])
    B = B.split("-")
    B[0], B[1] = int(B[0]),int(B[1])
    # print(A,B)

    # if (A[0] <= B[0] and A[1] >= B[1]) or (B[0] <= A[0] and B[1] >= A[1]):
    if (A[0] <= B[0] and A[1] >= B[0]) or (B[0] <= A[0] and B[1] >= A[0]):
        print(A,B)
        total += 1

print(total)