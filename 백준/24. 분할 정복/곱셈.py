# 분할 정복을 사용하여 해결
# A**B  = A**B//2 + A**B//2 로 나눌 수 있음
# 또한, (a*b) % c = (a % c + b % c) % c 

A,B,C = map(int,input().split(" "))
def test(a,b):
  if b == 1:
    return a % C
  
  temp = test(a,b//2)

  if b % 2 == 0:
    return temp * temp % C # 모듈러 연산 성질
  else:
    return temp * temp * a % C
print(test(A,B))
