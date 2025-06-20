import java.util.*;

public class q2 {
    static String[] map = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    static void combine(String digits, int i, StringBuilder sb, List<String> res) {
        if (i == digits.length()) {
            res.add(sb.toString());
            return;
        }
        for (char c : map[digits.charAt(i) - '0'].toCharArray()) {
            sb.append(c);
            combine(digits, i + 1, sb, res);
            sb.deleteCharAt(sb.length() - 1);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String digits = sc.next();
        List<String> res = new ArrayList<>();
        if (!digits.isEmpty()) combine(digits, 0, new StringBuilder(), res);
        System.out.println(res);
    }
}
