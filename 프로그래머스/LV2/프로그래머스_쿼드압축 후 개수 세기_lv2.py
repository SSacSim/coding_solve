arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
arr = [[1,0,1,1],[0,0,1,1],[1,1,1,1],[1,1,1,1]]

# 전체 1의 갯수만 셀거임
one_count = 0
zero_count = 0
def zip_(start_x, start_y, end_x,end_y):
  global one_count, zero_count
  print("==============================")
  if start_x == end_x and start_y == end_y:
    if arr[start_x][start_y] == 1:
      one_count += 1
    else:
      zero_count += 1
    print("arr return",[arr[start_x][start_y] , 1 ])
    return [arr[start_x][start_y] , 1 ] # 값, 단일값 여부
  
  arr_len = (end_x - start_x + 1) // 2
  # 4등분 합니다.
  print("zip_1 들어감")
  zip_1 =  zip_(start_x,start_y, start_x + arr_len - 1 , start_y + arr_len - 1)# 좌상
  print("zip_1 나옴")
  print("zip_2 들어감")
  zip_2 =  zip_(start_x, start_y + arr_len ,  end_x - arr_len , end_y)# 우상
  print("zip_2 나옴")
  print("zip_3 들어감")
  zip_3 =  zip_(start_x + arr_len, start_y + arr_len , end_x, end_y)# 우하
  print("zip_3 나옴")
  print("zip_4 들어감")
  zip_4 =  zip_(start_x + arr_len , start_y ,  end_x, end_y - arr_len)# 좌하
  print("zip_4 나옴")
  
  
  total_zip = zip_1[0] + zip_2[0] + zip_3[0] + zip_4[0]
  print("total_zip",total_zip)
  print("단일값 여부 " , zip_1[1] == zip_2[1] == zip_3[1] == zip_4[1] == 1)
  if zip_1[1] == zip_2[1] == zip_3[1] == zip_4[1] == 1: # 단일값으로 구성되어있냐?
    if zip_1[0] == 1 and zip_2[0] == 1 and zip_3[0] == 1 and zip_4[0] == 1:
      one_count -=3
      print("return [1,1]")
      return [1 , 1]
    elif zip_1[0] == 1 and zip_2[0] == 1 and zip_3[0] == 1 and zip_4[0] == 0:
      print("return [0,1]")
      zero_count -= 3
      return [0 , 1]
    else:
      return [total_zip , 0]
  else:
    return [total_zip , 0]

zip_(0,0,len(arr)-1,len(arr)-1)
print([zero_count, one_count])
