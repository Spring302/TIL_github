import math

# n = int(input())
for n in range(1,1000):
    print(n, end=':')
    ten = int(math.log10(n))+1
    if ten == 1:
        print(n)
    else:
        # 최소 생성자 예상 범위
        if n-9*ten > 0:
            m = n-9*ten
        else:
            m = 0
        for i in range(m, n+1):
            if i==n:
                print(0)
                break
            else:
                cons = i+(sum(map(int,str(i))))
                if cons == n:
                    print(i)
                    break



