
import java.util.Scanner;

public class q1 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter total number of hours:");
        int n = sc.nextInt();

        int[] vehicles = new int[n];
        System.out.print("Enter the number of vehicles for each hour:");
        for (int i = 0; i < n; i++) {
            vehicles[i] = sc.nextInt();
        }

        int count = 0;
        for (int i = 1; i < n; i++) {
            if (vehicles[i] >= 50 && vehicles[i] > vehicles[i - 1]) {
                count++;
            }
        }

        System.out.println(" Total Critical jam hours: " + count);
        sc.close();
    }
}
