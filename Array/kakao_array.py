import re
def solution(expression):
    answer=[]
    numbers=re.split('[\-\+\*]',expression)
    operation=re.split('\d+',expression)
    del operation[-1]
    del operation[0]
    opr=[['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+'],['*','-','+'],
        ['*','+','-']]
    for i in range(1):
        tmp_num=list(map(int,numbers))
        tmp_opr=operation
        cnt=0
        for j in range(len(tmp_opr)):
            if tmp_opr[cnt]==opr[i][0]:
                tmp_num[cnt]=operate(tmp_opr[cnt],tmp_num[cnt],tmp_num[cnt+1])
                del tmp_num[cnt+1]
                del tmp_opr[cnt]
            else:
                cnt+=1
        cnt=0
        for j in range(len(tmp_opr)):
            print(tmp_opr,cnt,opr[i])
            if tmp_opr[cnt]==opr[i][1]:
                tmp_num[cnt]=operate(tmp_opr[cnt],tmp_num[cnt],tmp_num[cnt+1])
                del tmp_num[cnt+1]
                del tmp_opr[cnt]
            else:
                cnt+=1
        cnt=0
        for j in range(len(tmp_opr)):
            if tmp_opr[cnt]==opr[i][2]:
                tmp_num[cnt]=operate(tmp_opr[cnt],tmp_num[cnt],tmp_num[cnt+1])
                del tmp_num[cnt+1]
                del tmp_opr[cnt]
            else:
                cnt+=1

        
        
        answer.append(tmp_num[0])
                
    
    return answer

def operate(a,n1,n2):
    if a=='+':
        return n1+n2
    elif a=='-':
        return n1-n2
    else:
        return n1*n2

input_data="100-200*300-500+20"
print(solution(input_data))



# 다른 정답지
#지리네
def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)



#정석 정답지
import re
from itertools import permutations

def solution(expression):
    #1
    op = [x for x in ['*','+','-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    ex = re.split(r'(\D)',expression)

    #2
    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                _ex = _ex[:tmp]+_ex[tmp+2:]
        a.append(_ex[-1])

    #3
    return max(abs(int(x)) for x in a)