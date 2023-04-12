package day01;

import java.util.*;

public class MinStack {

    /**
     * 使用辅助栈完成最小值的存取
     * 入栈时将元素压入普通栈，同时将此时辅助栈的栈顶和元素进行比对，较小的压入辅助栈
     * 出栈时，两个一起出栈
     */
    Deque<Integer> stack;
    Deque<Integer> minStack;

    /**
     * initialize your data structure here.
     */
    public MinStack() {
        stack = new LinkedList<>();
        minStack = new LinkedList<>();
        minStack.push(Integer.MAX_VALUE);
    }

    public void push(int x) {
        stack.push(x);
        minStack.push(Math.min(minStack.peek(), x));
    }

    public void pop() {
        stack.pop();
        minStack.pop();

    }

    public int top() {
        return stack.peek();
    }

    public int min() {
        return minStack.peek();
    }
}