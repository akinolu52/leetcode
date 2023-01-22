
def sortArrayByParityII(nums):
    result = []
    checkingEven = True

    for idx, num in enumerate(nums):
        print('-> ',idx, num, checkingEven, nums, result)

        if num == '#':
            idx -= 1
            continue
        if checkingEven:
            if num % 2 == 0:
                result.append(num)
                nums[idx] = '#'
            else:
                count = -1
                # print(idx, len(nums))
                while count < len(nums) - 1:
                    count += 1
                    curr = nums[count]

                    if curr == '#':
                        continue
                    if curr % 2 == 0:
                        result.append(curr)
                        nums[count] = '#'
                        break

            checkingEven = False
        else:
            if num % 2 != 0:
                result.append(num)
                nums[idx] = '#'
            else:
                count = -1
                while count <= len(nums) - 1:
                    count += 1
                    curr = nums[count]

                    if curr == '#':
                        continue
                    if curr % 2 != 0:
                        result.append(curr)
                        nums[count] = '#'
                        break

            checkingEven = True

        print('=> ',idx, num, checkingEven, nums, result)

    return result


nums = [4, 2, 5, 7]
print(sortArrayByParityII(nums))
