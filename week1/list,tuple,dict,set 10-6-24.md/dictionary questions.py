### 1. Merge Two Dictionaries


def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)


### 2. Invert a Dictionary


def invert_dict(dictionary):
    inverted = {value: key for key, value in dictionary.items()}
    return inverted

original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = invert_dict(original_dict)
print(inverted_dict)


### 3. Sort a Dictionary by Value


def sort_dict_by_value(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[1]))
    return sorted_dict

unsorted_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_dict = sort_dict_by_value(unsorted_dict)
print(sorted_dict)


### 4. Remove Duplicate Values from a Dictionary


def remove_duplicate_values(dictionary):
    unique_values = {}
    for key, value in dictionary.items():
        if value not in unique_values.values():
            unique_values[key] = value
    return unique_values

original_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
unique_dict = remove_duplicate_values(original_dict)
print(unique_dict)


### 5. Group Data by Key


def group_by_key(data, key):
    grouped = {}
    for item in data:
        value = item[key]
        if value in grouped:
            grouped[value].append(item)
        else:
            grouped[value] = [item]
    return grouped

data = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'Chicago'},
    {'name': 'Charlie', 'age': 35, 'city': 'New York'},
    {'name': 'David', 'age': 40, 'city': 'Chicago'}
]

grouped_by_city = group_by_key(data, 'city')
print(grouped_by_city)