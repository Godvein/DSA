#include <iostream>

int binarySearch(int arr[],int size,int target){

int low = 0;
int high = size - 1;

while(low <= high){

int mid = (low + high) / 2;

if(arr[mid] == target){
return mid;
}
else if(target > arr[mid]){
low = mid + 1;
}
else if(target < arr[mid]){
high = mid - 1;
}
}
return -1;
}

int main(){
int arr[] = {10, 14, 22, 30, 45, 50, 66};
int size = sizeof(arr)/sizeof(int);
int result = binarySearch(arr,size, 22);

if(result != -1){
std::cout << "element found at index: " << result << std::endl;
}
else{
std::cout << "element not found" << std::endl;
}
return 0;
}
