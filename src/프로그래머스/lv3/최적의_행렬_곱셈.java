package 프로그래머스.lv3;

/**
 * 문제요약<br>
 * <br>
 * (a by b) * (b by c) = a * b * c 번 연산<br>
 * 모든 행렬 곱을 구하기 위한 최소 곱셈 연산 수 구하기<br>
 * <br>
 * 제한사항<br>
 * <br>
 * 3 <= 행렬 개수 <= 200<br>
 * 1 <= 행, 열 크기 <= 200<br>
 * 계산 불가한 행렬은 주어지지 않음<br>
 * <br>
 * 해결전략<br>
 * <br>
 * DP<br>
 * dp[i][j] = dp[i][k] + dp[k][j] + cal(i, k, j)<br>
 * 행렬 크기 기록하는 DP 배열<br>
 * 최소 곱셈 연산 수 기록 DP 배열<br>
 *
 */

public class 최적의_행렬_곱셈 {

    private static class Solution {
        public int solution(int[][] matrix_sizes) {
            int n = matrix_sizes.length;

            int[][] dp = new int[n][n];
            int[][][] size = new int[n][n][2];

            for (int i = 0; i < n; i ++) {
                for (int j = i; j < n; j++) {
                    size[i][j] = new int[]{matrix_sizes[i][0], matrix_sizes[j][1]};
                    if (i != j) {
                        dp[i][j] = Integer.MAX_VALUE;
                    }
                }
            }

            for (int step = 1; step < n; step ++) {
                for (int i = 0; i < n - step; i ++) {
                    int j = i + step;
                    for (int k = i; k < j; k ++) {
                        dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k + 1][j] + multiply(i, j, k, size));
                    }
                }
            }

            return dp[0][n - 1];
        }

        private int multiply(int i, int j, int k, int[][][] size) {
            int[] matrixA = size[i][k];
            int[] matrixB = size[k + 1][j];
            return matrixA[0] * matrixB[0] * matrixB[1];
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 270
        int solution1 = solution.solution(new int[][]{new int[]{5, 3}, new int[]{3, 10}, new int[]{10, 6}});
        System.out.println("solution1 = " + solution1);

    }

}
