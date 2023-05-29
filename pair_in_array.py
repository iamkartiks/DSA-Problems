def find_pairs(array, target_sum):
    pairs = []
    complements = {}

    for num in array:
        complement = target_sum - num
        if complement in complements:
            pairs.append((num, complement))
            print(pairs)
        complements[num] = complement
    print(complements)

    return pairs

# Example usage
array = [2, 4, 6, 8, 10]
target = 14
result = find_pairs(array, target)
print("Pairs:", result)
