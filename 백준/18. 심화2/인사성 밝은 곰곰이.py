import sys
input = sys.stdin.readline
N = int(input().strip())

count = 0
for _ in range(N):
  input_text = input().strip()

  if input_text == 'ENTER':
    name_dict = dict()
  else:
    if input_text not in name_dict:
      name_dict[input_text] = 1
      count += 1
print(count)
