
def merge(intervals):
    result = [[1, 6]]
    intervalsLen = len(intervals)

    result = []

    for i, parentInt in enumerate(sorted(intervals)):
        foundIntersection = False
        j = i + 1

        if parentInt == '#':
            continue

        parentStart, parentEnd = parentInt

        while j < intervalsLen:
            childInt = intervals[j]

            if childInt == '#':
                break

            childStart, childEnd = childInt
            check = False

            if childStart == parentStart or childStart == parentEnd or childEnd == parentEnd:
                check = True

            # find min of childStart & parentStart then run condition
            minStart = min(childStart, parentStart)
            print('minStart ', minStart, parentInt, childInt)

            if minStart == parentStart:
                # print('parent min of {} and {} is {}'.format(parentInt, childInt, parentInt))
                # print('expand => ', parentStart, childStart, parentEnd)

                check = parentStart <= childStart <= parentEnd

            else:
                # print('child min of {} and {} is {}'.format(parentInt, childInt, childInt))
                print('expand => ', childStart, parentStart,
                      childEnd, childStart <= parentStart <= childEnd)

                check = childStart <= parentStart <= childEnd

            # there's an intersection between these two arrays
            if check:
                foundIntersection = True
                childInt = '#'
                newInterval = [min(parentStart, childStart),
                               max(parentEnd, childEnd)]

                result.append(newInterval)

            j += 1
        if not foundIntersection:
            result.append(parentInt)

    print('intervals => ', intervals)

    return result

# # [[1, 6], [8, 10], [15, 18]]
# print('result after merge => ', merge(
#     intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))


# # [[1, 5]]
# print('result after merge => ', merge(intervals=[[1, 4], [4, 5]]))

# # [[1, 3], [5, 6], [8, 10], [15, 18]]
# print('result after merge => ', merge(
#     intervals=[[1, 3], [5, 6], [8, 10], [15, 18]]))


# [[1, 3], [8, 10], [15, 18]]
print('result after merge => ', merge(
    intervals=[[2, 2], [1, 3], [8, 10], [15, 18]]))


#             # ps >= cs and cs <= pe
#             check1 = parentStart >= childStart and parentEnd <= childStart
#             # or parentEnd <= childEnd
#             print('check1 => ',
#                   check1, interval, intervals[j])

#             # ps <= cs then pe >= cs
#             check2 = parentStart <= childStart and parentEnd >= childStart
#             # or parentEnd >= childEnd


# def merge(intervals):
#     result = [[1, 6]]
#     intervalsLen = len(intervals)

#     result = []

#     for i, interval in enumerate(intervals):
#         if interval == '#':
#             continue
#         parentStart, parentEnd = interval
#         j = i + 1
#         # print('parent => ', interval, parentStart, parentEnd)
#         foundIntersection = False

# # [2, 2], [1, 3]
#         while j < intervalsLen:
#             childStart, childEnd = intervals[j]

#             check = False

#             # if childStart == parentStart or childStart == parentEnd or childEnd == parentEnd // there's an intersection
#             if childStart == parentStart or childStart == parentEnd or childEnd == parentEnd:
#                 check = True

#             # find min of childStart & parentStart then run condition
#             minStart = min(childStart, parentStart)
#             if minStart == parentStart:
#                 # check = parentStart >= childStart and parentEnd <= childStart
#                 check = childStart <= parentStart >= childEnd

#             else:
#                 # print('v ', intervals[j], interval)
#                 check = parentStart <= childStart >= parentEnd
#                 print('v ', intervals[j], interval, parentStart <= childStart, childStart >= parentEnd)
#                 # check = parentStart <= childStart and parentStart <= childEnd
#                 # check = parentStart <= childStart and parentEnd >= childStart
#                 # [3 6] [5 9]
#                 # [2 ] [4 ]
#                 # [1 3] [2 2]

#                 # ps <= cs >= pe

#             # there's an intersection between these two arrays
#             if check:
#                 foundIntersection = True
#                 # del intervals[j]
#                 intervals[j] = '#'
#                 newInterval = [min(parentStart, childStart),
#                                max(parentEnd, childEnd)]

#                 result.append(newInterval)
#                 print('intersect => ', interval, intervals[j], newInterval)

#             # print('\tchild => ', childInterval, childStart, childEnd)

#             j += 1
#         if not foundIntersection:
#             result.append(interval)

#         # print('interval => ', interval)

#     return result

# # # [[1, 6], [8, 10], [15, 18]]
# # print('result after merge => ', merge(
# #     intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))

# # # [[1, 5]]
# # print('result after merge => ', merge(intervals=[[1, 4], [4, 5]]))

# # # [[1, 3], [5, 6], [8, 10], [15, 18]]
# # print('result after merge => ', merge(
# #     intervals=[[1, 3], [5, 6], [8, 10], [15, 18]]))


# # [[1, 3], [8, 10], [15, 18]]
# print('result after merge => ', merge(
#     intervals=[[2, 2], [1, 3], [8, 10], [15, 18]]))
