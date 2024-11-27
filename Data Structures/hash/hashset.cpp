#include <iostream>
#include <unordered_set>

int main() {
std::unordered_set<int> hashset;

//insert into hashset
hashset.insert(1);
hashset.insert(2);
hashset.insert(3);

//remove element from hashset
hashset.erase(2);

//check if element exist
if(hashset.find(1) != hashset.end()){
std::cout << "element found" << "\n";
}

//display set element
for(int element : hashset){
std::cout << element << "\n";
}
}

