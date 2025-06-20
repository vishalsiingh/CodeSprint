import java.util.Scanner;
public class q2{
  public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();
    int count=0;
    if (n>10){
      System.out.println("Abhik's Marathon journey intensifies! lets's see his detailed zig-zag pattern :");
    }
    for(int day=1;day<n;day++){
    int numcount=day;

    int maxwidth=(n-1)*4;
      int currentwidth=(numcount-1)*4;
      int spaces=(maxwidth-currentwidth)/2;
    for(int s=0;s<spaces;s++){
      System.out.print(" ");
    }if(day%2==1){
      for(int i=1;i<=day;i++){
        System.out.print(i);
        count++;
        if(i!=day) System.out.print("   ");
      }
      
    }else{
      for (int i=day;i>=1;i--){
        System.out.print(i);
        count++;
        if(i!=1) System.out.print("   ");
      }
    }
    System.out.println();
  }
  System.out.println("Total numbers printed" + count);
}
}