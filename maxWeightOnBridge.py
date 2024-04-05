# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(U, weight):
    # Implement your solution here
    # need to sort array weight in order up.
    weight.sort()
    num_cars = len(weight)
    count = 0       # number of cars turned back

    # create pointers used for queue, beginning and end
    left, right = 0, num_cars - 1
    
    while left <= right:
        if left == right:   # one car remaining
            count += 1
            break

        if weight[left] + weight[right] <= U:  # if two cars that are heavy are allowed
            left += 1
            right -= 2
        else:                       # heaviest car is not allowed to pass with others+
            right -= 1
        count += 1                  # cars turned back increment

    return count

    # maxWeight = U units at a time.
    # N cars waiting to cross.
    # weight = [] // weight of Kth car is weight[K] // first index is standard 0

    # maxOnBridge = 2, following a queue order
    # if one is removed, all following said car will move up one

    # find the minimum # of drivers turning back to prevent overload

    # an example // if we set the maxWeight to 9, we cannot have vehicles enter, they need to turn
    # N is an integer within the range [1... 1000000000]
    pass