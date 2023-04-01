#include <iostream>
#include <queue>
using namespace std;

int main()
{
    priority_queue<int> p;
    p.push(5);
    p.push(9);
    p.push(4);
    p.push(3);
    p.pop(); // remove the top element
    while (!p.empty())
    {
        cout << ' ' << p.top(); // printing elements
        p.pop();
    }
}