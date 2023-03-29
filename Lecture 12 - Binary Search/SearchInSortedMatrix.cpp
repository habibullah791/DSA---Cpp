#include <iostream>
#include <vector>

using namespace std;

vector<int> SearchInSortedMatrix(vector<vector<int>> matrix, int target)
{

    vector<int> result;

    cout << matrix.size() << endl;
    cout << matrix[0].size() - 1 << endl;

    for (size_t i = 0; i < matrix.size(); i++)
    {
        for (size_t j = 0; j < matrix[0].size(); j++)
        {
            if (matrix[i][j] == target)
            {
                result.push_back(i);
                result.push_back(j);
                return result;
            }
        }
    }
    result.push_back(-1);
    result.push_back(-1);
    return result;
}

int main()
{
    vector<vector<int>> myVector = {
        {1, 4, 7, 12, 15, 1000},
        {2, 5, 19, 31, 32, 1001},
        {3, 8, 24, 33, 35, 1002},
        {40, 41, 42, 44, 45, 1003},
        {99, 100, 103, 106, 128, 1004},
    };

    vector<int> result = SearchInSortedMatrix(myVector, 40);
    // print the result
    for (auto i : result)
    {
        cout << i << " ";
    }
}