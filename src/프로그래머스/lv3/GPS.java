package 프로그래머스.lv3;

/**
 * 문제요약
 * <p>
 * 택시는 거점 간 도로가 있는 경우에만 이동<p>
 * 이미 지난 거점을 재방문 가능<p>
 * 모든 도로는 양방향 통행 가능<p>
 * 오류가 있는 경로를 최소한으로 수정하여 이동 가능한 경로로 만들때 수정 횟수 구하기<p>
 * 올바른 경로로 수정이 불가한 경우엔 -1 반환<p>
 * <p><p>
 * 제한사항<p>
 * <p><p>
 * 2 <= 거점 수 <= 200<p>
 * 1 <= 도로 수 <= 10^4<p>
 * 2 <= 경로 상 거점 수 <= 100<p>
 * 도로정보 : [A, B]<p>
 * 거점 번호는 1부터 n 까지 숫자<p>
 * 모든 도로는 양방향 통행<p>
 * 시작, 도착 거점은 변경 불가<p>
 * <p><p>
 * 해결전략<p>
 * <p><p>
 * DP<p>
 * dp[i][j] : i 번 경로에서 j 거점에 있을때의 최소 수정 횟수<p>
 * dp[i][j] = min(self, dp[i-1][n] + 1(경로가 없으면) / 0(경로가 있으면))<p>
 * <p>
 *
 */

public class GPS {

    private static class Solution {

        public int solution(int n, int m, int[][] edge_list, int k, int[] gps_log) {
            boolean[][] adj = getAdj(n, edge_list);
            int[][] dp = getDp(n, k, gps_log);

            for (int time = 1; time <= k; time++) {
                for (int currPoint = 1; currPoint <= n; currPoint++) {
                    for (int prevPoint = 1; prevPoint <= n; prevPoint++) {
                        if (adj[currPoint][prevPoint]) {
                            dp[time][currPoint] = Math.min(dp[time][currPoint], dp[time - 1][prevPoint]);
                        }
                    }

                    if (currPoint != gps_log[time - 1]) {
                        dp[time][currPoint]++;
                    }
                }
            }

            int answer = dp[k][gps_log[k - 1]];
            if (answer >= k) {
                return -1;
            }
            return answer;
        }

        private int[][] getDp(int n, int k, int[] gpsLog) {
            int[][] dp = new int[k + 1][n + 1];

            for (int i = 0; i <= k; i++) {
                for (int j = 0; j <= n; j++) {
                    dp[i][j] = k + 1;
                }
            }

            dp[1][gpsLog[0]] = 0;

            return dp;
        }

        private boolean[][] getAdj(int n, int[][] edge_list) {
            boolean[][] adj = new boolean[n + 1][n + 1];
            for (int[] edge : edge_list) {
                int u = edge[0];
                int v = edge[1];

                adj[u][v] = true;
                adj[v][u] = true;
            }
            return adj;
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // 1
        int answer1 = s.solution(7, 10,
                new int[][]{new int[]{1, 2}, new int[]{1, 3}, new int[]{2, 3}, new int[]{2, 4}, new int[]{3, 4},
                        new int[]{3, 5}, new int[]{4, 6}, new int[]{5, 6}, new int[]{5, 7}, new int[]{6, 7}}, 6,
                new int[]{1, 2, 3, 3, 6, 7});
        System.out.println("answer = " + answer1);

        // 0
        int answer2 = s.solution(7, 10,
                new int[][]{new int[]{1, 2}, new int[]{1, 3}, new int[]{2, 3}, new int[]{2, 4}, new int[]{3, 4},
                        new int[]{3, 5}, new int[]{4, 6}, new int[]{5, 6}, new int[]{5, 7}, new int[]{6, 7}}, 6,
                new int[]{1, 2, 3, 5, 6, 7});
        System.out.println("answer = " + answer2);

    }

}
