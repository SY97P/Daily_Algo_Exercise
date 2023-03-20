import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 징검다리건너기small {
    /** answer
     * YES
     * NO
     */
    static int n;
    static int k;
    static int[] alist;
    static boolean[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\동적1\\징검다리건너기small.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        alist = new int[n];
        dp = new boolean[n];

        dp[0] = true;

        st = new StringTokenizer(br.readLine());
        for (int i = 0 ;i < n; i ++) {
            alist[i] = Integer.parseInt(st.nextToken());
        }

        solve();

        System.out.println(dp[n-1] ? "YES" : "NO");

//        System.out.println(Arrays.toString(dp));
    }

    private static void solve() {
        for (int i = 0; i < n; i ++) {
            if (dp[i]) {
                for (int j = 1; j < n - i; j++) {
                    int energy = j * (1 + Math.abs(alist[i + j] - alist[i]));
                    if (energy <= k)
                        dp[i+j] = true;
                }
            }
        }
    }
}
