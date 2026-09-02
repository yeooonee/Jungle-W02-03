

# 첫번째는 임의로 놓음
# 각 행, 열에 퀸을 1개만 배치

pos = [0] * 8
cnt = 0

def put() -> None:
    for i in range(8):
        print(f'{pos[i]:2}', end='')  
    print()

def set(i: int) -> None:
    
    global cnt  # 이거 없이는 지역변수 취급함
    for j in range(8):
        flag = True
        # 같은 행 제거 
        # 확정된 값 지나치기 
        if j in pos[0:i]:   # 점유된 행들일 경우에
            continue
        
        # 이미 확정된 행과 비교
        # i 만큼 돌면서
        for k in range(i):
            i2,j2 = k, pos[k]
            # 확정된 행의 값들과 i,j 와 비교하여 차이의 절대값이 같으면 대각선
            di = abs(i - i2)
            dj = abs(j - j2)
            if di == dj :
                flag = False
        
        if flag == False:
            continue
            
        pos[i] = j
        if i == 7:
            cnt += 1   
            put()
        else:
            set(i + 1)
            
set(0)
print(cnt)
