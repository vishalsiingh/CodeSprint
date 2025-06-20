
import java.util.*;
class Node{
  int val;
  Node next;
  Node(int v){val=v;}
}
  public class q1{
    public static void main(String[] args){
      Scanner sc=new Scanner(System.in);
      int n =sc.nextInt();
      if(n==0) return ;
      Node head=new Node(sc.nextInt()),temp=head;
      for(int i=1;i<n;i++){
        temp.next=new Node(sc.nextInt());
        temp=temp.next;
      }
      Node curr=head;
      while(curr != null && curr.next != null){
        if(curr.val==curr.next.val)
          curr.next=curr.next.next;
        else
          curr=curr.next;
      }
      while (head !=null){
        System.out.print(head.val + (head.next !=null ? " -> ": ""));
        head=head.next;
      }
      
    }
  }










