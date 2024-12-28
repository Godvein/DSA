#include <iostream>
#include <queue>

struct Node {

int data;
Node* left;
Node* right;

Node(int value){
data = value;
left = nullptr;
right = nullptr;
}

};

void iterative_bfs(Node* root){
std::queue<Node*> q;
q.push(root);

while(!q.empty()){
Node* node = q.front();
q.pop();

std::cout << node->data << std::endl;

if(node->left != NULL){
q.push(node->left);
}
if(node->right != NULL){
q.push(node->right);
}

}
}

bool binary_search(Node* node, int target){

if(node == NULL){
return false;
}

if(node->data == target){
return true;
}

if(target > node->data){
return binary_search(node->right, target);
}
else{
return binary_search(node->left, target);
}

}


int main(){
Node* root = new Node(5);
Node* node2 = new Node(2);
Node* node3 = new Node(7);
Node* node4 = new Node(3);
Node* node5 = new Node(4);
Node* node6 = new Node(10);

root->left = node2;
root->right = node3;

node2->left = node4;
node2->right = node5;

node3->left = node6;

/*
               5
             /   \
           2      7
          / \    /
         3   4   10
*/



//binary search tree
Node* broot = new Node(10);
Node* bnode2 = new Node(5);
Node* bnode3 = new Node(15);
Node* bnode4 = new Node(3);
Node* bnode5 = new Node(7);
Node* bnode6 = new Node(12);

broot->left = bnode2;
broot->right = bnode3;

bnode2->left = bnode4;
bnode2->right = bnode5;

bnode3->left = bnode6;

/* 
             10
            /  \
           5   15	
          / \  /
         3   7 12  
*/

iterative_bfs(root);

std::cout << binary_search(root, 2) << std::endl;
std::cout << binary_search(root, 11) << std::endl;
return 0;
}


