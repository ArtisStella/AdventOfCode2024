
leftList = []
rightList = []
result = []

with open("D1/input1.txt") as inFile:  
  for line in inFile.readlines():
    nums = line.split("   ")
    leftList.append(int(nums[0]))
    rightList.append(int(nums[1]))

leftList = sorted(leftList)
rightList = sorted(rightList)

for num in leftList:
  multiplier = rightList.count(num)
  result.append(num * multiplier)
  
print(sum(result))
