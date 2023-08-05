import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

// ((110(0101))(0010)1(0001))

public class 쿼드트리 {
    static boolean LOG = true;

    static int n;
    static int[][] matrix;

    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(
//            new FileReader(
//                    "C:\\Users\\onetu\\IdeaProjects\\Daily_Algo_Exercise\\백준\\단계별\\분할정복\\쿼드트리.txt"
//            )
//        );
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        matrix = new int[n][n];

        for (int i=0; i < n; i ++) {
            String[] line = br.readLine().split("");
            for (int j=0; j < n; j++) {
                matrix[i][j] = Integer.parseInt(line[j]);
            }
        }

        if (LOG) {
            for (int[] mat: matrix)
                System.out.println(Arrays.toString(mat));
        }

        quadTree(n, 0, n, 0);
        System.out.println();
    }

    private static void quadTree(int i_length, int i_start, int j_length, int j_start) {
        if (i_length <= 1 || j_length <= 1) {
            System.out.print(matrix[i_start][j_start]);
            return;
        }

        int onlyOne = checkColor(i_length, i_start, j_length, j_start);

        if (onlyOne >= 0)
            System.out.print(onlyOne);
        else {
            System.out.print("(");

            int next_i_length = (int) i_length/2;
            int next_j_length = (int) j_length/2;
            int odd_i_length = i_length%2==0 ? next_i_length : next_i_length+1;
            int odd_j_length = j_length%2==0 ? next_j_length : next_j_length+1;

            quadTree(next_i_length, i_start, next_j_length, j_start);
            quadTree(next_i_length, i_start, odd_j_length, j_start+next_j_length);
            quadTree(odd_i_length, i_start+next_i_length, next_j_length, j_start);
            quadTree(odd_i_length, i_start+next_i_length, odd_j_length, j_start+next_j_length);

            System.out.print(")");
        }
    }

    private static int checkColor(int i_length, int i_start, int j_length, int j_start) {
        int color = matrix[i_start][j_start];
        for (int i = 0; i < i_length; i ++) {
            for (int j = 0; j < j_length; j ++) {
                if (matrix[i+i_start][j+j_start] != color)
                    return -1;
            }
        }
        return color;
    }
}
