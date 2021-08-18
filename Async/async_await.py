import time
import asyncio


## https://www.daleseo.com/python-asyncio/
## 동기 비동기의 '기본' 작동원리에 대한 설명이 잘 나와있다
## 아래는 간단한 실습 코드이다.
## 작동 결과는 이해하지만 coroutine 객체가 return 된다는 부분을 좀 더 파악해보도록 하자.

def find_users_sync(n):
    for i in range(1, n + 1):
        print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
        time.sleep(1)
    print(f'> 총 {n} 명 사용자 동기 조회 완료!')

def process_sync():
    start = time.time()
    find_users_sync(3)
    find_users_sync(2)
    find_users_sync(1)
    end = time.time()
    print(f'>>> 동기 처리 총 소요 시간: {end - start}')

async def find_users_async(n):
    for i in range(1, n + 1):
        print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
        await asyncio.sleep(1)
    print(f'> 총 {n} 명 사용자 비동기 조회 완료!')

async def process_async():
    start = time.time()
    await asyncio.wait([
        find_users_async(3),
        find_users_async(2),
        find_users_async(1),
    ])
    end = time.time()
    print(f'>>> 비동기 처리 총 소요 시간: {end - start}')