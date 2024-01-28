package 프로그래머스.lv3;

import java.util.Arrays;

/**
 * 문제요약<br>
 *<br>
 * 권투선수는 각자 1 ~ n 번호<br>
 * 실력이 좋은 선수가 반드시 이김<br>
 * 주어진 경기 결과를 바탕으로 정확하게 순위를 매길 수 있는 선수의 수 구하기<br>
 *<br>
 * 제한사항<br>
 *<br>
 * 1 <= 선수 수 <= 100<br>
 * 1 <= 경기결과 수 <= 4_500<br>
 * [A, B] : A 선수가 B 선수 이김<br>
 * 모든 경기 결과에는 모순이 없음<br>
 *<br>
 * 해결전략 (플로이드 와샬)<br>
 *<br>
 * 모든 경기 결과를 2차원 배열에 기록<br>
 * 플로이드 와샬 알고리즘으로 순위 분석<br>
 *  [i][j] : [i][k] && [k][j]<br>
 *  i가 j 를 이기려면 i 는 k 에 이겨야 하고, k 도 j 를 이겨야 함<br>
 *
 */

public class 순위 {

    private static class Solution {

        private static final int SELF = 2;
        private static final int WIN = 1;
        private static final int LOSE = -1;
        private static final int NO_INFO = 0;

        public int solution(int n, int[][] results) {
            int[][] dp = new int[n + 1][n + 1];

            for (int i = 1; i <= n; i ++) {
                dp[i][i] = SELF;
            }
            for (int[] result : results) {
                dp[result[0]][result[1]] = WIN;
                dp[result[1]][result[0]] = LOSE;
            }

            for (int k = 1; k <= n; k ++) {
                for (int i = 1; i <= n; i ++) {
                    for (int j = 1; j <= n; j ++) {
                        if (i == j) {
                            continue;
                        }

                        if (dp[i][k] == WIN && dp[k][j] == WIN) {
                            dp[i][j] = WIN;
                        } else if (dp[i][k] == LOSE && dp[k][j] == LOSE) {
                            dp[i][j] = LOSE;
                        }
                    }
                }
            }

            return (int) Arrays.stream(dp)
                    .filter(array -> {
                        long count = Arrays.stream(array)
                                .filter(a -> a != NO_INFO)
                                .count();
                        return count == n;
                    })
                    .count();
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 2
        int solution1 = solution.solution(5, new int[][]{new int[]{4, 3}, new int[]{4, 2}, new int[]{3, 2}, new int[]{1, 2}, new int[]{2, 5}});
        System.out.println("solution = " + solution1);

        // 1
        int solution2 = solution.solution(4, new int[][]{new int[]{1, 2}, new int[]{2, 3}, new int[]{1, 4}});
        System.out.println("solution = " + solution2);

    }

}
