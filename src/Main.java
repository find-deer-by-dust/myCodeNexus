import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int min = 99999999;
		int i = 0;
		int[] l = new int[n];
		int p = 0;
		for (i = 0; i < n; i++) {
			l[i] = in.nextInt();
			if (l[i] < min)
				min = l[i];
		}
		for (i = 0; i < n; i++) {
			if (l[i] == min)
				p++;
		}
		System.out.println(n - p);
	}

}
// 4 5 1
// 01000
// 00010
// 00200
// 00001