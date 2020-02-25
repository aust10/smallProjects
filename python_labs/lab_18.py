

#test data 
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.
def peaks(data):

    peaks_list = []
#starting at 1 and stepping -1 makes it so we dont check the beginging or the end because it does not matter 
    for i in range(1,len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks_list.append(i)
    return peaks_list
    
print(peaks(data))

#alleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

def valley(data):

    valley_list = []
#starting at 1 and stepping -1 makes it so we dont check the beginging or the end because it does not matter
    for i in range(1,len(data)-1):
        if data[i] < data[i-1] and data[i] < data[i+1]:
            valley_list.append(i)
    return valley_list
print(valley(data))

#peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

def peaks_and_vallys(data):

    peaks_list = peaks(data)
    valley_list = valley(data)

    peaks_valley = peaks_list + valley_list
    peaks_valley.sort()
    return peaks_valley
print (peaks_and_vallys(data))

def find_highest_point(data):
    #  arguments: list of elevations as ints 
    #     return: highest point in elevations 

    highest = 0
    for point in data:
        if point > highest:
            highest = point
    print(f"the highest point is {highest}")
    return highest

def print_range(data):
    #  arguments: none
    #     returns: how much water in range (also prints range) 

    # counter for calculating how much water 
    water_counter = 0

    # nested for loops for printing out data.  left index is row, right index is column
    # use highest point plus two to account for the fact that 1) hight starts at 1, not 0 and 
    # 2) keep one row of sky above highest mountain
    for y in range(find_highest_point(data)+1,0,-1):

        # x will be an element in data, not an index
        for x in range(len(data)):
            # determine what to print: '  ' for air, 'X ' for ground, 'O ' for water
            # if too high and not water, print " "
            if data[x] < y and not is_water(data, x, y):
                print('   ', end='')
            # if too high and is water, print O
            elif data[x] < y and is_water(data, x, y):
                print('O  ', end='')
                water_counter += 1
            # else, must be ground so print X
            elif data[x] >= y:
                print('X  ', end='')
        print()

    # return water counter
    return water_counter

def is_water(data, x, y):
    ''' parameters: data and location (index) along range, and height we're evaluating
        return: returns true if water, false if not water'''

    # recursively check to left and right, if there is land return true, else return false
    is_land_to_left = check_left(data,x,y)
    is_land_to_right = check_right(data,x,y)

    # return if there is land to both left and right
    return is_land_to_left and is_land_to_right

def check_left(data,x,y):
    # edge case: you've found the edge
    if x <= -1 or x >= len(data):
        return False        # you've found the edge
    elif data[x] == y:
        return True         # you've found land...element in data is equal to current height
    else:
        return check_left(data, x-1, y)     # call the check left function recursively, passing x-1 as the new x coordinate

# recursive function to check right
def check_right(data,x,y):
    # edge case: you've found the edge
    if x <= -1 or x >= len(data):
        return False        # you've found the edge
    elif data[x] == y:
        return True         # you've found land...element in data is equal to current height
    else:
        return check_right(data, x+1, y)     # call the check left function recursively, passing x+1 as the new x coordinate


print(f' there is {print_range(data)} water in this range')