# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        smallest = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = smallest
    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    for i in range(1, len(arr)):
        current_number = arr[i]
        current_index = i
        #Iterate to the left until an element is less than the current index number
        while current_index > 0 and arr[current_index-1] > current_number:
            #Shift elements to the right
            arr[current_index] = arr[current_index-1]
            current_index -= 1
        #Insert Element into right postion
        arr[current_index] = current_number

    return arr

# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr