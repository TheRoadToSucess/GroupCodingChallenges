ans = []
nums = [8, 13, 11, 90, -5, 4]

numsList = sorted(nums)
j = 1

for x in numsList:
    if x % 2 == 0:
        ans.append(x)


for i in range(len(numsList) - 1, -1, -1):
    if numsList[i] % 2 != 0:
        ans.insert(j, numsList[i])
        j +=2

print(ans)