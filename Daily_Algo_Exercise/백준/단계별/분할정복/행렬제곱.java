import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class 행렬제곱 {
    final static int MODULER = 1000;

    static int n;
    static long b;
    static int[][] matrix;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "C:\\Users\\onetu\\IdeaProjects\\Daily_Algo_Exercise\\백준\\단계별\\분할정복\\행렬제곱.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] line = br.readLine().split(" ");
        n = Integer.parseInt(line[0]);
        b = Long.parseLong(line[1]);

        matrix = new int[n][n];

        for (int i = 0; i < n; i++) {
            line = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                matrix[i][j] = Integer.parseInt(line[j]) % MODULER;
            }
        }

        printMatrix(squareMatrix(b));
    }

    private static int[][] squareMatrix(long b) {
        if (b <= 1)
            return matrix;
        int[][] rtnMatrix = squareMatrix(b/2);
        if (b%2 == 0)
            return multiplyMatrix(rtnMatrix, rtnMatrix);
        return multiplyMatrix(multiplyMatrix(rtnMatrix, rtnMatrix), matrix);
    }

    private static int[][] multiplyMatrix(int[][] mat_a, int[][] matrix_b) {
        int[][] mat_b = reverseMatrix(matrix_b);
        int[][] result = new int[n][n];
        for (int i =0; i < n; i ++) {
            for (int j = 0; j < n; j++) {
                result[i][j] = multiply(mat_a[i], mat_b[j]);
            }
        }
        return result;
    }

    private static int[][] reverseMatrix(int[][] matrix) {
        int[][] result = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                result[i][j] = matrix[j][i];
            }
        }
        return result;
    }

    private static int multiply(int[] sub_a, int[] sub_b) {
        int result = 0;
        for (int i = 0; i < n; i ++) {
            result += sub_a[i] * sub_b[i];
        }
        return result % MODULER;
    }

    private static void printMatrix(int[][] matrix) {
        for (int i =0; i < n; i++) {
            for (int j=0; j < n; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}
