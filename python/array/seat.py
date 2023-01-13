def maxDistToClosest(seats) -> int:
    import math

    longestZeroCount = -1
    longestZeroPosition = {
        'start': None,
        'end': None
    }

    maxDistance = 0

    for index, seat in enumerate(seats):
        nextIndex = index + 1
        if seat == 0:
            zeroCount = 1
            zeroPosition = {
                'start': index,
                'end': index
            }
            while nextIndex < len(seats) and seats[nextIndex] == 0:
                zeroCount += 1
                zeroPosition['end'] = nextIndex
                nextIndex += 1

            if zeroCount > longestZeroCount:
                # print('found one zero', index, zeroCount, zeroPosition)
                longestZeroCount = zeroCount
                longestZeroPosition = zeroPosition
    
    start, end = longestZeroPosition.get('start'), longestZeroPosition.get('end')
    seatPosition = 0;

    if end == len(seats) - 1:
        seat = end

    if start == end and end != None:
        seat = end + 1

    if start != None and end != None:
        mid = start + end
        seat = math.ceil(mid / 2)

    # calculate the max distance
    # maxDistance
    


print('result => ', maxDistToClosest(seats=[1, 0, 0, 0, 1, 0, 1]))
print('result => ', maxDistToClosest(seats=[1, 0, 0, 0]))
print('result => ', maxDistToClosest(seats=[0, 1]))
print('result => ', maxDistToClosest(seats=[0, 0, 1]))
