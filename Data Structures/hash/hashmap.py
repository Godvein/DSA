# HashMaps - Dictionary
d = {
    'bob': 1,    # O(1) for initialization of the dictionary
    'steve': 2,
}
print(d)

# Add to HashMap
d['karen'] = 6  # O(1) on average
print(d)

# Check for the key
if 'karen' in d:  # O(1) on average
    print(True)

# Check value of key
print(d['bob'])  # O(1) on average

# Loop over key-value pairs
for key, value in d.items():  # O(n), where n is the number of items in the dictionary
    print(f"key: {key} value: {value}")

# defaultdict
from collections import defaultdict
default = defaultdict(int)  # O(1) for initialization
print(default[3])  # O(1) for access (default initialization)

# Counter
from collections import Counter
string = 'aaaaaaabbbbbbbbbbccccccccddddddd'
count = Counter(string)  # O(n), where n is the length of the string
print(count)
