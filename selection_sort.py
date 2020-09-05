#Selection Sort algorithm - O(n^2)

def selection_sort(array):
    for i in range(0, len(array)-1):
        j = i+1
        while j < len(array):
            if array[j]<array[i]:
                array[i], array[j] = array[j], array[i]
                j+=1
            else:
                j+=1
    return array



if __name__ == "__main__":
    print(selection_sort([6,4,5,8,7,3,2,1]))
                
