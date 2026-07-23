#include <iostream>
using namespace std;

int main() {
    int arr[] = {3, 8, 12, 17, 25, 31, 46};
    int n = 7;
    int target = 25;

    int low = 0;
    int high = n - 1;
    bool found = false;

    while (low <= high) {
        int mid = (low + high) / 2;

        if (arr[mid] == target) {
            cout << "Element found at index: " << mid;
            found = true;
            break;
        }
        else if (arr[mid] < target) {
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }

    if (!found) {
        cout << "Element not found";
    }

    return 0;
}
