#include <iostream>

using namespace std;

// function prototype
int fibonacciSeries(int number);

int main()
{

    int number, result;

    cout << "Enter the number  :";
    cin >> number;

    result = fibonacciSeries(number);
    cout << "Sum of fibonacci seres is : " << result;
}

int fibonacciSeries(int number)
{

    int firstNumber = 0;
    int secondNumber = 1;
    int sum = 0;
    int total = 0;

    cout << firstNumber << " "<< secondNumber << " ";

    for (size_t i = 0; i < number; i++)
    {
        sum = firstNumber + secondNumber;
        firstNumber = secondNumber;
        secondNumber = sum;

        cout << sum << " ";
        total += sum;
    }
    return total ;
}