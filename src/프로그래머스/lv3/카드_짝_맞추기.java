package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.PriorityQueue;
import java.util.stream.Collectors;

/**
 * 문제요약<br>
 *<br>
 * 4*4 배열에 최대 6가지 카드가 각각 두 장씩 뒤집힌 채로 배치<br>
 * 카드 한 장을 뒤집고, 해당 카드 숫자와 일치하는 다른 숫자를 뒤집으면 카드 사라짐<br>
 * 남은 카드를 모두 제거하는데 필요한 최소 조작횟수 구하기<br>
 * 조작법<br>
 *  - 방향키 : 해당 방향으로 1칸 이동<br>
 *  - ctrl + 방향키 : 해당 방향에 있는 가장 가까운 카드로 한번에 이동 (카드가 없으면 해당 방향 끝으로 이동)<br>
 *  - enter : 카드 뒤집기<br>
 *<br>
 * 제한사항<br>
 *<br>
 * board 행렬길이 = 4<br>
 * 0 <= board 원소 <= 6<br>
 *  0 : 빈 칸<br>
 *  나머지 : 해당 숫자에 상응하는 카드<br>
 *  좌측상단 : (0, 0)<br>
 *  우측하단 : (3, 3)<br>
 * 0 <= 최초 커서 행, 열 위치 <= 3<br>
 *<br>
 * 해결전략 (Dijkstra, DFS, Permutation)<br>
 *<br>
 * 카드 숫자별 위치 미리 추출<br>
 * 카드 순서 순열으로 만들기<br>
 * 해당 순열에 따라 DFS<br>
 *  두 개의 카드 중 어디를 먼저 뒤집을지에 따라 DFS 처리<br>
 * 모든 결과에 대해서 구해지는 최소값을 유지<br>
 *  해당 값보다 큰 조작횟수인 경우 trunning<br>
 *
 */

public class 카드_짝_맞추기 {

    private static class Solution {

        private static final int BOUND = 4;
        private static final int[] dx = {1, 0, 0, -1};
        private static final int[] dy = {0, 1, -1, 0};

        private int answer;
        private int[][] board;
        private Map<Integer, List<Coordi>> cardLocations;
        private List<List<Integer>> permutations;

        public int solution(int[][] _board, int r, int c) {
            answer = Integer.MAX_VALUE;
            board = _board;
            cardLocations = new HashMap<>();
            permutations = new ArrayList<>();

            findCardLocations();
            List<Integer> cardNumbers = cardLocations.keySet().stream().collect(Collectors.toList());
            makePermutations(cardNumbers, new ArrayList<>());

            for (List<Integer> permutation : permutations) {
                dfs(new Coordi(r, c), 0, 0, permutation);
            }

            return answer;
        }

        private void dfs(Coordi coordi, int countOfOperation, int cardIndex, List<Integer> permutation) {
            if (countOfOperation > answer) {
                return;
            }

            if (cardIndex >= permutation.size()) {
                answer = countOfOperation;
                return;
            }

            int cardNumber = permutation.get(cardIndex);
            List<Coordi> cardLocation = cardLocations.get(cardNumber);
            Coordi a = cardLocation.get(0);
            Coordi b = cardLocation.get(1);

            int caDistance = bfs(coordi, a);
            board[a.x][a.y] = 0;
            int abDistance = bfs(a, b);
            board[b.x][b.y] = 0;
            dfs(b, countOfOperation + caDistance + abDistance + 2, cardIndex + 1, permutation);
            board[a.x][a.y] = cardNumber;
            board[b.x][b.y] = cardNumber;

            int cbDistance = bfs(coordi, b);
            board[b.x][b.y] = 0;
            int baDistance = bfs(b, a);
            board[a.x][a.y] = 0;
            dfs(a, countOfOperation + cbDistance + baDistance + 2, cardIndex + 1, permutation);
            board[b.x][b.y] = cardNumber;
            board[a.x][a.y] = cardNumber;
        }

        private int bfs(Coordi start, Coordi end) {
            int[][] dp = initDp(start);

            PriorityQueue<Coordi> q = new PriorityQueue<>();
            q.add(new Coordi(start.x, start.y, dp[start.x][start.y]));

            while (!q.isEmpty()) {
                Coordi coordi = q.poll();

                if (coordi.distance > dp[coordi.x][coordi.y]) {
                    continue;
                }
                if (Objects.equals(coordi, end)) {
                    return coordi.distance;
                }

                normalOperation(coordi, dp, q);
                ctrlOperation(coordi, dp, q);
            }

            return 0;
        }

