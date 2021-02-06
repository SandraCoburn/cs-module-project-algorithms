'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache): #add cache to optimize. evey n value now is only computed once. It reduces the runtime from O(3^n) to O(n). It does increase space complexity
    # Count how many possible ways of eating x number of cookies
    #What's the base case if done recursevely
    #if n == 0 return 1 if n is a negative return 0
    '''runtime O(3^n)'''
    # if n < 0:
    #     return 0
    # if n == 0:
    #     return 1
    # else:
    #     return eating_cookies(n-1,) + eating_cookies(n-2) + eating_cookies(n-3)

    if n < 0:
        return 0
    if n == 0:
        return 1
    #check the cache to see if it holds the answer this branch is looking for
    elif n in cache:
        return cache[n]
    else:
        #otherwise, n is not in the cahce, so we need to commpute the answer the "nomal" way
        #once the answer is computed, save it in the cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]

#how can we optimize this?
#how do we reduce the amount of redundant work?
    #use a data structure (cache) to answer that some other branch has already done
    #someone has to still figure ou the answer in the first place
    #but once that answer is computed, we'll share that answer with any other branch that needs to calculate the same thing
    #branches that need an answer tht's already been computed can check the cache
    #to see if the answer is already in there and just pull it out
    #what data structure should we use for the cache?
    #save the n value for the branch along with its associated answer
    #save the n value as a key and the associated answer as its value in a dict
    #we'll need to pass the dict to each recursive call

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    #cache = {i: 0 for i in range(num_cookies+1)}
    #cache =[0 for _ in range(num_cookies+1)]

    print(f"There are {eating_cookies(num_cookies, {})} ways for Cookie Monster to each {num_cookies} cookies")
