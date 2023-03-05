n = 8
m = 4
section = 	[2, 3, 6]

now_section = 1
count = 0

for i in section:
    if now_section < i:  # 페인팅이 필요한 곳보다 현재 있는 곳보다 뒤에 있을때
        now_section = i
        
    if i < now_section: # 페인팅이 필요한 곳이지만, 이미 페인팅이 됐을 경우 
        continue
    
    if now_section > n - m: # 끝부분의 페인팅이 필요한 경우
        count += 1
        break
    else:
        count += 1
        now_section += m
print(count)
    