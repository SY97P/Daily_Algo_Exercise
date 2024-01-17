package 프로그래머스.lv3;

import java.util.PriorityQueue;

/**
 * 문제요약
 * <p>
 * 캐릭터는 다각형 둘레 따라서 이동
 * 서로 다른 직사각형의 x축, y축 좌표가 같은 경우 없음 (꼭지점에서 만나거나 변이 겹치지 않음)
 * 지형이 분리되지 않음
 * 지형이 포함되지 않음
 * 캐릭터가 아이템을 줍기 위해 이동하는 최단 거리 구하기
 * <p>
 * 제한사항
 * <p>
 * 1 <= 직사각형 수 <= 4
 * 직사각형 = [좌측하단x, 좌측하단y, 우측상단x, 우측상단y]
 * 1 <= x, y <= 50
 * 캐릭터 위치 != 아이템 위치
 * <p>
 * 해결전략
 * <p>
 * 크기를 두 배 늘려 생각한다
 * 두 배 전체보드에 두 배 직사각형에 해당하는 부분을 1로 채운다
 * 1로 채워진 부분 중에서 테두리가 아닌 칸 (주변 8칸이 모두 1인 칸) 은 2로 채운다
 * 캐릭터 위치에서 아이템 위치까지 1로 채워진 부분으로만 이동해서 구해지는 최단거리를 반환한다
 *
 */

public class 아이템_줍기 {

    private static class Solution {

        private static final int BOUND = 50;
        private static final int MULTIPLIER = 2;
        private static final int[] dx = {1, 0, 0, -1};
        private static final int[] dy = {0, 1, -1, 0};

        private int[][] board;

        public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
            board = new int[BOUND * MULTIPLIER + 1][BOUND * MULTIPLIER + 1];
            characterX *= MULTIPLIER;
            characterY *= MULTIPLIER;
            itemX *= MULTIPLIER;
            itemY *= MULTIPLIER;

            fillAllRegion(rectangle);
            fillInnerRegion();

            return bfs(characterX, characterY, itemX, itemY) / 2;
        }

        private int bfs(int characterX, int characterY, int itemX, int itemY) {
            int[][] dp = initDp();
            PriorityQueue<int[]> pq = new PriorityQueue<>((arr1, arr2) -> arr1[0] - arr2[0]);

            dp[characterX][characterY] = 0;
            pq.add(new int[]{dp[characterX][characterY], characterX, characterY});

            while (!pq.isEmpty()) {
                int[] current = pq.poll();

                if (dp[current[1]][current[2]] < current[0]) {
                    continue;
                }

                if (current[1] == itemX && current[2] == itemY) {
                    return dp[current[1]][current[2]];
                }

                for (int i = 0; i < dx.length; i ++) {
                    int nx = current[1] + dx[i];
                    int ny = current[2] + dy[i];

                    if (isOutOfBound(nx, ny)) {
                        continue;
                    }

                    if (board[nx][ny] == 1 && dp[nx][ny] > dp[current[1]][current[2]] + 1) {
                        dp[nx][ny] = dp[current[1]][current[2]] + 1;
                        pq.add(new int[]{dp[nx][ny], nx, ny});
                    }
                }
            }

            return 0;
        }

        private int[][] initDp() {
            int[][] dp = new int[BOUND * MULTIPLIER + 1][BOUND * MULTIPLIER + 1];
            for (int i = 0; i <= BOUND * MULTIPLIER; i ++) {
                for (int j = 0; j <= BOUND * MULTIPLIER; j ++) {
                    dp[i][j] = BOUND * 5;
                }
            }
            return dp;
        }

        private void fillInnerRegion() {
            for (int i = 0; i <= BOUND * MULTIPLIER; i ++) {
                for (int j = 0; j <= BOUND * MULTIPLIER; j ++) {
                    if (board[i][j] == 1 && isInnerRegion(i, j)) {
                        board[i][j] = 2;
                    }
                }
            }
        }

        private boolean isInnerRegion(int x, int y) {
            int count = 0;
            for (int i = -1; i <= 1; i ++) {
                for (int j = -1; j <= 1; j ++) {
                    int nx = x + i;
                    int ny = y + j;

                    if (!isOutOfBound(nx, ny) && board[nx][ny] != 0) {
                        count ++;
                    }
                }
            }
            return count >= 9;
        }

        private boolean isOutOfBound(int x, int y) {
            return x < 0 || x > BOUND * MULTIPLIER || y < 0 || y > BOUND * MULTIPLIER;
        }

        private void fillAllRegion(int[][] rectangles) {
            for (int[] rectangle : rectangles) {
                for (int i = rectangle[0] * MULTIPLIER; i <= rectangle[2] * MULTIPLIER; i ++) {
                    for (int j = rectangle[1] * MULTIPLIER; j <= rectangle[3] * MULTIPLIER; j ++) {
                        board[i][j] = 1;
                    }
                }
            }
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 17
        int solution1 = solution.solution(new int[][]{new int[]{1, 1, 7, 4}, new int[]{3, 2, 5, 5}, new int[]{4, 3, 6, 9}, new int[]{2, 6, 8, 8}}, 1, 3, 7, 8);
        System.out.println("solution1 = " + solution1);

        // 11
        int solution2 = solution.solution(new int[][]{new int[]{1, 1, 8, 4}, new int[]{2, 2, 4, 9}, new int[]{3, 6, 9, 8}, new int[]{6, 3, 7, 7}}, 9, 7, 6, 1);
        System.out.println("solution2 = " + solution2);

        // 9
        int solution3 = solution.solution(new int[][]{new int[]{1, 1, 5, 7}}, 1, 1, 4, 7);
        System.out.println("solution3 = " + solution3);

        // 15
        int solution4 = solution.solution(new int[][]{new int[]{2, 1, 7, 5}, new int[]{6, 4, 10, 10}}, 3, 1, 7, 10);
        System.out.println("solution4 = " + solution4);

        // 10
        int solution5 = solution.solution(new int[][]{new int[]{2, 2, 5, 5}, new int[]{1, 3, 6, 4}, new int[]{3, 1, 4, 6}}, 1, 4, 6, 3);
        System.out.println("solution5 = " + solution5);

        // 8
        int solution6 = solution.solution(new int[][]{new int[]{2, 1, 3, 6}, new int[]{4, 1, 5, 6}, new int[]{1, 2, 6, 3}, new int[]{1, 4, 6, 5}}, 3, 2, 5, 4);
        System.out.println("solution6 = " + solution6);

    }

}
