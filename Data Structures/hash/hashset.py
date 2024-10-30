# HashSet
a = set()  # O(1) for initialization

# Add elements to HashSet
a.add(1)  # O(1) on average
a.add(2)  # O(1) on average
a.add(3)  # O(1) on average
a.add(4)  # O(1) on average

# Check if an element exists in HashSet
if 1 in a:  # O(1) on average
    print(True)

# Remove element
a.remove(4)  # O(1) on average

# Remove duplicate characters with HashSet
string = 'aaaaaaabbbbbbbbbbccccccccddddddd'
sets = set(string)  # O(n), where n is the length of the string
print(sets)

