#include <iostream>
#include <vector>
using namespace std;

int binarySearch(vector<int> array, int target)
{

    int start = 0;
    int end = array.size() - 1;
    int mid = (start + end) / 2;

    for (size_t i = 0; i < array.size(); i++)
    {
        cout << "Mid: " << mid << endl;
        if (target == array[mid])
        {
            return mid;
        }
        else if (array[mid] < target)
        {
            start = mid + 1;
        }
        else
        {
            end = mid - 1;
        }
        mid = (start + end )/ 2;
    }

    return -1;
}

int main()
{
    vector<int> array = {0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355};
    int target = 355;
    int result = binarySearch(array, target);

    cout << (result == 0 ? "Not Found" : "Found at index: ") << result << endl;
}