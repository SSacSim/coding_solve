n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
word_index = 0
j = 0
user_words = []

answer_turn =0
answer_user_id = 0
while True:
    j += 1  # 돌아간 횟수
    
    if word_index >= len(words):
        break
    for i in range(1, n+ 1): #  사람 id
        if len(user_words) == 0:
            user_words.append(words[word_index])
            word_index += 1
        elif words[word_index] not in user_words:
            print(words[word_index][0])
            print(user_words)
            print("========================")
            if words[word_index][0] == user_words[-1][-1]:
                user_words.append(words[word_index])
                word_index += 1
            else:
                answer_user_id = i
                break

        else:
            answer_user_id = i
            break
        print('===============================')
        
    if answer_user_id != 0:
        answer_turn = j
        break
    
print(answer_user_id, answer_turn)
        