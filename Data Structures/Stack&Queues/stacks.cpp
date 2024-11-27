#include <iostream>
#include <stack>
int main(){
std::stack<int> s;

//push an element into stack
s.push(1);
s.push(2);
s.push(3);

//get size of stack
std::cout << "size: " << s.size() << "\n";

//pop from the stack 
s.pop();

//view top element of stack
std::cout << "top: " << s.top() << "\n";
return 0;
}
