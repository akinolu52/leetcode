
def removeElement(nums, val: int):
    # nums = ''.join(str(e) for e in sorted(nums))
    # print('nums = {} '.format(nums))

    # if

    # nums = sorted(nums.replace(str(val), ''))

    # print('nums = {} '.format(nums))

    # nums = [int(i) for i in nums]
    # # nums = list(''.join(int(e) for e in sorted(nums)))
    # print('nums = {} '.format(nums))
    # nums = sorted(nums)
    # print('nums = {} '.format(nums))

    pop_index = []

    for index, num in enumerate(nums):
        if num == val:
            print('index ', index)
            pop_index.append(index)

    pop_index.reverse()
    print('pop_index ', pop_index)

    for index in pop_index:
        nums.pop(index)
        print('nums ', nums)
        

    return nums

    # return len(sorted(list(''.join(str(e) for e in sorted(nums)).replace(str(val), ''))))


print(removeElement([3, 2, 2, 3], 3))
# print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
# print(removeElement())
# print(removeElement())
