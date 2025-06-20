import java.util.Scanner;
public class q1{
  public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
    System.out.print("the numbr of warehouses:");
    int r=sc.nextInt();
    System.out.print("the number of products:");
    int c=sc.nextInt();
    int[][] stock=new int[r][c];
    System.out.println("stock levels:");
    for(int i=0;i<r;i++){
      for(int j=0;j<c;j++){
        stock[i][j]=sc.nextInt();
      }
    }
    int overcount=0;
    for(int i=0;i<r;i++){
      int count=0;
      for(int j=0;j<c;j++){
        if(stock[i][j]>=100){
          count++;
        }
      }
      if (count>=3){
        overcount++;
      }
    }
    System.out.println("The number of Overstocked warehouses" +overcount);
    sc.close();
  }
}