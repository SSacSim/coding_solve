import heapq
def solution(operations):
    now_buho = 1
    num_list = []
    for i in operations:
      alpha , num = i.split(" ")



      if alpha == "I":
        num_list.append( now_buho * int(num))

      else:
        if len(num_list) == 0:
          continue

        if now_buho == 1 : # 지금 양수
          if int(num) == 1 : # 최대 구하기
            num_list = [ x * -1 for x in num_list]
            now_buho = -1
        else: # 지금 음수
          if int(num) == -1:
            num_list = [ x * -1 for x in num_list]
            now_buho = 1


        heapq.heapify(num_list)
        heapq.heappop(num_list)
    if len(num_list) == 0:
      answer=[0,0]
    else:
      if now_buho == -1:
        num_list = [x * -1 for x in num_list]
      answer = [max(num_list),min(num_list)]
    return answer

# 수정
