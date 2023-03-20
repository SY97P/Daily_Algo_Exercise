import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;

public class 동전2 {
    static int n;
    static int k;
    static int[] coins;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\동적1\\동전2.txt"
                )
        );

        String[] line = br.readLine().split(" ");

        n = Integer.parseInt(line[0]);
        k = Integer.parseInt(line[1]);

        coins = new int[n+1];

        dp = new int[n+1][k+1];

        for (int i = 1; i <= n; i ++) {
            coins[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= k; j ++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k; j ++) {
                if (j % coins[i] == 0) {
                    dp[i][j] = j / coins[i];
                }
            }
        }

//        for (int[] d: dp)
//            System.out.println(Arrays.toString(d));

        solve();

        System.out.println(dp[n][k]);

//        for (int[] d: dp)
//            System.out.println(Arrays.toString(d));
    }

    private static void solve() {
        for (int j = 1; j <= k; j ++) {
            for (int i = 1; i <= n; i++) {
                if (j - coins[i] >= 0 && dp[i-1][j-coins[i]] != Integer.MAX_VALUE) {
                    dp[i][j] = Math.min(dp[i][j], dp[i-1][j - coins[i]] + 1);
                }
                if (dp[i][j] < dp[i-1][j])
                    dp[i-1][j] = dp[i][j];
                else
                    dp[i][j] = dp[i-1][j];
            }
        }
    }
}
