"""
Flatten a 2-level nested list into a single list.

Example:
Input:  [[1, 2], [3, 4], [5]]
Output: [1, 2, 3, 4, 5]
"""
from itertools import chain

def flatten_list(nested: list) -> list:
    """
    Flatten a 2-level nested list
    
    Args:
        nested: List of lists (2 levels only)
    
    Returns:
        Flattened list
    """
    
    return list(chain.from_iterable(nested))


"""
Access values from nested dictionaries using a path.

Example:
data = {
    "user": {
        "profile": {
            "name": "Alice",
            "age": 30
        }
    }
}

get_nested_value(data, ["user", "profile", "name"]) → "Alice"
get_nested_value(data, ["user", "profile", "city"]) → None (doesn't exist)
"""

def get_nested_value(data: dict, path: list, default=None):
    """
    Safely get value from nested dict using path
    
    Args:
        data: Nested dictionary
        path: List of keys to traverse
        default: Value to return if path doesn't exist
    
    Returns:
        Value at path or default
    """
    curr = data

    for key in path:
        if isinstance(curr, dict):
            current = current.get(key)
        else:
            return None
    return current



"""
Flatten a nested dictionary using dot-notation for keys.

Example:
Input: {
    "user": {
        "name": "Alice",
        "address": {
            "city": "SF",
            "zip": "94102"
        }
    }
}

Output: {
    "user.name": "Alice",
    "user.address.city": "SF",
    "user.address.zip": "94102"
}
"""

def flatten_dict(nested: dict, parent_key: str = '', sep: str = '.') -> dict:
    """
    Flatten nested dictionary
    
    Args:
        nested: Nested dictionary
        parent_key: Prefix for keys (used in recursion)
        sep: Separator for keys (default '.')
    
    Returns:
        Flattened dictionary
    """
    pass


"""
Extract specific fields from a list of dictionaries.

This is VERY common in API responses and database queries!

Example:
users = [
    {"name": "Alice", "age": 30, "city": "SF"},
    {"name": "Bob", "age": 25, "city": "NYC"},
    {"name": "Charlie", "age": 35, "city": "LA"}
]

extract_field(users, "name") → ["Alice", "Bob", "Charlie"]
extract_fields(users, ["name", "city"]) → [
    {"name": "Alice", "city": "SF"},
    {"name": "Bob", "city": "NYC"},
    {"name": "Charlie", "city": "LA"}
]
"""

def extract_field(data: list, field: str) -> list:
    """Extract single field from list of dicts"""
    res = []

    for user in data:
        res.append(user[field])
    
    return res


def extract_fields(data: list, fields: list) -> list:
    """Extract multiple fields from list of dicts"""
    res = []

    for user in data:
        d = {}
        for field in fields:
            d[field] = user[field]
        res.append(d)
    return res


"""
Group list of dictionaries by a key.

This is SQL's GROUP BY in Python!

Example:
patients = [
    {"name": "Alice", "city": "SF", "age": 30},
    {"name": "Bob", "city": "NYC", "age": 25},
    {"name": "Charlie", "city": "SF", "age": 35}
]

group_by(patients, "city") → {
    "SF": [
        {"name": "Alice", "city": "SF", "age": 30},
        {"name": "Charlie", "city": "SF", "age": 35}
    ],
    "NYC": [
        {"name": "Bob", "city": "NYC", "age": 25}
    ]
}
"""
from collections import defaultdict 

def group_by(patients: list, key: str) -> dict:
    """
    Group list of dicts by a key
    
    Args:
        data: List of dictionaries
        key: Key to group by
    
    Returns:
        Dictionary where keys are unique values of the grouping key,
        values are lists of records with that key value
    """
    d = defaultdict(list)

    for patient in patients:
        d[patient[key]].append(patient)
    return dict(d)

patients = [
    {"name": "Alice", "city": "SF", "age": 30},
    {"name": "Bob", "city": "NYC", "age": 25},
    {"name": "Charlie", "city": "SF", "age": 35}
]
print(group_by(patients, "city"))


"""
Flatten a deeply nested list (recursive).

Example:
Input:  [1, [2, [3, [4, 5]]], 6, [7, 8]]
Output: [1, 2, 3, 4, 5, 6, 7, 8]

This requires RECURSION because you don't know the depth!

Base case: If isinstance is not list then append
recursive case: 
"""

def deep_flatten(nested) -> list:
    """
    Recursively flatten a nested list of any depth
    
    Args:
        nested: Can be int, or list of ints/lists
    
    Returns:
        Flattened list
    """
    res = []

    for elem in nested:
        if isinstance(elem, list):
            res.extend(deep_flatten(elem))
        else:
            res.append(elem)
    return res






