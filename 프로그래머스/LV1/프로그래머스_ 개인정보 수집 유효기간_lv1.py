def solution(today, terms, privacies):
    terms_dict = dict()

    for i in terms:
      temp = i.split(" ")
      terms_dict[temp[0]] = int(temp[1])
        

    to_y = int(today.split(".")[0] + today.split(".")[1] + today.split(".")[2])

    answer = []
    for index,i in enumerate(privacies):
      before = i.split(" ")[0]
      before_list = before.split(".")

      year = int(before_list[0])
      month = int(before_list[1])
      day = int(before_list[2])

      temp = i.split(" ")[1]
      
      if temp not in terms_dict:
            break
      month += terms_dict[temp]

      if month >= 13:
        year += month // 12
        if month % 12 == 0:
            month = 12
            year -=1
        else:
            month = month % 12

      day -= 1
      if day == 0:
        day = 28
        month -= 1
      if month == 0:
        month = 12
        year -= 1

      year = str(year)
      if month < 10:
        month = "0" + str(month)
      else:
        month =str(month)

      if day < 10:
        day = "0" + str(day)
      else:
        day = str(day)

      total = int(year + month + day)

      if to_y > total:
        answer.append(index+1)
    return answer
