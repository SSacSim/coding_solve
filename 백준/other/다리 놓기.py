T = int(input())

for _ in range(T):
    left , right = map(int,input().split(" "))
    if left < right:
      temp = left
      left = right
      right = temp

    mamo = [[1 if i == 0 else 0 for i in range(right + 1)] for j in range(left + 1)]
    for now_left in range(1, left + 1 ):
      for now_right in range(1, now_left + 1 ):
        if now_right >= right+ 1:
          break
        mamo[now_left][now_right] = mamo[now_left -1][now_right] + mamo[now_left -1][now_right - 1]

    print(mamo[left][right])
