#include <iostream>
#include <vector>
#include <climits>
using namespace std;

vector<int> FindThreeLaargestNumber(vector<int> array)
{
    //  create a vector to store the three largest number
    vector<int> threeLargest = {INT_MIN, INT_MIN, INT_MIN};
    // print the vector to the console

    for (size_t i = 0; i < array.size(); i++)
    {

        if (array[i] > threeLargest[2])
        {
            threeLargest[0] = threeLargest[1];
            threeLargest[1] = threeLargest[2];
            threeLargest[2] = array[i];
        }
        else if (array[i] > threeLargest[1])
        {
            threeLargest[0] = threeLargest[1];
            threeLargest[1] = array[i];
        }
        else if (array[i] > threeLargest[0])
        {
            threeLargest[0] = array[i];
        }
    }

    return threeLargest;
}

int main()
{
    vector<int> array = {141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7};

    //  call the function and print the result to the console
    vector<int> result = FindThreeLaargestNumber(array);
    for (size_t i = 0; i < result.size(); i++)
    {
        cout << result[i] << " ";
    }
}