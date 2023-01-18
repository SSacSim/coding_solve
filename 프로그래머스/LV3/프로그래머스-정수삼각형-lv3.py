triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
tri_list = []
for i_idx,i in enumerate(triangle):
  if len(tri_list)  == 0: 
    tri_list.append(i)
    continue

  temp_j = []
  for  j_idx , j in enumerate(i):
    if j_idx == 0 : 
      temp_j.append(j + tri_list[i_idx-1][0])
    elif j_idx == len(i)-1 : # 마지막 index
      temp_j.append(j + tri_list[i_idx-1][-1])
    else:
      temp_j.append(j + max(tri_list[i_idx-1][j_idx] , tri_list[i_idx-1][j_idx-1] ))

  tri_list.append(temp_j)
print(max(tri_list[-1]))
