A_up, A_down = map(int,input().split(" "))
B_up, B_down = map(int,input().split(" "))

# 최대 공약수 
def gcd(a,b):
  while True:
    if b == 0 :
      break
    temp = a % b
    a = b
    b = temp
  return a
down = int(A_down * B_down / gcd(A_down , B_down))
up = B_up * down // B_down + A_up * down // A_down
temp = gcd(up,down)
print(up // temp , down // temp)
