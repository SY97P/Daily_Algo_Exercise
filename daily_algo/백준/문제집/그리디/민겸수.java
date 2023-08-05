import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;

public class 민겸수 {
    /** answer
     * 5000000000005555555555
     * 1000000000055555555555
     *
     * 55011
     * 51510
     *
     * 501
     * 151
     *
     * 50550
     * 155105
     */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\그리디\\민겸수.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int tc = 0; tc < 4; tc ++) {
            String[] line = br.readLine().split("");

            String minValue = "";
            String maxValue = "";

            int count = 0;
            for (int i = 0; i < line.length; i ++) {
                if (line[i].equals("M")) {
                    count ++;
                } else {
                    // M이 하나라도 있었으면
                    if (count > 0) {
                        long value = (long) Math.pow(10, count);
                        minValue += Long.toString(value + 5);
                        maxValue += Long.toString(value * 5);
                    } else {
                        minValue += "5";
                        maxValue += "5";
                    }
                    count = 0;
                }
            }
            if (count > 0) {
                long value = (long) Math.pow(10, count - 1);
                minValue += Long.toString(value);
                for (int k = 0; k < count; k ++) {
                    maxValue += "1";
                }
            }

            System.out.println(maxValue);
            System.out.println(minValue);
        }
    }
}