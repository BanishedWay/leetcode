package day01;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Stack;

public class CQueue<T> {

    //使用两个栈实现队列

    Deque<T> inStack, outStack;

    public CQueue() {
        inStack = new ArrayDeque<>();
        outStack = new ArrayDeque<>();
    }

    public void appendTail(T value) {
        this.push(value);
    }

    public T deleteHead() {
        return this.pop();
    }

    //进栈时将元素压入输入栈
    public void push(T value) {
        inStack.push(value);
    }

    /*
    出栈时先判断输出栈是否为空
    * 不为空则输出栈顶
    为空则将输入栈输出到输出栈中，然后输出栈顶
    */
    public T pop() {
        if (outStack.isEmpty()) {
            if (inStack.isEmpty()) {
                System.out.println("ERROR!\nCQueue is empty!");
                System.exit(0);
            }
            while (!inStack.isEmpty()) {
                outStack.push(inStack.pop());
            }
        }
        return outStack.pop();
    }
}
