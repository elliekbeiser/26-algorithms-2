def linear_search(data, target):
    """
    Search for target in data using linear search.
    
    Linear search checks each element sequentially until finding the target
    or reaching the end of the list.
    
    Args:
        data (list): List to search (can be sorted or unsorted)
        target: Item to find
    
    Returns:
        int: Index of target if found, -1 if not found
    
    Time Complexity: O(n) - must check up to n elements
    Space Complexity: O(1) - uses constant extra space
    
    Example:
        linear_search([5, 2, 8, 1, 9], 8) returns 2
        linear_search([5, 2, 8, 1, 9], 7) returns -1
    """
    # TODO: Implement linear search that loops through each element and returns its index if found and -1 if not found.
    
    for item in data:
        if item == target:
            return item
        else:
            return -1


linear_search([5, 2, 8, 1, 9], 8)
