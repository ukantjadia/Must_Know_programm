import java.util.*;

public class recursionSum{
    public int sumNumber(int n){
        if( n == 1)
            return 1;
        else
            return n + sumNumber(n-1);
    }

    public static void main(String args[]){
        Scanner sc  = new Scanner(System.in);
        System.out.println("Enter the limit till sum to be done: ");
        int n = sc.nextInt();
        // sumNumber obj = new sumNumber();
        // int sum = obj.sumnNumber(n);
        System.out.println("The sum of number is : "+sumNumber(n));
    }
}