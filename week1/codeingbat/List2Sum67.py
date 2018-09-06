def sum67(nums):
  for n in range(0, len(nums)):
    if nums[n]==6:
      nums[n]=0
      for m in range(n+1, len(nums)):
        k=nums[m]
        nums[m]=0
        if k==7:
          n=m+1
          break
  return sum(nums)
