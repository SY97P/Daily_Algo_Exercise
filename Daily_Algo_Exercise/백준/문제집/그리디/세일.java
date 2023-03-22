import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;

public class 세일 {
    /** answer
     * 8
     * 21
     */
    static int n;
    static Integer[] cost;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\그리디\\세일.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int tc = 0; tc < 2; tc ++) {
            n = Integer.parseInt(br.readLine());

            int[] temp = new int[n];

            for (int i = 0; i < n; i++) {
                temp[i] = Integer.parseInt(br.readLine());
            }

            cost = Arrays.stream(temp).boxed().toArray(Integer[]::new);
            Arrays.sort(cost, Comparator.reverseOrder());

            System.out.println(Arrays.toString(cost));

            int count = 0;
            int result = 0;
            for (int i = 0; i < n; i++) {
                if (count >= 2) {
                    count = 0;
                    continue;
                }
                count++;
                result += cost[i];
            }

            System.out.println(result);
        }
    }
}
