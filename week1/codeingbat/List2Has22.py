def has22(nums):
  for n in range(0, len(nums)-1):
    if nums[n:n+2]==[2, 2]:
      return True
  return False
