import java.io.FileReader;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class 가장긴짝수연속한부분수열small {
    static int n;
    static int k;
    static int[] alist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\동적1\\가장긴짝수연속한부분수열(smal).txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        alist = new int[n+1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            alist[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(solve());
    }

    private static int solve() {
        int result = 0;
        for (int i = 1; i <= n; i ++) {
            if (alist[i] % 2 == 0) {
                int count = 1;
                int odd_count = 0;
                // 현재까지 지나온 홀수가 k개 미만일 때만 연산
                for (int j = i - 1; j > 0 && odd_count <= k; j --) {
                    // 이전 수가 짝수라면 count를 증가
                    if (alist[j] % 2 == 0) {
                        count ++;
                    }
                    // 이전 수가 홀수라면 odd_count를 증가
                    else {
                        odd_count ++;
                    }
                }
                result = Math.max(result, count);
            }
        }
        return result;
    }
}