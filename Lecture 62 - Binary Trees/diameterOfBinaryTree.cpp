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

int diameterOfTree(Node *root, int *height)
{
    if (root == NULL)
    {
        *height = 0;
        return 0;
    }

    // int leftHeight = heightOfBinaryTree(root->left);
    // int rightHeight = heightOfBinaryTree(root->right);

    // int currentDiameter = leftHeight + rightHeight + 1;

    // int leftDiameter = diameterOfTree(root->left);
    // int rightDiameter = diameterOfTree(root->right);

    // return max(currentDiameter, max(leftDiameter, rightDiameter));

    // optimised code

    int lh = 0, rh = 0;
    int leftDiameter = diameterOfTree(root->left, &lh);
    int rightDiameter = diameterOfTree(root->right, &rh);

    int currentDiameter = lh + rh + 1;

    *height = max(lh, rh) + 1;
    return max(currentDiameter, max(leftDiameter, rightDiameter));
}
int main()
{
    Node *root = NULL;
    int height = 0;

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

    int diameter = diameterOfTree(root, &height);

    cout << "Diameter of tree is: " << diameter << endl;
}