        private void ctrlOperation(Coordi coordi, int[][] dp, PriorityQueue<Coordi> q) {
            for (int d = 0; d < dx.length; d ++) {
                int nx = coordi.x + dx[d];
                int ny = coordi.y + dy[d];

                while (!isOutOfBound(nx + dx[d], ny + dy[d]) && board[nx][ny] == 0) {
                    nx += dx[d];
                    ny += dy[d];
                }

                if (!isOutOfBound(nx, ny) && dp[nx][ny] > coordi.distance + 1) {
                    dp[nx][ny] = coordi.distance + 1;
                    q.add(new Coordi(nx, ny, dp[nx][ny]));
                }
            }
        }

        private void normalOperation(Coordi coordi, int[][] dp, PriorityQueue<Coordi> q) {
            for (int d = 0; d < dx.length; d ++) {
                int nx = coordi.x + dx[d];
                int ny = coordi.y + dy[d];

                if (isOutOfBound(nx, ny)) {
                    continue;
                }

                if (dp[nx][ny] > coordi.distance + 1) {
                    dp[nx][ny] = coordi.distance + 1;
                    q.add(new Coordi(nx, ny, dp[nx][ny]));
                }
            }
        }

        private boolean isOutOfBound(int nx, int ny) {
            return nx < 0 || nx >= BOUND || ny < 0 || ny >= BOUND;
        }

        private int[][] initDp(Coordi start) {
            int[][] dp = new int[BOUND][BOUND];
            for (int i = 0; i < BOUND; i ++) {
                for (int j = 0; j < BOUND; j ++) {
                    dp[i][j] = Integer.MAX_VALUE;
                }
            }
            dp[start.x][start.y] = 0;
            return dp;
        }


        private void makePermutations(List<Integer> cardNumbers, List<Integer> list) {
            if (list.size() == cardNumbers.size()) {
                permutations.add(List.copyOf(list));
                return;
            }

            for (int cardNumber : cardNumbers) {
                if (!list.contains(cardNumber)) {
                    list.add(cardNumber);
                    makePermutations(cardNumbers, list);
                    list.remove(list.size() - 1);
                }
            }
        }

        private void findCardLocations() {
            for (int i = 0; i < BOUND; i ++) {
                for (int j = 0; j < BOUND; j ++) {
                    if (board[i][j] == 0) {
                        continue;
                    }

                    cardLocations.putIfAbsent(board[i][j], new ArrayList<>());
                    cardLocations.get(board[i][j]).add(new Coordi(i, j));
                }
            }
        }

        private static class Coordi implements Comparable<Coordi> {
            int x;
            int y;
            int distance;

            Coordi (int x, int y) {
                this.x = x;
                this.y = y;
            }

            Coordi (int x, int y, int distance) {
                this.x = x;
                this.y = y;
                this.distance = distance;
            }

            @Override
            public int compareTo(Coordi o) {
                return Integer.compare(this.distance, o.distance);
            }

            @Override
            public boolean equals(Object o) {
                if (this == o) return true;
                if (o == null || this.getClass() != o.getClass()) return false;
                Coordi c = (Coordi) o;
                return this.x == c.x && this.y == c.y;
            }

            @Override
            public int hashCode() {
                return Objects.hash(x, y);
            }

        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 14
        int solution1 = solution.solution(new int[][]{new int[]{1, 0, 0, 3}, new int[]{2, 0, 0, 0}, new int[]{0, 0, 0, 2}, new int[]{3, 0, 1, 0}}, 1, 0);
        System.out.println("solution1 = " + solution1);

        // 16
        int solution2 = solution.solution(new int[][]{new int[]{3, 0, 0, 2}, new int[]{0, 0, 1, 0}, new int[]{0, 1, 0, 0}, new int[]{2, 0, 0, 3}}, 0, 1);
        System.out.println("solution2 = " + solution2);

        // 5
        int solution3 = solution.solution(new int[][]{new int[]{0, 0, 0, 1}, new int[]{0, 0, 0, 0}, new int[]{0, 1, 0, 0}, new int[]{0, 0, 0, 0}}, 0, 3);
        System.out.println("solution3 = " + solution3);

    }

}
