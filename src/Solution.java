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
        if (pHead==null)
            return null;
        if (pHead.next == null)
            return pHead;

        
        ListNode head = new ListNode(-1);
        head.next = pHead;

        
        pHead=head;
        while (pHead.next != null) {
            if (pHead.val == pHead.next.val) {
                ListNode q = pHead.next;
                while (q.val == pHead.val && q.next != null) {
                    q.val = 0;
                    q = q.next;
                }
                pHead.val = 0;
                pHead = q;
            } 
            else
                pHead = pHead.next;
        }

        pHead=head;
        ListNode tmp=head;
        while(pHead!=null){
            if(pHead.next.val==0){

            }
            else{
                tmp.next=pHead.next; 
                tmp=pHead.next;
            }
            pHead=pHead.next;
        }

        if(head.next==null){
            return null;
        }
            

        return head.next;
    }
}
