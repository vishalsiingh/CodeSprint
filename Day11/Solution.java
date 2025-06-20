import java.util.Scanner;

class ListNode {
    int val;
    ListNode next;
    ListNode(int v) { val = v; }
}

public class Solution {
    public static boolean detectAndRemoveLoop(ListNode head) {
        if (head == null) return true;

        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                slow = head;
                if (fast == head) {
                    while (fast.next != head) fast = fast.next;
                } else {
                    while (slow.next != fast.next) {
                        slow = slow.next;
                        fast = fast.next;
                    }
                }
                fast.next = null;
                return true;
            }
        }
        return true;
    }

    public static ListNode createLinkedList(int[] arr, int pos) {
        if (arr.length == 0) return null;
        ListNode head = new ListNode(arr[0]), curr = head, loopNode = null;
        for (int i = 1; i < arr.length; i++) {
            curr.next = new ListNode(arr[i]);
            curr = curr.next;
            if (i == pos - 1) loopNode = curr;
        }
        if (pos > 0) curr.next = loopNode;
        return head;
    }

    public static void printList(ListNode head) {
        ListNode curr = head;
        while (curr != null) {
            System.out.print(curr.val);
            curr = curr.next;
            if (curr != null) System.out.print(" -> ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter node values: ");
        String[] input = sc.nextLine().split(" ");
        int[] arr = new int[input.length];
        for (int i = 0; i < input.length; i++) arr[i] = Integer.parseInt(input[i]);
        System.out.print("Enter loop position (0 if no loop): ");
        int pos = sc.nextInt();

        ListNode head = createLinkedList(arr, pos);
        detectAndRemoveLoop(head);

        System.out.print("Linked list after removal: ");
        printList(head);
        sc.close();
    }
}
