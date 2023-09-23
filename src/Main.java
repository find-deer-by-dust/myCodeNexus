
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
	static int p;
	static int[] list;
	static int n;
	static int x;
	static int y;

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int t = in.nextInt();
		int i;
		for (i = 0; i < t; i++) {
			p = 0;
			n = in.nextInt();
			x = in.nextInt();
			int j;
			list = new int[n];
			for (j = 0; j < n; j++) {
				list[j] = in.nextInt();
			}
			y = n / 2;
			if (y * 2 != n)
				y++;
			function(y, x, 0);
			System.out.println(p);
		}
		in.close();
	}

	public static void function(int num, int x, int a) {
		// System.out.println(num + " " + x + " " + a);
		if (num == 0 && x <= 0) {
			// System.out.println(p);
			p++;
		} 
		else if (a < list.length) {
			function(num - 1, x - list[a], a + 1);
			function(num, x, a + 1);
		}
	}
}
// 1 5 10 3 2 3 4 5
// 1 2 5 6 7