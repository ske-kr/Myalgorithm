import sys
input=sys.stdin.readline


def onetwothree():
    n=int(input())
    number=[]
    num=[1,2,4]
    for i in range(7):
        num.append(sum(num[i:i+3]))

    for i in range(n):
        number.append(int(input()))
        print(num[number[i]-1])

onetwothree()