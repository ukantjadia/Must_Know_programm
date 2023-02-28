/*
Given an array (or string), the task is to reverse the array/string. 
    
1) Initialize start and end indexes as start = 0, end = n-1 
2) In a loop, swap arr[start] with arr[end] and change start and end as follows : 
start = start +1, end = end – 1
  */ 

#include<iostream>
using namespace std;

void reverse(int arr[], int size_arr)
{
    int start = 0 ,end = size_arr-1;

    while (start < end )
    {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}

void printArray(int arr[],int size_arr)
{
    for (int i =0 ; i < size_arr ; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}


int main()
{
    int arr[] = {12,13,14,15,16,17};
    int size_arr = sizeof(arr)/sizeof(arr[0]);
    printArray(arr,size_arr);
    reverse(arr,size_arr);
    printArray(arr,size_arr);
    return 0;

}
