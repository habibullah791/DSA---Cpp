#include <iostream>
#include <queue>
using namespace std;

class Node
{
public:
    int data;
    Node *left;
    Node *right;

    Node(int d)
    {
        data = d;
        left = NULL;
        right = NULL;
    }
};

int heightOfBinaryTree(Node *root)
{
    if (root == NULL)
    {
        return 0;
    }

    int leftHeight = heightOfBinaryTree(root->left);
    int rightHeight = heightOfBinaryTree(root->right);

    return max(leftHeight, rightHeight) + 1;
}
int main()
{
    Node *root = NULL;

    // add node in tree without using buildTree function
    //  tree representation
    //          1
    //        /   \
    //       2     3
    //      / \   / \
    //     4   5 6   7
    //   / \     \
    //  8   9     10
    // /
    // 11

    root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->left = new Node(6);
    root->right->right = new Node(7);
    root->left->left->left = new Node(8);
    root->left->left->right = new Node(9);
    root->right->left->right = new Node(10);
    root->left->left->left->left = new Node(11);

    int height = heightOfBinaryTree(root);

    cout << "Heigt Is : " << height;
}