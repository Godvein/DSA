#include <iostream>

struct Node{
int value;
Node* next;
};

typedef Node* nodeptr;

void insertNodeBeginning(nodeptr& head,int value){
nodeptr newptr;
newptr = new Node();
newptr->value = value;
newptr->next = head;
head = newptr;
}

void displayList(nodeptr head){
while(head != NULL){
std::cout << head->value << "->";
head = head->next;
}
std::cout << "\n";
}

void insertNodeEnd(nodeptr& head, int value){
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
}
}

int main(){
nodeptr head;
head = new Node();
head->value = 1;
head->next =  NULL;

insertNodeBeginning(head, 2);
insertNodeEnd(head, 3);
displayList(head);
return 0;
}
