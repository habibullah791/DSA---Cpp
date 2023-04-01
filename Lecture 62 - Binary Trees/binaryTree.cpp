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

Node *buildTree(Node *root)
{
    int data;

    cout << "Enter Data : ";
    cin >> data;

    root = new Node(data);

    // base condition
    if (data == -1)
    {
        return NULL;
    }

    //  inserting in left and right of node
    cout << "Enter data in left of " << data << " : " << endl;
    root->left = buildTree(root->left);

    cout << "Enter data in right of " << data << " : " << endl;
    root->right = buildTree(root->right);

    return root;
}

void levelOrderTriversal(Node *root)
{
    // using queue fot level Order Triversal

    queue<Node *> q;
    int count = 1;
    q.push(root);
    q.push(NULL);

    while (!q.empty())
    {
        Node *temp = q.front();
        q.pop();

        if (temp == NULL)
        {
            cout << endl;

            if (!q.empty())
            {
                q.push(NULL);
            }
        }
        else
        {
            count++;
            cout << temp->data << " ";

            if (temp->left)
            {
                q.push(temp->left);
            }

            if (temp->right)
            {
                q.push(temp->right);
            }
        }
    }

    cout << "HEight is : " << count << endl;
}
void inOrderTrivarsal(Node *root)
{

    if (root == NULL)
    {
        return;
    }

    inOrderTrivarsal(root->left);
    cout << root->data << " ";
    inOrderTrivarsal(root->right);
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
    

    // root = buildTree(root);
    // cout << endl;

    levelOrderTriversal(root);
    cout << endl;

    inOrderTrivarsal(root);
}