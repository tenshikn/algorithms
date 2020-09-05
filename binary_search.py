#binary_search

def binary_search(array, key):
    """binary search function that works for a sorted array"""
    
    p = 0
    r = len(array) - 1
    while p <= r:
        q = (p + r)//2
        if array[q] == key:
            return q
        if array[q] > key:
            r = q - 1
        elif array[q] < key:
            p = q + 1
        else:
            return None


if __name__ == "__main__":
    num_list = [2, 3, 6, 8, 8, 11, 31]
    
    print(binary_search(num_list, 11))
    
    print(binary_search(num_list, 8))
    
    print(binary_search(num_list, 5))



























