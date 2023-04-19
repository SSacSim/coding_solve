import sys
input = sys.stdin.readline

N,M = map(int,input().strip().split(" "))
site_dict = dict()

for _ in range(N):
  site_, password_ = input().strip().split(" ")
  site_dict[site_] = password_
    
for _ in range(M):
  input_site = input().strip()
  print(site_dict[input_site])
