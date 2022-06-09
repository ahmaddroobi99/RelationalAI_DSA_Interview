def solution(S):
    ha ={}
    count=0
    for i in S:
        if i in ha :
            ha[i]+=1
        else :
            ha[i]=1

    for i in ha.values():
        if i %2 ==1 :
            count+=1
    return count

    return ha
print(solution("axxaxa"))


