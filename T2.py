

N=5
K=8


# def solution(N, K):
#     count=0
#     sum=0
#     s=[ i for i in range(N)]
#     print(s)
#     if K in s:
#         return 1
#     for i in range(N):
#         for j in range(i+1,)
#


print(solution(N,K))


def solution( N,  K) :
    ans = 0
    while K  :
        if N == 0: return -1
        if N >= K :
            ans+=1
            break;

        else :
            ans+=1
            K = K-N
            N = N-1


    return ans

