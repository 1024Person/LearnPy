l1 = [1,2,3,4,5,6,7,8,9]
l2 = [1,2,5]

s1 = set(l1)
s2 = set(l2)

# 对称差集
result = s1 ^ s2
print(result)

print(s2.difference(s1))