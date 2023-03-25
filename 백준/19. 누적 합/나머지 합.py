from collections import Counter
def combination_count(left):
  answer = (left * (left -1)) / 2
  return answer

N,M = map(int,input().split(" ")) # N : input 갯수 , M : 나누는 값
num_list = list(map(int,input().split(" ")))

sum_list = []
temp = 0
answer = 0
for i in num_list:
  temp += i
  if temp % M == 0:
     answer +=1
  sum_list.append(temp % M) 

count_list = Counter(sum_list)

for i in count_list:
  if count_list[i] >=2:
      answer += int(combination_count(count_list[i]))
print(answer)