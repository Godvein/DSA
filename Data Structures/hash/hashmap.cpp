#include <iostream>
#include <unordered_map>

int main(){
std::unordered_map<std::string, int> map = {{"Bob", 1}};

//insert into map
map["Art"] = 2;
map["leena"] = 3;

//remove keys from map
map.erase("Art");

//display key and value from map
for(const auto& pair: map){
std::cout << "key: " << pair.first << " value: " << pair.second << "\n";
}

//find key from map
if(map.find("Bob") != map.end()){
std::cout << "key exists" << "\n";
}
return 0;
}
