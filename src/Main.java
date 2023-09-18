
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int[] list;
	static int m;
	static int p = 0;

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		m = in.nextInt();
		int n = in.nextInt();
		int i;
		list = new int[n];
		for (i = 0; i < n; i++) {
			list[i] = in.nextInt();
		}
		function(0, m);
		System.out.println(p);
	}

	static void function(int a, int b) {
		if (b == 0) {
			p++;
		}
		System.out.println(a);
		System.out.println(b);
		if (a+1<list.length) {
			function(a + 1, b - list[a]);
			function(a + 1, b);
		}
	}
}