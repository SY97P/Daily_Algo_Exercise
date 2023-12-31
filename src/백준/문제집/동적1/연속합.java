import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 연속합 {
    static int n;
    static int[] alist;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\동적1\\연속합.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        alist = new int[n + 1];
        dp = new int[n + 1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            alist[i] = Integer.parseInt(st.nextToken());
        }

        continuousSum();

        int result = Integer.MIN_VALUE;
        for (int i = 1; i <= n; i ++) {
            result = Math.max(result, dp[i]);
        }
        System.out.println(result);

//      printDP();
    }

    private static void continuousSum() {
        for (int i = 1; i <= n; i++) {
            dp[i] = Math.max(dp[i - 1] + alist[i], alist[i]);
        }
    }

    private static void printDP() {
        for (int a: alist)
            System.out.print(a + " ");
        System.out.println();
        for (int d: dp)
            System.out.print(d + " ");
        System.out.println();
    }
}
