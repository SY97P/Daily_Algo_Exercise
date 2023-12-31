import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 가장큰증가하는부분수열 {
    // answer : 113

    static int n;
    static int[] alist;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\동적1\\가장큰증가하는부분수열.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        alist = new int[n+1];
        dp = new int[n+1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i =1; i <= n; i++) {
            alist[i] = Integer.parseInt(st.nextToken());
        }

        lbis();

        int result = 0;
        for (int i =1; i <= n; i++) {
            result = Math.max(result, dp[i]);
        }
        System.out.println(result);

//        printDP();
    }

    private static void lbis() {
        for (int i =1; i <= n; i++) {
            for (int j =0; j < i ; j++) {
                if (alist[i] > alist[j]) {
                    dp[i] = Math.max(dp[i], alist[i] + dp[j]);
                }
            }
        }
    }

    private static void printDP() {
        for (int a: alist) {
            System.out.print(a + " ");
        }
        System.out.println();
        for (int d: dp) {
            System.out.print(d + " ");
        }
        System.out.println();
    }
}
