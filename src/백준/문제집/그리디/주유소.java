import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;

public class 주유소 {
    /** answer
     * 18
     * 10
     * 5
     */
    static int n;
    static long[] dist;
    static long[] cost;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\그리디\\주유소.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int tc = 0; tc < 3; tc ++) {
            n = Integer.parseInt(br.readLine());

            dist = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();
            cost = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();

//            System.out.println(Arrays.toString(dist));
//            System.out.println(Arrays.toString(cost));

            long result = 0L;
            long minCost = cost[0];
            for (int i = 0; i < n-1; i ++) {
                if (minCost > cost[i])
                    minCost = cost[i];
                result += dist[i] * minCost;
            }
            System.out.println(result);
        }
    }
}
