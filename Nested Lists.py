N=[]
for i in range(int(input())):
    name = input()
    score = float(input())
    N.append([name,score])
second_highest = sorted(set([score for name, score in N]))[1]
print('\n'.join(sorted([name for name, score in N if score == second_highest])))
