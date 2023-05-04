
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {
		Solution s = new Solution();
		ArrayList<String> x = s.Permutation("aooo");

		for (String words : x) {
			System.out.println(words);
		}
	}

}
