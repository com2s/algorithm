while True:
    nums = list(map(int, input().split()))

    if not nums[0]:
        break

    tree = 1
    for i in range(1, len(nums)):
        if i%2 == 0:
            tree -= nums[i]

        else:
            tree *= nums[i]

    print(tree)   
