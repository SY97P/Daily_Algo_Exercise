package 프로그래머스.lv3;

/**
 * 문제요약
 * <p>
 * - A 가 먼저 시작
 * - 발판 있는 곳만 이동 가능
 * - 발판 이동(상하좌우) 시 기존 발판 제거됨
 * - 승리자는 최대한 빨리 이기도록, 패배자는 최대한 늦게 지도록
 * - 패배조건
 *  1. 이동할 발판이 없는 경우
 *  2. 두 명이 같은 발판에 있는 경우
 * <p>
 * 문제 조건
 * <p>
 * 1 <= 발판 세로, 가로 <= 5 (직사각형)
 * 0 : 발판 없음 / 1 : 발판 있음
 * <p>
 * 해결전략
 * <p>
 * - DFS
 * 1. 각 플레이어가 이동할 수 있는 발판으로 모두 이동해봄
 * 2. 각 이동에 대해서 구해진 값 중에서 본인이 이길 수 있는 경우가 있다면 최소값을 반환하고, 없다면 최대값을 반환
 * 3. 패배조건
 *  3-1. 이동할 발판이 없는 경우 return [상대방 이김, 0]
 *  3-2. 두 명이 같은 발판에 있는 경우 return [상대방 이김, 1]
 *
 */

public class 사라지는_발판 {

    private static class Solution {

        private static final int[] dx = new int[]{1, 0, 0, -1};
        private static final int[] dy = new int[]{0, 1, -1, 0};

        private int[][] board;
        private int n;
        private int m;

        public int solution(int[][] _board, int[] aloc, int[] bloc) {
            board = _board;
            n = board.length;
            m = board[0].length;

            return dfs(aloc, bloc, 0).count;
        }

        private Result dfs(int[] playerLoc, int[] otherLoc, int step) {
            int winCount = Integer.MAX_VALUE;
            int loseCount = Integer.MIN_VALUE;

            if (!movable(playerLoc)) {
                return new Result(false, step);
            }
            if (playerLoc[0] == otherLoc[0] && playerLoc[1] == otherLoc[1]) {
                return new Result(true, step + 1);
            }

            for (int i = 0; i < dx.length; i ++) {
                int nr = playerLoc[0] + dx[i];
                int nc = playerLoc[1] + dy[i];

                if (checkRange(nr, nc)) {
                    continue;
                }

                board[playerLoc[0]][playerLoc[1]] = 0;

                Result result = dfs(otherLoc, new int[]{nr, nc}, step + 1);
                if (!result.flag) {
                    winCount = Math.min(winCount, result.count);
                } else {
                    loseCount = Math.max(loseCount, result.count);
                }

                board[playerLoc[0]][playerLoc[1]] = 1;
            }

            if (winCount < Integer.MAX_VALUE) {
                return new Result(true, winCount);
            }
            return new Result(false, loseCount);
        }

        private boolean movable(int[] playerLoc) {
            for (int i = 0; i < dx.length; i ++) {
                int nr = playerLoc[0] + dx[i];
                int nc = playerLoc[1] + dy[i];

                if (checkRange(nr, nc)) {
                    continue;
                }
                return true;
            }
            return false;
        }

        private boolean checkRange(int nr, int nc) {
            return nr < 0 || nr >= n || nc < 0 || nc >= m || board[nr][nc] == 0;
        }

        private static class Result {
            boolean flag;
            int count;

            Result (boolean flag, int count) {
                this.flag = flag;
                this.count = count;
            }
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 5
        int solution1 = solution.solution(new int[][]{new int[]{1, 1, 1}, new int[]{1, 1, 1}, new int[]{1, 1, 1}},
                new int[]{1, 0}, new int[]{1, 2});
        System.out.println("solution1 = " + solution1);

        // 4
        int solution2 = solution.solution(new int[][]{new int[]{1, 1, 1}, new int[]{1, 0, 1}, new int[]{1, 1, 1}},
                new int[]{1, 0}, new int[]{1, 2});
        System.out.println("solution2 = " + solution2);

        // 4
        int solution3 = solution.solution(new int[][]{new int[]{1, 1, 1, 1, 1}}, new int[]{0, 0}, new int[]{0, 4});
        System.out.println("solution3 = " + solution3);

        // 0
        int solution4 = solution.solution(new int[][]{new int[]{1}}, new int[]{0, 0}, new int[]{0, 0});
        System.out.println("solution4 = " + solution4);
    }

}
