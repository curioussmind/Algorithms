def binary_search(list, item):
    low = 0  # low and high keep track of which part of the list
    high = len(list) - 1 #we seacrh in.

    while low <= high:  # while we haven't narrowed it doen to  one element
        mid = (low + high) #check the middle element
        guess = list[mid]
        if guess == item: #found the item
            return mid
        elif guess > item: #the guess was too high
            high = mid -1
        else:           # the guess was too low
            low = mid + 1
    return None # the item doesn't exist

my_list = [1, 3, 5, 7, 9] #test

print(binary_search(my_list, 3)) # output: 1  --> remember that lists start at 0 so the second slot has index 1
print(binary_search(my_list, -1)) # output None --> "None" means nil in python. it indicates that the iten wasn't found.