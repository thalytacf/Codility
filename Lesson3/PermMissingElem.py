'''
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
'''
#PAINLESS

def solution(A):
    A.sort()
    print(A)
    if A == []:
        return 1

    if A[0] != 1:
        return 1

    if A == [1]:
        return  2
    cont = 1

    for i in A:
        if A[i]+1 != A[i+1]:
            return  A[i]+1

    # while cont in A:
    #     cont+=1
    # return cont

    #for i in range(len(A)):

print(solution(2,3,5,1))
