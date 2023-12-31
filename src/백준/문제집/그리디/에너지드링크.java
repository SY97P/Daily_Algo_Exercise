import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class 에너지드링크 {
    /** answer
     * 20
     * 716.5
     */
    static int n;
    static PriorityQueue<Long> drink;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\그리디\\에너지드링크.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        drink = new PriorityQueue<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i ++) {
            drink.add(-1 * Long.parseLong(st.nextToken()));
        }

        double result = -1 * drink.poll();
        while (!drink.isEmpty()) {
            long curr = -1 * drink.poll();
            result = Math.min(result, curr) / 2.0 + Math.max(result, curr);
        }
        System.out.println(result);
    }
}
