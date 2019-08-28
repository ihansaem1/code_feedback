def solution(L, x):
    if x < L[0] :
        L.insert(0, x)
    if x > L[-1] :
        L.append(x)
    for i in range(len(L)) :
        if L[i] < x < L[i+1] :
            L.insert(i+1, x)
            break
    answer = L
    return answer
