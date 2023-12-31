import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;

public class 서강근육맨 {
    /** answer
     * 5
     */
    static int n;
    static long[] machine;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\그리디\\서강근육맨.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int tc = 0; tc < 1; tc ++) {
            n = Integer.parseInt(br.readLine());

            machine = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();

            Arrays.sort(machine);

            System.out.println(Arrays.toString(machine));

            long result = 0L;
            if (n % 2 == 0) {
                for (int i = 0; i < (int) n / 2 + 1; i++) {
                    result = Math.max(result, machine[i] + machine[n - 1 - i]);
                    System.out.println(machine[i] + " " + machine[n - 1 - i]);
                }
            } else {
                result = Math.max(result, machine[n - 1]);
                for (int i = 0; i < (int) n / 2; i++) {
                    result = Math.max(result, machine[i] + machine[n - 2 - i]);
                    System.out.println(machine[i] + " " + machine[n - 2 - i]);
                }
            }
            System.out.println(result);
        }
    }
}
