package 프로그래머스.lv3;

/**
 * 문제요약
 *
 * 무지와 어피치의 택시 합승 시 최저요금 구하기
 * 중복되지 않는 양방향 간선
 * 최종 비용 = 모든 간선 비용 합
 * 출발지점 s 에서 시작해 a, b 각 구간으로 이동하는데 최종적으로 발생하는 택시 요금을 최소로 구하기
 *
 * 제한사항
 *
 * 3 <= 지점 수 <= 200
 * 1 <= 지점 번호 <= n
 * s, a, b 는 모두 다른 지점
 * 요금정보(간선정보) : [지점번호1, 지점번호2, 요금]
 * 1 <= 요금 <= 10^5
 * 모두 도착할 수 있는 경우만 주어짐
 *
 * 해결전략 (플로이드-와샬)
 *
 * 모든 지점 간의 최단비용을 구할 수 있는 2차원 배열
 * 플로이드 와샬 알고리즘 적용
 * 모든 지점을 합승 마무리 구간(경유지)로 고려했을때 발생하는 최종비용 비교 후 최소값 반환
 */

public class 합승_택시_요금 {

    private static class Solution {

        private static final int MAX_COST = 200 * 100_000 + 1;

        private int[][] dp;

        public int solution(int n, int s, int a, int b, int[][] fares) {
            initDp(n, fares);

            floydWarshar(n);

            int answer = Integer.MAX_VALUE;
            for (int waypoint = 1; waypoint <= n; waypoint ++) {
                int cost = dp[s][waypoint] + dp[waypoint][a] + dp[waypoint][b];
                answer = Math.min(answer, cost);
            }

            return answer;
        }

        private void floydWarshar(int n) {
            for (int k = 1; k <= n; k ++) {
                for (int i = 1; i <= n; i ++) {
                    for (int j = 1; j <= n; j ++) {
                        dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k][j]);
                    }
                }
            }
        }

        private void initDp(int n, int[][] fares) {
            dp = new int[n + 1][n + 1];

            for (int i = 0; i <= n; i ++) {
                for (int j = 0; j <= n; j ++) {
                    if (i == j) {
                        continue;
                    }
                    dp[i][j] = MAX_COST;
                }
            }
            for (int[] fare : fares) {
                int u = fare[0], v = fare[1], c = fare[2];
                dp[u][v] = c;
                dp[v][u] = c;
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 82
        int solution1 = solution.solution(6, 4, 6, 2, new int[][]{new int[]{4, 1, 10}, new int[]{3, 5, 24}, new int[]{5, 6, 2}, new int[]{3, 1, 41}, new int[]{5, 1, 24}, new int[]{4, 6, 50}, new int[]{2, 4, 66}, new int[]{2, 3, 22}, new int[]{1, 6, 25}});
        System.out.println("solution1 = " + solution1);

        // 14
        int solution2 = solution.solution(7, 3, 4, 1, new int[][]{new int[]{5, 7, 9}, new int[]{4, 6, 4}, new int[]{3, 6, 1}, new int[]{3, 2, 3}, new int[]{2, 1, 6}});
        System.out.println("solution2 = " + solution2);

        // 18
        int solution3 = solution.solution(6, 4, 5, 6, new int[][]{new int[]{2, 6, 6}, new int[]{6, 3, 7}, new int[]{4, 6, 7}, new int[]{6, 5, 11}, new int[]{2, 5, 12}, new int[]{5, 3, 20}, new int[]{2, 4, 8}, new int[]{4, 3, 9}});
        System.out.println("solution3 = " + solution3);

    }

}
