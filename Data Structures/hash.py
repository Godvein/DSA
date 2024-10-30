#hashset
a = set()
#add element to hashset
a.add(1)
a.add(2)
a.add(3)
a.add(4)
#check if element exist in hashset
if 1 in a:
    print(True)

#remove element
a.remove(4)

#remove duplicate character with hashset
string = 'aaaaaaabbbbbbbbbbccccccccddddddd'
sets = set(string)
print(sets)
