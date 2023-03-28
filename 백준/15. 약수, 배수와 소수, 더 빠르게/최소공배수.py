left, right = map(int,input().split(" "))
temp1 = max(left,right)
temp2 = min(left,right)
def gcd (bigger , smaller):
    while True:
        temp = bigger % smaller
        if temp == 0:
            return smaller
        bigger = smaller
        smaller = temp
print(int(left * right / gcd(temp1,temp2)))