#DSA-Tryout

import random
## Linear search algo implementation
def linear_search(num,element_list):
    nog = 0
    for i in range(0, len(element_list)):
        nog+=1
        if (num == element_list[i]):
            print ("found!")
            break
    if (i==len(element_list)):
        print("not found!")
    return nog

    #Remove pass and write the logic to search num in element_list using linear search algorithm
    #Return the total number of guesses made





## Binary search algo implementation   
def binary_search(num,element_list):
    nog=0
    low=0
    high=len(element_list)-1
    mid=high//2
    #print(nog,low,mid,high)
    while(True):
        
        if(num<element_list[mid]):
            nog+=1
            high = mid
            mid = (high+low)//2
            #print(nog,low,mid,high)
            
            
        elif(num>element_list[mid]):
            nog+=1
            low = mid
            mid = ((high-low+1)//2)+low
            #print(nog,low,mid,high)
            
        else:
            nog+=1
           # print(nog,low,mid,high)
            print ("found!")
            break
    
    return nog

#Initializes a list with values 1 to n in random order and returns it
def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1, n+1):
        list_of_elements.append(i)
    return list_of_elements
##    mid=n//2
##    for j in range(0,n):
##        index1=random.randrange(0,mid)
##        index2=random.randrange(mid,n)
##        num1=list_of_elements[index1]
##        list_of_elements[index1]=list_of_elements[index2]
##        list_of_elements[index2]=num1
    

def play(n):
    loe=initialize_list_of_elements(n)
    #print(loe)
    index=random.randrange(len(loe))
    ntg=loe[index]
    #print(ntg)
    nog=linear_search(ntg, loe) # nog=binary_search(ntg, loe)
    #print(loe.index(nog))
    print("number of guesses:", nog)
    # Step 1: Invoke initialize_list_of_elements() by passing n
    # Step 2: Generate a random number from the list of elements. The number should be between 1 and n (both inclusive)
    # Step 3: Invoke find_it() by passing the number generated at Step 2 and list generated at Step 1 and display the return value
    # Remove pass and write the code to implement the above three steps.
    

#Pass different values to play() and observe the output
play(400)
play(100)
play(50)






## Selection Sort algo implementation

def find_next_min(num_list,start_index):
    #Remove pass and write the logic to find the minimum element in a sub-list and return the index of the identified element in the num_list.
    #start_index indicates the start index of the sub-list

    min_element = num_list[start_index]
    start_index+=1
    
    while (start_index<len(num_list)):   
        if (min_element>num_list[start_index]):
            min_element = num_list[start_index]
        start_index+=1
    return num_list.index(min_element)


def swap(num_list, first_index, second_index):
    num_list[first_index], num_list[second_index] = num_list[second_index], num_list[first_index]


def selection_sort(num_list):
    #Remove pass and implement the selection sort algorithm to sort the elements of num_list in ascending order
    total_no_of_passes=0
    for i in range(0, len(num_list)-1):
        total_no_of_passes+=1
        min_index = find_next_min(num_list, i)
        swap(num_list, i, min_index)
    return total_no_of_passes

#Pass different values to the function and test your program
num_list=[8,2,19,34,23, 67, 91]
print("Before sorting;",num_list)
selection_sort(num_list)
print("After sorting:",num_list)






## Bubble sort algo implementaion

def swap(num_list, first_index, second_index):
    global no_of_swaps
    temp=num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]=temp
    no_of_swaps+=1

def bubble_sort(num_list):
    global no_of_passes
    end_index=len(num_list)
    for index1 in range(0, end_index-1):
        swapped=False
        no_of_passes+=1
        for index2 in range(0, (end_index-index1-1)):
            if(num_list[index2]>num_list[index2+1]):
                swap(num_list, index2, index2+1)
                swapped=True
        if(swapped==False):
            break
        print("At the end of pass-",no_of_passes,":",num_list)

no_of_swaps=0
no_of_passes=0
num_list=[5,4,3,2,1]
print("In the beginning:",num_list)
print("______________________________________________")
bubble_sort(num_list)
print("______________________________________________")
print("At the end:",num_list)
print("______________________________________________")
print("No. of swaps:", no_of_swaps)
print("No. of passes:",no_of_passes)



## Merge sort algo implementaion

#lex_auth_0127667368801157123532

from math import ceil
def merge_sort(num_list):
    # Remove pass and write the logic here to return the sorted list
    low = 0
    high = len(num_list)-1
    if low==high:
        return num_list
    else:
        mid = ceil(high/2)
        left_list=[]
        right_list=[]
        for i in range(high+1):
            if i<mid:
                left_list.append(num_list[i])
            else:
                right_list.append(num_list[i])
        sorted_list = merge(merge_sort(left_list), merge_sort(right_list))
        return sorted_list
        

def merge(left_list, right_list):
    # Remove pass and write the logic to merge the elements in the left_list and right_list and return the sorted list
    i=0
    j=0
    sorted_list=[]
    while (i<len(left_list) and j<len(right_list)):
        if left_list[i]<=right_list[j]:
            sorted_list.append(left_list[i])
            i+=1
        else:
            sorted_list.append(right_list[j])
            j+=1        
    while (i<len(left_list)):
        sorted_list.append(left_list[i])
        i+=1
    while (j<len(right_list)):
        sorted_list.append(right_list[j])
        j+=1
    return sorted_list
    


    

num_list=[34, 67, 8, 19, 2, 23, 1, 91]
print("Before sorting:",num_list)
sorted_list = merge_sort(num_list)
print("After sorting:",sorted_list)





## Quick sort algo implementaion


def swap(num_list, first_index, second_index):
    temp=num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]=temp
    

def quick_sort(num_list,low,high):
    if(low>=high):
        return
    split_point=partition(num_list,low,high)
    quick_sort(num_list,low,split_point-1)
    quick_sort(num_list,split_point+1,high)
    
def partition(num_list,low,high):
    pivot=num_list[low]
    i=low+1
    j=high
    done=False
    while not done:
            while (i<=j and num_list[i]<=pivot):
                i=i+1
            while( num_list[j]>=pivot and j>=i):
                j=j-1
            if(j < i):
                done=True
            else:
                swap(num_list,i,j)
    swap(num_list,low,j)  
    return j

num_list=[3,1,0,4,2]
print("Before sorting;",num_list)
l=len(num_list)
quick_sort(num_list,0,l-1)
print("After sorting:",num_list)





