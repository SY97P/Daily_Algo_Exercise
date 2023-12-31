import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;

public class 쉬운계단수 {
    final static int BOUND = 1000000000;
    static int n;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new InputStreamReader(
                        System.in
                )
        );

        n = Integer.parseInt(br.readLine());

        dp = new int[n + 1][11];

        for (int i = 1; i <= 9; i++) {
            dp[1][i] = 1;
        }

        solve();

        System.out.println(Arrays.stream(dp[n]).sum() % BOUND);

//        for (int[] d: dp)
//            System.out.println(Arrays.toString(d));
    }

    private static void solve() {
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j <= 9; j++) {
                if (j == 0)
                    dp[i][j] = dp[i - 1][j + 1];
                else
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1];
            }
        }
    }
}
