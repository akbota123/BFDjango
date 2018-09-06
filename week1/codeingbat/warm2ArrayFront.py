def array_front9(nums):
    for nine in nums[:4]:
        if nine == 9:
            return True
    return False