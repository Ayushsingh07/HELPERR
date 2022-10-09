public class SieveOfEratosthenes {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 25;
		SOE(n);

	}
	public static void SOE(int n)
	{
		boolean[] multiple = new boolean[n+1];
		for(int i = 2 ; i <= n ; i++) {
		multiple[i] = true;
		}
		for(int factor = 2; factor*factor <= n; factor++)
		{
			if(multiple[factor]) {
				for(int mult = 2; mult*factor<=n;mult++)
				{
					multiple[mult*factor] = false;
					
				}
			}
			
		}
		for(int i = 0 ; i <= n ; i++)
		{
			if(multiple[i]) {
				System.out.print(i + " ");
			}
		}
	}

}
// Output
// 2 3 5 7 11 13 17 19 23 
