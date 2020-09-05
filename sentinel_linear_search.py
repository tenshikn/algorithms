def sentinel_linear_search(array,x):
    last, array[len(array)-1] = array[len(array)-1], x
    i=0
    while array[i]!=x:
        i+=1
    array[len(array)-1]=last #after while loop evaluates to false:
    #put the array back in order
    if i<len(array)-1:
        return i
    else:
        if array[len(array)-1]==x:
            return len(array)-1
        else:
            return f"{x} cannot be found in {array}"


print(sentinel_linear_search([1,2,3,4,5,6,7],4))
print(sentinel_linear_search([1,2,3,4,5,6,7],9))
            
