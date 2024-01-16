package 프로그래머스.lv3;

/**
 * 문제요약
 * <p>
 * N * M 행렬
 * 공격 -> 내구도 깎임
 * 힐링 -> 내구도 참
 * 내구도 <= 0 -> 파괴 (이 상태에서도 내구도 깎이고 참)
 * 모든 작업이 끝난 후 파괴되지 않은 건물 수 구하기 (내구도 >= 1 인 건물 수 구하기)
 * <p>
 * 제한사항
 * <p>
 * 1 <= 행 길이, 열 길이 <= 10^3 (직사각형)
 * 1 <= 초기 내구도 <= 10^3
 * 1 <= 스킬 길이 <= 15 * 10^4
 * 스킬 : [타입(1:공격,2:힐링), r1, c1, r2, c2, 내구도 변화값]
 * 1 <= 내구도 변화값 <= 500
 * <p>
 * 해결전략 (누적합)
 * <p>
 * (r1, c1) ~ (r2, c2) 구간 누적합을 계속 구해감
 *  [r1, c1], [r2 + 1, c2 + 1] = degree
 *  [r1, c2 + 1], [r2 + 1, c1] = -degree
 * 원본 내구도 행렬에 누적합 행렬 더하기
 * 결과에서 1 이상인 칸의 개수 반환
 */

public class 파괴되지_않은_건물 {

    private static class Solution {

        public int solution(int[][] board, int[][] skills) {
            int n = board.length;
            int m = board[0].length;

            int[][] accumulation = new int[n + 1][m + 1];

            for (int[] skill : skills) {
                int degree = skill[0] == 1 ? -1 * skill[5] : skill[5];
                int r1 = skill[1];
                int c1 = skill[2];
                int r2 = skill[3];
                int c2 = skill[4];

                accumulation[r1][c1] += degree;
                accumulation[r2 + 1][c2 + 1] += degree;
                accumulation[r1][c2 + 1] += -degree;
                accumulation[r2 + 1][c1] += -degree;
            }

            for (int i = 0; i <= n; i ++) {
                for (int j = 0; j < m; j ++) {
                    accumulation[i][j + 1] += accumulation[i][j];
                }
            }

            for (int j = 0; j <= m; j ++) {
                for (int i = 0; i < n; i ++) {
                    accumulation[i + 1][j] += accumulation[i][j];
                }
            }

            int answer = 0;
            for (int i = 0; i < n; i ++) {
                for (int j = 0; j < m; j ++) {
                    if (board[i][j] + accumulation[i][j] > 0) {
                        answer ++;
                    }
                }
            }

            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 10
        int solution1 = solution.solution(
                new int[][]{new int[]{5, 5, 5, 5, 5}, new int[]{5, 5, 5, 5, 5}, new int[]{5, 5, 5, 5, 5}, new int[]{5, 5, 5, 5, 5}},
                new int[][]{new int[]{1, 0, 0, 3, 4, 4}, new int[]{1, 2, 0, 2, 3, 2}, new int[]{2, 1, 0, 3, 1, 2}, new int[]{1, 0, 1, 3, 3, 1}});
        System.out.println("solution1 = " + solution1);

        // 6
        int solution2 = solution.solution(
                new int[][]{new int[]{1, 2, 3}, new int[]{4, 5, 6}, new int[]{7, 8, 9}},
                new int[][]{new int[]{1, 1, 1, 2, 2, 4}, new int[]{1, 0, 0, 1, 1, 2}, new int[]{2, 2, 0, 2, 0, 100}});
        System.out.println("solution2 = " + solution2);
    }
}
