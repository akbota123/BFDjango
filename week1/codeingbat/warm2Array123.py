def array123(nums):
  for n in range(len(nums)-2):
    if nums[n:n+3]==[1, 2, 3]:
      return True
  return False
