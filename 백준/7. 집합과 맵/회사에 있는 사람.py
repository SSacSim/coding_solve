import sys
input = sys.stdin.readline
N = int(input().strip())
log_ = dict()
for _ in range(N):
  name, action = input().strip().split(" ")
  
  if action == "enter":
    log_[name] = 1
  else:
    log_[name] = 0
enter = []
for i in log_.items():
  if i[1] == 1:
    enter.append(i[0])
enter.sort(reverse = True)

for i in enter:
  print(i)
