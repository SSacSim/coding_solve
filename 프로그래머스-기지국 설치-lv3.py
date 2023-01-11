n = 16
stations = [9]
w = 2

import numpy as np

end_point = 0

count = 0
for i in stations: # stations은 오름차순으로 정렬되어있음
    print("i",i)
    print("be_fore_end_point",end_point)

    if i - w <=0:
        end_point = i + w
        continue
    
    # i - end_point > 설치되어 있지 않은 구간 lenth
    print("=============")
    print((i - w - end_point - 1))
    print(w*2+1)
    print("=============")
    count += int(np.ceil((i - w - end_point - 1) / (w *2 +1)))
    
    end_point = i + w # 이전에 여기까지 설치됨 update
    print("end_point",end_point)
    print("count",count)
if end_point < n:
    count += int(np.ceil((n - end_point) / (w *2 +1)))
print(count)