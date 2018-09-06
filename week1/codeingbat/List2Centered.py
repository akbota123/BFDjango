def centered_average(nums):
  sum=0
  for n in nums:
    sum+=n
  return (sum-min(nums)-max(nums))/(len(nums)-2)
