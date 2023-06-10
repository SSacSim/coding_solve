import sys
input = sys.stdin.readline
L , C  = map(int,input().strip().split(" "))
alpha_list = list(input().strip().split(" "))
alpha_list.sort()
mo = ['a', 'e', 'i', 'o', 'u']
def recur(start , alpha_):
  # print("====")
  # print("alpha_",alpha_)
  if len(alpha_) == L :
    aeiou = 0
    others = 0
    for k in alpha_:
      if k in mo:
        aeiou += 1
      else:
        others += 1
      
      if aeiou >= 1 and others >=2 :
        print("".join(alpha_))
        break
    return
  
  temp_alpha_ = alpha_.copy()
  for i in range(start , len(alpha_list)):
    recur(i + 1 , temp_alpha_ + [alpha_list[i]])
    # print("return")
recur(0,[])
