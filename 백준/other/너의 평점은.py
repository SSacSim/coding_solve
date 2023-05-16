jumsu = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0,
}

answer = 0
sum_hakjum = 0
for _ in range(20):
    name, hakjum, grade = input().split(" ")
    
    if grade != "P":
        answer += float(hakjum) * jumsu[grade]
        sum_hakjum += float(hakjum)
        
print(answer / sum_hakjum)