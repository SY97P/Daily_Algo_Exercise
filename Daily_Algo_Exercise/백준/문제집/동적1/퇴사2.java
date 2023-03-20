import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 퇴사2 {
    static int n;
    static int[] t;
    static int[] p;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\알분류\\dp\\퇴사.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());

        t = new int[n+2];
        p = new int[n+2];

        dp = new int[n+2];

        for (int i = 1; i <= n; i ++) {
            st = new StringTokenizer(br.readLine());
            t[i] = Integer.parseInt(st.nextToken());
            p[i] = Integer.parseInt(st.nextToken());
        }

        solve();

        System.out.println(dp[n+1]);

        System.out.println(Arrays.toString(dp));
    }

    private static void solve() {
        for (int i = 1; i <= n+1; i++) {
            dp[i] = Math.max(dp[i], dp[i-1]);
            if (i + t[i] <= n + 1) {
                dp[i + t[i]] = Math.max(dp[i + t[i]], dp[i] + p[i]);
            }
        }
    }
}
