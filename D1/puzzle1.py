
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

for i in range(len(leftList)):
  left = leftList[i]
  right = rightList[i]
  result.append(abs(left - right))
  
print(sum(result))
