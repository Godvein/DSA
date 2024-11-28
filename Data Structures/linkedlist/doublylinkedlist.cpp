#include <iostream>

struct Node{
int value;
Node* prev;
Node* next;
};

typedef Node* nodeptr;

void displayList(nodeptr head){
while(head!=NULL){
std::cout << "<-" << head->value << "->";
head = head->next;
}
std::cout << "\n";
}

void insertBeginning(nodeptr& head, int value){
nodeptr newptr;
newptr = new Node;
newptr->value = value;
newptr->next = head;
newptr->prev = NULL;
if(head != NULL){
head->prev = newptr;
}
head = newptr;
}

void insertEnd(nodeptr& head, int value){
nodeptr newptr;
newptr = new Node();
newptr->value = value;
newptr->next = NULL;
nodeptr temp;
temp = head;

if(head == NULL){
head = newptr;
}
else{
while(temp->next != NULL){
temp = temp->next;
}
temp->next = newptr;
newptr->prev = temp;
}
}
int main(){
nodeptr head;
head = new Node();
head->value = 1;
head->prev = NULL;
head->next = NULL;

insertBeginning(head, 2);
insertEnd(head, 3);
displayList(head);
return 0;
}
