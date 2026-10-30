##class TestIterator:
##    value = 0
##    def __next__(self):
##        self.value += 1
##        if self.value > 10: raise StopIteration
##        return self.value
##    def __iter__(self):
##        return self
##
##t = TestIterator()
##itr = iter(t)

# [2, -3, 5, -1, 3, -9, 8, -2, 7]

# maximum sum of a contagious subarray in an array

def kanade_algo(arr):
    res = currmax = arr[0]
    
    for i in range(1, len(arr)):
        currmax = max(arr[i], currmax+arr[i])
        res = max(currmax, res)
    return res


def kanade_algo_alter(arr):
    res = arr[0]
    
    for i in range(len(arr)):
        currsum = 0
        
        for j in range(i,len(arr)):
            currsum += arr[j]
            res = max(currsum, res)

    return res
        



















    
    
    
