package day02;

public class ListReverse {
    public ListNode reverseList(ListNode head) {
        //采用原地逆置的方法对链表进行逆置
        ListNode preNode = null, curNode = head, nextNode = null;
        while (curNode != null) {
            nextNode = curNode.next;
            curNode.next = preNode;
            preNode = curNode;
            curNode = nextNode;
        }
        return preNode;
    }
}
