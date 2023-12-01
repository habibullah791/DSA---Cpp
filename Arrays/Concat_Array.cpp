#include <iostream>
#include <vector>

using namespace std;

vector<int> getConcatenation(vector<int> &nums)
{
    int size = nums.size();
    int newSize = size * 2;

    vector<int> newArr;
    int j = 0;
    for (int i = 0; i < newSize; i++)
    {
        if (j >= size)
        {
            j = 0;
        }

        newArr.push_back(nums[j++]);
    }

    return newArr;
}

int main()
{
    vector<int> nums = {1, 2, 1};
    vector<int> result = getConcatenation(nums);
    cout << "Entring for loop";
    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << endl;
    }

    return 0;
}