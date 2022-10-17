import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        // write ur code here
        int n=scn.nextInt();
        
        for(int x=1;x<=10;x++)
        {
            System.out.println(n+" * "+x+" = "+(n*x));
        }

    }
}