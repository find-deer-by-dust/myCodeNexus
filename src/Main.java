
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Solution s = new Solution();
		String a = "ababaaa";
		String b = "aa";
		a.indexOf(b);
		System.out.println(s.kmp(a, b));
		System.out.println(a.indexOf(b));
	}

}
