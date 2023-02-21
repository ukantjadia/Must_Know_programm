#include<iostream>
#include<cmath>

using namespace std;

int main()
{
    int exp, result;
    cout << "Enter exponent ";
    cin >> exp;

    result = pow(2,exp);

    int sum = 0.0;
    while(result > 0)
    {
        sum += result%10;
        result /= 10;
    }    

    cout << sum << endl;


    return 0;
    


}