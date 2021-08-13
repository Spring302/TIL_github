# 문제풀이 유용한 함수들
`round(1.2345, 2) # 1.23`

`'0 100'.split() # ['0', '100']`

```
freezing_point, boiling_point = '0 100'.split()

print(freezing_point,boiling_point)
```

```
m = 2

for n in range(1, 10):
    print(f'{m} * {n} = {m*n:2d}')
```

# 이게 뭐람다(lambda)?

```
def hap(x,y):
    return x+y
hap(10,20)
```
```
(lambda x,y:x+y)(10,20)
```