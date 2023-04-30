text1 = input()
text2 = input()
matrix = [ [ 0 for _ in range(len(text1))] for _ in range(len(text2))]
for row_index, i in enumerate(text2):
  for col_index , j in enumerate(text1):
    if i == j :
      matrix[row_index][col_index] = 1

max_count = 0
for row_index in range(1,len(text2)):
  for col_index in range(1,len(text1)):
    if matrix[row_index][col_index] != 0 and matrix[row_index - 1][col_index - 1] != 0:
      matrix[row_index][col_index] += matrix[row_index - 1][col_index - 1]
      if max_count < matrix[row_index][col_index]:
        max_count = matrix[row_index][col_index]
print(max_count)
