package day02;


import java.util.HashMap;
import java.util.Map;

class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}

public class RandomList {
    Map<Node, Node> map = new HashMap<>();

    public Node copyRandomList(Node head) {
        //使用哈希表存储每个结点的副本，只要有一个结点未被创建，则递归创建该结点
        if (head == null) {
            return null;
        }
        if (!map.containsKey(head)) {
            Node headNew = new Node(head.val);
            map.put(head, headNew);
            //递归检查结点是否存在
            headNew.next = copyRandomList(head.next);
            headNew.random = copyRandomList(head.random);
        }
        return map.get(head);
    }
}
