import java.util.Scanner;
public class q2{
  public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
    System.out.print("Number of days:");
    int n = sc.nextInt();
    int[] temps=new int[n];
    System.out.println("Temperature readings:");
    for(int i=0;i<n;i++){
      temps[i]=sc.nextInt();
    }
    int count=1;
    int longest=1;
    for(int i=1;i<n;i++){
      if(temps[i]>temps[i-1]){
        count++;
        longest=Math.max(longest,count);
      }else{
        count=1;
      }
    }
    System.out.print("Length of longest increasing Subarray is :"+longest);
    sc.close();
  }
}