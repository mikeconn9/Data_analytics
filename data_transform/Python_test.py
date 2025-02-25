#input:
'''
4
Sona
-25.001
Mona
-25.0001
Mini
-25.000
Rita
-25.0
'''

if __name__ == '__main__':
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_score = list([name, score])
        score_list.append(student_score)
# sort the list based on score(asc) and name(alpha)
    score_list.sort(key=lambda x: (x[1], x[0]), reverse=False)
# Move the index to the last min in the list
    first_min_idx = 0
    while score_list[first_min_idx][1] == score_list[0][1]:
        first_min_idx = first_min_idx + 1
        if first_min_idx == len(score_list):
            break
# Determine what are the 'static' values and capture them
    first_min_idx = first_min_idx - 1
    first_min_score = score_list[first_min_idx][1]
# Scan the remaining lists, print all the second mins
    base = first_min_idx
    idx = first_min_idx + 1
    while (score_list[idx][1] > first_min_score):
        if (idx == first_min_idx + 1) or (score_list[idx][1] == score_list[base][1]):
            print(score_list[idx][0])
            base = idx
        idx = idx + 1
        if idx == len(score_list):
            break                
      