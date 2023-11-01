import java.util.*;

/*
 public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}
*/
public class Solution {
    public ListNode deleteDuplication(ListNode pHead) {
        if (pHead == null)
            return null;
        if (pHead.next == null)
            return pHead;

        ListNode head = new ListNode(-1);
        head.next = pHead;
        ListNode p = head.next;
        int tag = head.val;
        while (p != null) {
            if (p.val != tag) {
                tag = p.val;
            } else {
                p.val = -1;
            }
        }
        p = head.next;
        while (p.next != null) {
            if (p.next.val == -1) {
                p.val = -1;
            }
        }

        return head.next;
    }
}
