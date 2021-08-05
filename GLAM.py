def countPairs(numbers, k):
    # Write your code here
    ## delete all duplicated numbers
    numbers=list(set(numbers))

    result=0
    numbers.sort()
    n=len(numbers)
    # why not working;
    # for a in range(n-1):
    #     for b in range(a+1,n):
    #         if numbers[b]-numbers[a]==k:
    #             result+=1
    #             break
    #         if numbers[b]-numbers[a]>k:
    #             break
    
    start=0
    end=0
    #searching sorted list by index... 
    while end<n:
        if numbers[end]-numbers[start]==k:
            result+=1
            start+=1
            end+=1
        elif numbers[end]-numbers[start]>k:
            start+=1
        else:
            end+=1
    

    
    return result


## 코테에러,, 왜인지 이유찾기


import requests,json
#
# Complete the 'getUsernames' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER threshold as parameter.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/article_users?page=<pageNumber>
#

def getUsernames(threshold):
    # Write your code here
    result=[]
    testseturl="https://jsonmock.hackerrank.com/api/article_users?page={}"
    # get datas from the page(total numbers of page) 
    page_data=json.loads(requests.get(testseturl).content.decode())
    total_page=page_data['total_pages']
    total_users=page_data['total']
    per_page=page_data['per_page']
    
    # search 
    for i in range(1,total_page+1):
        page_data=json.loads(requests.get(testseturl.format(i)).content.decode())
        for i in range(min(per_page,total_users)):
            if page_data["data"][i]['submission_count']>threshold:
                result.append(page_data["data"][i]['username'])
        total_users-=per_page
    
    
    return result