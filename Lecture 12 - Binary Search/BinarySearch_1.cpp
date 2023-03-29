#include <iostream>
using namespace std;

int binarySearch(int array[], int size, int key)
{

    int start = 0;
    int end = size - 1;
    int mid = start + (end - start) / 2; // to avoid overflow   

    for (size_t i = 0; i < size; i++)
    {
        if (key == array[mid])
        {
            return mid;
        }
        else if (array[mid] < key)
        {
            start = mid + 1;
            mid = start + end / 2;
        }
        else
        {
            end = mid - 1;
            mid = start + end / 2;
        }
    }

    return 0;
}

int main()
{
    int array[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int result;

    result = binarySearch(array, 10, 10);

    cout << (result == 0 ? "Not Found" : "Found at index: ") << result << endl;
}