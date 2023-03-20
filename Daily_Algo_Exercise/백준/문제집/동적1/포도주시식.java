import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedReader;
import java.util.Arrays;

public class 포도주시식 {
    static int n;
    static int[] wine;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\동적1\\포도주시식.txt"
                )
        );

        n = Integer.parseInt(br.readLine());

        wine = new int[n+1];

        for (int i = 1; i <= n; i ++) {
            wine[i] = Integer.parseInt(br.readLine());
        }

        dp = new int[2][n+1];

        dp[0][1] = dp[1][1] = wine[1];

        solve();

        System.out.println(Math.max(dp[0][n], dp[1][n]));

//        for (int[] d: dp)
//            System.out.println(Arrays.toString(d));
    }

    private static void solve() {
        for (int i = 2; i <= n; i++) {
            dp[0][i] = wine[i] + Math.max(dp[0][i-2], dp[1][i-2]);
            dp[1][i] = Math.max(dp[1][i-1], wine[i] + dp[0][i-1]);
        }
    }
}
