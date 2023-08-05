import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;

public class 잃어버린괄호 {
    /** answer
     * -35
     * 100
     * 0
     */

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\그리디\\잃어버린괄호. txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int tc = 0; tc < 3; tc ++) {
            Queue<Integer> number = new LinkedList<>();
            Queue<Character> operator = new LinkedList<>();

            String line = br.readLine();

            String token = "";
            for (int i = 0; i < line.length(); i++) {
                if (line.charAt(i) >= '0' && line.charAt(i) <= '9') {
                    token += line.charAt(i);
                } else {
                    number.add(Integer.parseInt(token));
                    operator.add(line.charAt(i));
                    token = "";
                }
            }
            if (!token.equals("")) {
                number.add(Integer.parseInt(token));
            }

            int value = number.poll();

            boolean underMinus = false;
            while (!number.isEmpty()) {
//                System.out.print(value);
                int num = number.poll();
                char oper = operator.poll();
                if (oper == '-') {
                    value -= num;
                    underMinus = true;
                } else {
                    if (underMinus) {
                        value -= num;
                    } else {
                        value += num;
                    }
                }
//                System.out.printf(" %s %d = %d\n", oper, num, value);
            }
            System.out.println(value);
        }
    }
}
