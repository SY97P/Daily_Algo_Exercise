package 프로그래머스.lv3;

import java.util.Objects;
import java.util.PriorityQueue;

/**
 * 문제요약 <br>
 *<br>
 * N*N 경주로 부지<br>
 * 0 : 빈 칸 / 1 : 벽 칸<br>
 * (0, 0) 에서 출발해 (n-1, n-1) 까지 중간에 끊기지 않고 도달해야함.<br>
 * 상하좌우면서 빈 칸인 곳으로 경주로 건설 가능<br>
 * 직선도로 = 상하 or 좌우 -> 100원 소요<br>
 * 코너도로 = 직각으로 만남 -> 500원 소요<br>
 * 경주로 건설에 필요한 최소 비용 구하기<br>
 *<br>
 * 제한사항<br>
 *<br>
 * 3 <= 경주로 부지 한 변의 크기 <= 25<br>
 * 경주로를 건설할 수 있는 형태로 경주로 부지 주어짐<br>
 * 출발지, 도착지는 반드시 빈 칸<br>
 *<br>
 * 해결전략 (다익스트라)<br>
 *<br>
 * 우선순위 큐 만들고<br>
 * 노드 정보 만들고 [비용, x좌표, y좌표, 방향]<br>
 * DP 만들고 [n][n][4];<br>
 * 방향 : 0(상), 1(좌), 2(하), 3(우)<br>
 * 직선도로 : 두 방향 더해서 짝수<br>
 * 코너도로 : 두 방향 더해서 홀수<br>
 *
 */

public class 경주로_건설 {

    private static class Solution {

        private static final int STRAIGHT_COST = 100;
        private static final int CURVED_COST = 500;
        private static final int DIRECT_BOUND = 4;
        private static final int[] dx = {-1, 0, 1, 0};
        private static final int[] dy = {0, -1, 0, 1};

        private int n;

        public int solution(int[][] board) {
            n = board.length;

            return dijkstra(board);
        }

        private int dijkstra(int[][] board) {
            int[][][] dp = initDp();

            PriorityQueue<Node> q = new PriorityQueue<>();
            q.add(new Node(0, 0, 0, 2));
            q.add(new Node(0, 0, 0, 3));

            while (!q.isEmpty()) {
                Node node = q.poll();

                if (node.cost > dp[node.x][node.y][node.direction] || node.x == n - 1 && node.y == n - 1) {
                    continue;
                }

                for (int nextDirection = 0; nextDirection < DIRECT_BOUND; nextDirection ++) {
                    int nx = node.x + dx[nextDirection];
                    int ny = node.y + dy[nextDirection];

                    if (nx < 0 || nx >= n || ny < 0 || ny >= n || board[nx][ny] == 1) {
                        continue;
                    }

                    int nextCost = node.cost + STRAIGHT_COST + ((node.direction + nextDirection) % 2 != 0 ? CURVED_COST : 0);
                    if (dp[nx][ny][nextDirection] > nextCost) {
                        dp[nx][ny][nextDirection] = nextCost;
                        q.add(new Node(dp[nx][ny][nextDirection], nx, ny, nextDirection));
                    }
                }
            }

            return Math.min(Math.min(dp[n-1][n-1][0], dp[n-1][n-1][1]), Math.min(dp[n-1][n-1][2], dp[n-1][n-1][3]));
        }

        private int[][][] initDp() {
            int[][][] dp = new int[n][n][DIRECT_BOUND];
            for (int i = 0; i < n; i ++) {
                for (int j = 0; j < n; j ++) {
                    for (int k = 0; k < DIRECT_BOUND; k ++) {
                        dp[i][j][k] = Integer.MAX_VALUE;
                    }
                }
            }
            for (int k = 0; k < DIRECT_BOUND; k ++) {
                dp[0][0][k] = 0;
            }
            return dp;
        }

        private static class Node implements Comparable<Node> {
            int cost;
            int x;
            int y;
            int direction;

            Node (int cost, int x, int y, int direction) {
                this.cost = cost;
                this.x = x;
                this.y = y;
                this.direction = direction;
            }

            @Override
            public int compareTo(Node o) {
                return Integer.compare(this.cost, o.cost);
            }

            @Override
            public boolean equals(Object o) {
                if (this == o) return true;
                if (o == null || this.getClass() != o.getClass()) return false;
                Node n = (Node) o;
                return this.x == n.x && this.y == n.y;
            }

            @Override
            public int hashCode() {
                return Objects.hash(x, y);
            }

        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 900
        int solution1 = solution.solution(new int[][]{new int[]{0, 0, 0}, new int[]{0, 0, 0}, new int[]{0, 0, 0}});
        System.out.println("solution = " + solution1);

        // 3800
        int solution2 = solution.solution(new int[][]{new int[]{0, 0, 0, 0, 0, 0, 0, 1}, new int[]{0, 0, 0, 0, 0, 0, 0, 0}, new int[]{0, 0, 0, 0, 0, 1, 0, 0}, new int[]{0, 0, 0, 0, 1, 0, 0, 0}, new int[]{0, 0, 0, 1, 0, 0, 0, 1}, new int[]{0, 0, 1, 0, 0, 0, 1, 0}, new int[]{0, 1, 0, 0, 0, 1, 0, 0}, new int[]{1, 0, 0, 0, 0, 0, 0, 0}});
        System.out.println("solution = " + solution2);

        // 2100
        int solution3 = solution.solution(new int[][]{new int[]{0, 0, 1, 0}, new int[]{0, 0, 0, 0}, new int[]{0, 1, 0, 1}, new int[]{1, 0, 0, 0}});
        System.out.println("solution = " + solution3);

        // 3200
        int solution4 = solution.solution(new int[][]{new int[]{0, 0, 0, 0, 0, 0}, new int[]{0, 1, 1, 1, 1, 0}, new int[]{0, 0, 1, 0, 0, 0}, new int[]{1, 0, 0, 1, 0, 1}, new int[]{0, 1, 0, 0, 0, 1}, new int[]{0, 0, 0, 0, 0, 0}});
        System.out.println("solution = " + solution4);

    }

}
