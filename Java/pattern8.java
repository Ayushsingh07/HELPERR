import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        // write ur code here
        int n=scn.nextInt();
        for(int x=1;x<=n;x++)
        {
            for(int y=1;y<=n;y++)
            {
                if(x+y==(n+1))
                System.out.print("*\t");
                else System.out.print("\t");
            }
            System.out.println();
        }

    }
}