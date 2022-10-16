import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        // write ur code here
        
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        
        for(int x=n;x>=1;x--)
        {
            for(int y=n-1;y>=x;y--)
            System.out.print("\t");
            for(int y=1;y<=x;y++)
            System.out.print("*\t");
            
            System.out.println();
        }

    }
}