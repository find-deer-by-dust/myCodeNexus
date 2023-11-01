import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {

	public static void main(String[] args) {
		Solution s = new Solution();
		ListNode a = new ListNode(1);
		ListNode b = new ListNode(1);
		a.next = b;
		ListNode x = s.deleteDuplication(a);
		while (x != null) {
			System.out.println(x.val);
			x = x.next;
		}

	}

}
