import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 합이0이되는네정수 {
    /** answer
     * 5
     */

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\투포인터\\합이0이되는네정수.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int tc = 0; tc < 3; tc ++) {
            int n = Integer.parseInt(br.readLine());

            long a[] = new long[n];
            long b[] = new long[n];
            long c[] = new long[n];
            long d[] = new long[n];

            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                a[i] = Long.parseLong(st.nextToken());
                b[i] = Long.parseLong(st.nextToken());
                c[i] = Long.parseLong(st.nextToken());
                d[i] = Long.parseLong(st.nextToken());
            }

            long[] ab = new long[n * n];
            long[] cd = new long[n * n];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    ab[i * n + j] = a[i] + b[j];
                    cd[i * n + j] = c[i] + d[j];
                }
            }
            Arrays.sort(ab);
            Arrays.sort(cd);

            long result = 0;

            int l = 0;
            int r = n * n - 1;
            while (l < n * n && r >= 0) {
                long sum = ab[l] + cd[r];
                if (sum < 0) {
                    l ++;
                } else if (sum > 0) {
                    r --;
                } else {
                    long count_l = 1;
                    long count_r = 1;
                    while (true) {
                        if (l + 1 < n * n && ab[l] == ab[l + 1]) {
                            count_l++;
                            l++;
                        } else {
                            break;
                        }
                    }
                    while (true) {
                        if (r - 1 >= 0 && cd[r] == cd[r - 1]) {
                            count_r++;
                            r--;
                        } else {
                            break;
                        }
                    }
//                System.out.println(count_l + " " + count_r);
                    result += count_l * count_r;
                    l++;
                    r--;
                }
            }

            System.out.println(result);
        }
    }
}