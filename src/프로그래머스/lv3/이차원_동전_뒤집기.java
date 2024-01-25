package 프로그래머스.lv3;

/**
 * 문제요약<br>
 * <p>
 * beginning -> target 상태로 만들기 위해 필요한 최소 동전 뒤집기 횟수 구하기<br>
 * 같은 줄에 있는 모든 동전 뒤집기<br>
 * target 상태 만들기 불가 -> -1<br>
 * 0(앞면) / 1(뒷면)<br>
 * <br>
 * 제한사항<br>
 * <br>
 * 1 <= len(beginning) = len(target) <= 10<br>
 * 1 <= len(beginning[i]) = len(target[i]) <= 10<br>
 * <p>
 * 해결전략 (비트마스크)
 * <p>
 * 가로행만큼의 비트마스크 생성
 * 비트마스크가 0인 행은 원본배열, 1인 행은 플립배열로 바둑판 만들기
 * 0행의 모든 열을 순회하면서 바둑판과 타겟이 다른 값이면 폴드해봄
 * 폴드배열을 타겟과 비교해서 모두 같으면 최소 뒤집수 갱신
 * 만약에 최소 뒤집수가 한 번도 갱신 안됐으면(초기값이면) -1 리턴
 */

public class 이차원_동전_뒤집기 {

    private static class Solution {

        private int n;
        private int m;

        public int solution(int[][] beginning, int[][] target) {
            n = beginning.length;
            m = beginning[0].length;

            int answer = Integer.MAX_VALUE;

            int[][] fliped = new int[n][m];
            for (int i = 0; i < n; i ++) {
                fliped[i] = flip(beginning[i]);
            }

            for (int bitmask = (1 << n) - 1; bitmask >= 0; bitmask --) {
                int count = 0;
                int[][] board = new int[n][m];

                int copymask = bitmask;
                for (int i = 0; i < n; i ++) {
                    if ((copymask & 1) == 1) {
                        board[i] = fliped[i].clone();
                        count ++;
                    } else {
                        board[i] = beginning[i].clone();
                    }
                    copymask >>>= 1;
                }

                for (int j = 0; j < m; j ++) {
                    if (board[0][j] != target[0][j]) {
                        fold(j, board);
                        count ++;
                    }
                }

                if (isEqual(board, target)) {
                    answer = Math.min(answer, count);
                }
            }

            return answer == Integer.MAX_VALUE ? -1 : answer;
        }

        private void fold(int col, int[][] board) {
            for (int i = 0; i < n; i ++) {
                board[i][col] = (board[i][col] + 1) % 2;
            }
        }

        private int[] flip(int[] rowArray) {
            int[] fliped = rowArray.clone();
            for (int i = 0; i < m; i ++) {
                fliped[i] = (fliped[i] + 1) % 2;
            }
            return fliped;
        }

        private boolean isEqual(int[][] board, int[][] target) {
            for (int i = 0; i < n; i ++) {
                for (int j = 0; j < m; j ++) {
                    if (board[i][j] != target[i][j]) {
                        return false;
                    }
                }
            }
            return true;
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 5
        int[][] beginning1 = {
                {0, 1, 0, 0, 0},
                {1, 0, 1, 0, 1},
                {0, 1, 1, 1, 0},
                {1, 0, 1, 1, 0},
                {0, 1, 0, 1, 0}};
        int[][] target1 = {
                {0, 0, 0, 1, 1},
                {0, 0, 0, 0, 1},
                {0, 0, 1, 0, 1},
                {0, 0, 0, 1, 0},
                {0, 0, 0, 0, 1}};
        int solution1 = solution.solution(beginning1, target1);
        System.out.println("solution1 = " + solution1);

        // -1
        int[][] beginning2 = {
                {0, 0, 0},
                {0, 0, 0},
                {0, 0, 0}};
        int[][] target2 = {
                {1, 0, 1},
                {0, 0, 0},
                {0, 0, 0}};
        int solution2 = solution.solution(beginning2, target2);
        System.out.println("solution2 = " + solution2);
        
        // 2
        int[][] beginning3 = {
                {0, 0, 1, 0, 0},
                {1, 0, 0, 0, 0},
                {0,0,0,0,0},
                {0,0,0,0,0},
                {0,0,0,0,0}};
        int[][] target3 = {
                {0,1,0,1,1},
                {0,0,0,0,0},
                {1,0,0,0,0},
                {1,0,0,0,0},
                {1,0,0,0,0}};
        int solution3 = solution.solution(beginning3, target3);
        System.out.println("solution3 = " + solution3);
    }

}
