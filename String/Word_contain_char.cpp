#include <iostream>
#include <vector>
#include <string>

using namespace std;
vector<int> findWordsContaining(vector<string> &words, char x)
{
    vector<int> res;
    for (int i = 0; i < words.size(); i++)
    {
        if (words[i].find(x) != string::npos)
        {
            res.push_back(i);
        }
    }
    return res;
}

int main()
{
    vector<string> words = {"abc", "bcd", "cde"};
    char x = 'a';
    vector<int> result = findWordsContaining(words, x);
    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << endl;
    }

    return 0;
}