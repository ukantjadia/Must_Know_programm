// Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons.
/*Input: arr[] = {3, 5, 4, 1, 9}
Output: Minimum element is: 1
                Maximum element is: 9

Input: arr[] = {22, 14, 8, 17, 35, 3}
Output:  Minimum element is: 3
                Maximum element is: 35*/

# include<iostream>
using namespace std;

struct Pair{
    int min;
    int max;
};

Pair getMinMax(int arr[], int n){
    struct Pair minmax;
    int i;

    if (n == 1 )
    {
        minmax.max = arr[0];
        minmax.min = arr[0];
        return minmax;
    }

    if (arr[0] > arr[1])
    {
        minmax.max = arr[0];
        minmax.min = arr[1];
    }
    else
    {
        minmax.max = arr[1];
        minmax.min = arr[0];
    }

    for(i=2; i<n ; i++)
    {
        if (arr[i] > minmax.max)
            minmax.max = arr[i];
        
        else if (arr[i] < minmax.min)
            minmax.min = arr[i];
    }
    return minmax; 
}

int ownMethod(int arr[], int n)
{
    int min =0,max =0;
    if (n == 1){
        if (arr[0] < arr[1]){
            min = arr[0];
            max = arr[1];
        }
        else
        {
            max = arr[1];
            min = arr[0];
        } 
        cout << " minimux " << min << " " << " maxmum " << max << endl;
    }
    else
    {
        for (int i = 0 ; i < n ; i++ ){
            if ( arr[i] < min )
            {
                min = arr[i];
            }
            else if (arr[i] > max )
            {
                max = arr[i];
            }
        }
        cout << " minimux " << min << " " << " maxmum " << max << endl;
    }

}





int main(){
    int arr[] = {1009,234,45,23,0,6,1};
    int arr2[] = {0,1};
    int arr3[] = {2};
    // int arr4[] = {};
    // int arr_size = sizeof(arr3)/sizeof(int);
    int arr_size = 7;
    // struct Pair minmax = getMinMax(arr3,arr_size);
    ownMethod(arr,arr_size);

    // cout << "Minimun element is : "<<minmax.min << endl;
    // cout << "Maximum element is : "<<minmax.max << endl;
    return 0;
}

