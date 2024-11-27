#include <iostream>
#include <queue>

int main(){
std::queue<int> q;

//push element in queue
q.push(1);
q.push(2);
q.push(3);

//pop element from queue
q.pop();

//view front and last element of queue
std::cout << "front element: " << q.front() << "\n";
std::cout << "back element: " << q.back() << "\n";
return 0;
}
