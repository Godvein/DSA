#include <iostream>
#include <stack>

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

void preorderTraversal(Node* root){
if(root != nullptr){
std::cout << root->data << std::endl;
preorderTraversal(root->left);
preorderTraversal(root->right);
}
return;
}

void inorderTraversal(Node* root){
if(root != nullptr){
inorderTraversal(root->left);
std::cout << root->data << std::endl;
inorderTraversal(root->right);
}
return;
}

void postorderTraversal(Node* root){
if(root != nullptr){
postorderTraversal(root->left);
postorderTraversal(root->right);
std::cout << root->data << std::endl;
}
return;
}

void iterative_dfs(Node* root){
std::stack<Node*> stack;
stack.push(root);

while(!stack.empty()){
Node* node = stack.top();
std::cout << node->data << std::endl;
stack.pop();
if(node->right != NULL){
stack.push(node->right);
}
if(node->left != NULL){
stack.push(node->left);
}

}
}

bool dfs_search(Node* node,int value){
if(node == NULL){
return false;
}
else if(node->data == value){
return true;
}
else{
return dfs_search(node->left, value) || dfs_search(node->right, value);
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

preorderTraversal(root);
inorderTraversal(root);
postorderTraversal(root);

iterative_dfs(root);

std::cout << dfs_search(root, 2) << std::endl;
std::cout << dfs_search(root, 11) << std::endl;
return 0;
}



