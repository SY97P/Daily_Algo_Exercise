import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

// 517691607
public class 피보나치수6 {
    final static long P = 1000000007L;

    static long n;
    static long[][] matrix = {{1, 1}, {1, 0}};

    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(
//                new FileReader(
//                        "C:\\Users\\onetu\\IdeaProjects\\Daily_Algo_Exercise\\백준\\단계별\\분할정복\\피보나치수6.txt"
//                )
//        );
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Long.parseLong(br.readLine());

        System.out.println(squareMatrix(n)[1][0] % P);
    }

    private static long[][] squareMatrix(long n) {
        if (n < 2)
            return matrix;
        long[][] rtnMatrix = squareMatrix(n/2);
        if (n % 2 == 0)
            return multiplyMatrix(rtnMatrix, rtnMatrix);
        return multiplyMatrix(multiplyMatrix(rtnMatrix, rtnMatrix), matrix);
    }

    private static long[][] multiplyMatrix(long[][] matA, long[][] matB) {
        long[][] result = new long[2][2];
        for (int i = 0; i < 2; i ++) {
            for (int j = 0; j < 2; j ++) {
                result[i][j] = multiply(matA[i], matB[j]);
            }
        }
        return result;
    }

    private static long multiply(long[] subA, long[] subB) {
        long result = 0L;
        for (int i = 0; i < 2; i ++) {
            result += subA[i] * subB[i];
        }
        return result % P;
    }

    private static void printMatrix(long[][] matrix) {
        for (long[] mat : matrix)
            System.out.println(Arrays.toString(mat));
    }
}
