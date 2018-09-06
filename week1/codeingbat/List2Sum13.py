def sum13(nums):
  if len(nums)==0:
    return 0
  for n in range(0, len(nums)):
    if nums[n]==13:
      nums[n]=0
      if n+1<len(nums):
        nums[n+1]=0
  return sum(nums)
