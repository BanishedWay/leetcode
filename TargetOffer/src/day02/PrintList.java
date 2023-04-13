package day02;

import java.util.Stack;

public class PrintList {
    //使用辅助栈存储链表的值
    public int[] reversePrint(ListNode head) {
        Stack<ListNode> stack = new Stack<>();
        ListNode tmp = head;
        while (tmp != null) {
            stack.push(tmp);
            tmp = tmp.next;
        }//将元素依次压入栈
        int[] res = new int[stack.size()];
        int size=stack.size();
        for (int i = 0; i < size; i++) {
            res[i] = stack.pop().val;
        }
        return res;
    }
}
