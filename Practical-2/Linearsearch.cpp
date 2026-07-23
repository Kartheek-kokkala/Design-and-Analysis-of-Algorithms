#include <iostream>
using namespace std;

int main()
{
    int arr[] = {45, 12, 78, 34, 90, 23};
    int n = 6;

    int searchElement = 90;
    int position = -1;

    
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == searchElement)
        {
            position = i;
            break;
        }
    }

    if (position != -1)
    {
        cout << "Element " << searchElement
             << " found at index: " << position;
    }
    else
    {
        cout << "Element not found";
    }

    return 0;
}
