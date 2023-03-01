#include<iostream>
using namespace std;

int main()
{
    int arr[] = {3,3};
    int size = sizeof(arr)/sizeof(arr[0]);
    for (int i=1; i<size;i++ )
    {
        if (arr[i-1] == arr[i])
        {
            cout << "True" << endl;
            return 0;
        }
    } 
    cout << "False" << endl;
    return 0;
}