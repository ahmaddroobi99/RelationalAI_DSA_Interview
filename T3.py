
# def solution(A):
#     ha = {}
#     for i in range(len(A)):
#         if A[i] in ha.keys():
#             ha[A[i]] += 1
#         else:
#             ha[A[i]] = 1

#     count = 0
#     for i in ha:
#         if (ha[i] > 1):
#             count += ha[i] - 1
#     return count

# the above solution didnt pass test 3 so i tried the below algorithm after do it pen and paper
# A= [6,2,3,5,6,3]
#
# print(solution (A))


def solution(A):
  #   NlogN
  A.sort()

  result = 0
  idx = 1

  for i in A:

    diff = i - idx

    if diff < 0:
      result -= diff

    elif diff > 0:
      result += diff

    idx += 1
  return result

A= [6,2,3,5,6,3]
# A=[2,1,4,4]
# A=[1,2,1]
# A=[1,1,1,1,1,2,3,4,5]
# A=[3,3,3,3]
# A=[1,2,3,4]
A=[4,3,2,1]

print(solution (A))