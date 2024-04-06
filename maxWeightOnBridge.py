# find minimum # of drivers turning back to prevent overload
# ex. if we set maxWeight = 9, we can't have vehicles enter, they need to turn    
# N is an integer within the range [1...1,000,000,000]    

def solution(U, weight):

    # need to sort array weight in order up.
    weight.sort()
    num_cars = len(weight)

    # number of cars turned back
    count = 0

    # create pointers used for queue, beginning and end
    left, right = 0, num_cars - 1
    
    while left <= right:
        if left == right:                       # one car remaining                       
            count += 1
            break

        if weight[left] + weight[right] <= U:   # if two heavy cars are allowed
            left += 1
            right -= 2
        else:                                   # heaviest car can't pass w/ another
            right -= 1
        count += 1                              # cars turned back incremented

    return count

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")