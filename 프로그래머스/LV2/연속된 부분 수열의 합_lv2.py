def solution(sequence, k):
    total_sum = 0
    start = 0 # 여기서부터
    end = -1 # 여기까지 더한다
    answer = [0,9999999]
    
    while True: # end가 종료됨
      if  end >= len(sequence):
        break

      if total_sum < k:
        end += 1
        if end < len(sequence):
            total_sum += sequence[end]

      elif total_sum > k:
        total_sum -= sequence[start]
        start += 1

      else:
        if answer[1] - answer[0] > end - start:
          answer = [start ,end]
        end += 1
        if end < len(sequence):
          total_sum += sequence[end]
        
    while True:
      if start >= len(sequence) - 1:
        break
      total_sum -= sequence[start]
      start +=1

      if total_sum == k:
        if answer[1] - answer[0] > end - start:
          answer = [start ,end]

    return answer