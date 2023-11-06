#include <iostream>
#include <queue>
#include <utility>
using namespace std;

class Node
{
public:
    int data;
    Node *left;
    Node *right;

    Node(int data)
    {
        this->data = data;
        this->left = NULL;
        this->right = NULL;
    }
};

// Function to build a binary tree recursively
Node *buildTree(Node *node)
{
    cout << "Enter The Data" << endl;
    int data;
    cin >> data;

    node = new Node(data);

    if (data == -1)
    {
        return NULL; // If data is -1, it indicates an empty node
    }

    cout << "Enter the left child of " << data << endl;
    node->left = buildTree(node->left);
    cout << "Enter the right child of " << data << endl;
    node->right = buildTree(node->right);
    return node;
}

// Function to perform level-order traversal of a binary tree
void levelOrderTrivarsal(Node *root)
{
    queue<Node *> q;
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
                q.push(NULL); // Use NULL as a level separator
            }
        }
        else
        {
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
}

// Function to perform in-order traversal of a binary tree
void inOrderTrivarsal(Node *node)
{
    if (node == NULL)
    {
        return;
    }

    inOrderTrivarsal(node->left);
    cout << node->data << " ";
    inOrderTrivarsal(node->right);
}

// Function to perform pre-order traversal of a binary tree
void preOderTrivarsal(Node *node)
{
    if (node == NULL)
    {
        return;
    }

    cout << node->data << " ";
    preOderTrivarsal(node->left);
    preOderTrivarsal(node->right);
}

// Function to perform post-order traversal of a binary tree
void postOrderTrivarsal(Node *node)
{
    if (node == NULL)
    {
        return;
    }

    postOrderTrivarsal(node->left);
    postOrderTrivarsal(node->right);
    cout << node->data << " ";
}

// Function to build a binary tree from level order input
void buildFromLevelOrder(Node *&node)
{
    queue<Node *> q;
    cout << "Enter data for root :  ";
    int data;
    cin >> data;
    node = new Node(data);
    q.push(node);

    while (!q.empty())
    {
        Node *temp = q.front();
        q.pop();

        cout << "Enter data for the left node for " << temp->data << endl;
        int leftData;
        cin >> leftData;
        if (leftData != -1)
        {
            temp->left = new Node(leftData);
            q.push(temp->left);
        }

        cout << "Enter data for the right node for " << temp->data << endl;
        int rightData;
        cin >> rightData;
        if (rightData != -1)
        {
            temp->right = new Node(rightData);
            q.push(temp->right);
        }
    }
}

// Function to count the number of leaf nodes in a binary tree
void countLeafNodes(Node *node, int &count)
{
    if (node == NULL)
    {
        return;
    }

    countLeafNodes(node->left, count);
    if (node->left == NULL && node->right == NULL)
    {
        count++;
    }
    countLeafNodes(node->right, count);
}

//  Function to find the max depth of the tree
int maxDepth(Node *node)
{

    if (node == NULL)
    {
        return 0;
    }

    int left = maxDepth(node->left);
    int right = maxDepth(node->right);

    int max = std::max(left, right) + 1;

    return max;
}
pair<int, int> fastDiameter(Node *root)
{
    if (root == NULL)
    {
        pair<int, int> p = make_pair(0, 0);
        return p;
    }

    pair<int, int> left = fastDiameter(root->left);
    pair<int, int> right = fastDiameter(root->right);

    int option1 = left.first;
    int option2 = right.first;
    int option3 = left.second + right.second + 1;

    pair<int, int> ans;

    ans.first = std::max(option1, std::max(option2, option3));
    ans.second = std::max(left.second, right.second) + 1;

    return ans;
}

// Function to return diameter of the tree
int diameterOFTree(Node *node)
{
    return fastDiameter(node).first;
}

// Functioj to check if the tree is balanced
bool isBalanced(Node *root)
{
    if (root == NULL)
    {
        return true;
    }

    bool left = isBalanced(root->left);
    bool right = isBalanced(root->right);

    bool diff = abs(maxDepth(root->left) - maxDepth(root->right)) <= 1;

    if (left && right && diff)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
    cout << "Creating Tree : " << endl;
    Node *root = NULL;

    // input will be 1 3 7 -1 -1 11 -1 -1 5 17 -1 -1 -1
    // root = buildTree(root);
    buildFromLevelOrder(root);

    // levelOrderTrivarsal(root);

    // cout << "In - order Trivarsal  - ";
    // inOrderTrivarsal(root);

    // cout << "\nPre - order Trivarsal  - ";
    // preOderTrivarsal(root);

    // cout << "\nPost - order Trivarsal  - ";
    // postOrderTrivarsal(root);

    cout << endl;
    int count = 0;
    countLeafNodes(root, count);
    cout << "Number of leaf nodes : " << count << endl;
    cout << "Depth of the binary tree : " << maxDepth(root) << endl;
    cout << "Diameter of the binary tree : " << diameterOFTree(root) << endl;
    cout << "Is binary tree Balanced: " << isBalanced(root) << endl;
}
