import math
C = 50
H = 30
D = input("Comma serprated variable D ")
k = D.split(',')
result = []
for i in k:
    ans = round(math.sqrt(2*C*int(i)/H))
    result.append(ans)
print(result)