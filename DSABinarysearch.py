#This code demonstrated the binary search algorithm in Python. Binary search is an efficient algorithm for finding an item from a sorted list of items. 
# It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index
        
        # Check if the target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore the right half
        else:
            right = mid - 1
            
    # Target was not found in the array
    return -1
# Example usage
if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    target_value = int(input("Enter the value to search for: "))
    
    result = binary_search(sorted_array, target_value)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array.")   
