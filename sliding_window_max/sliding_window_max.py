'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Loop through the array to compare the k numbers and return the max
    #move to the next index and do it all over again
    #how do you get to reach the first k number of elements in the array
    #how do you move to the next three
    #how do you compare the k window values
    #save the max in a variable, save all max var in an array
    #replace the max with the next window's max
    #return the max
    #the end of the array should be defined by using the k value to minus the end of array len(arr[-k])
    allmax = []
    if len(nums) != 0:
        for index,number in enumerate(nums):
            #stop before getting to end of aray
            if len(nums) < k:
                return allmax
            else:
                window = nums[index:index+k]
                print("first window",window)
                print(index, number)
                #compare the first k index and move k to next index
                #have the window stop before array is over
                window_max = max(window)
                
                # print(window_max)
                print("window max: ", window_max)
                allmax.append(window_max)
            
                print("array: ", allmax)
    return allmax

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
#3,3,5,5,6,7
    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
