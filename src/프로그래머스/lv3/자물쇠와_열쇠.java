package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.List;

/**
 * 문제요약
 *
 * N*N 크기 자물쇠, M*M 크기 열쇠
 * 자물쇠, 열쇠에 홈과 돌기
 * 홈과 돌기가 정확히 맞어떨어지고, 자물쇠의 모든 홈이 채워져야 자물쇠 열림
 * 열쇠는 회전, 이동 가능
 * 자물쇠 영역을 벗어난 열쇠는 자물쇠에 영향을 주지 않음
 * 주어진 자물쇠, 열쇠로 열리는 지 여부를 반환
 *
 * 제한사항
 *
 * 3 <= M <= N <= 20
 * 0 홈 / 1 돌기
 *
 * 해결전략
 *
 * N을 3배 늘리고 총 9배로 늘어난 전체 공간의 가운데 영역에 자물쇠 배치
 * 자물쇠와 열쇠가 최소 1칸 겹치는 경우부터 최대 M*M 칸 겹치는 모든 경우에 대해서 연산
 * 각 경우에 따라 열쇠를 회전시켜서 시도
 * 열리는 경우가 하나라도 있는 경우 true 반환 + 이후 연산 trunning
 * 그 외 false 반환
 * 열림 = 모든 자물쇠 영역에 대해서 (자물쇠값 + 열쇠값 = 1) 인 경우
 *
 */

public class 자물쇠와_열쇠 {

    private static class Solution {

        public boolean solution(int[][] key, int[][] lock) {
            int n = lock.length;

            int[][] space = getSpace(lock);
            List<int[][]> keys = getRotatedKeys(key);

            for (int i = 0; i < 2 * n; i ++) {
                for (int j = 0; j < 2 * n; j ++) {
                    for (int[][] rotatedKey : keys) {
                        if (matched(i, j, rotatedKey, space)) {
                            return true;
                        }
                    }
                }
            }

            return false;
        }

        private boolean matched(int x, int y, int[][] rotatedKey, int[][] space) {
            int n = space.length / 3;
            int m = rotatedKey.length;

            int[][] board = new int[3 * n][3 * n];

            for (int i = n; i < 2 * n; i ++) {
                for (int j = n; j < 2 * n; j ++) {
                    board[i][j] = space[i][j];
                }
            }

            for (int i = 0; i < m; i ++) {
                for (int j = 0; j < m; j ++) {
                    board[x + i][y + j] = space[x + i][y + j] + rotatedKey[i][j];
                }
            }

            for (int i = n; i < 2 * n; i ++) {
                for (int j = n; j < 2 * n; j ++) {
                    if (board[i][j] != 1) {
                        return false;
                    }
                }
            }
            return true;
        }

        private List<int[][]> getRotatedKeys(int[][] key) {
            List<int[][]> keys = new ArrayList<>();

            for (int k = 0; k < 4; k ++) {
                key = rotate(key);
                keys.add(key);
            }

            return keys;
        }

        private int[][] rotate(int[][] key) {
            int m = key.length;

            int[][] rotated = new int[m][m];
            for (int i = 0; i < m; i ++) {
                for (int j = 0; j < m; j ++) {
                    rotated[j][m - i - 1] = key[i][j];
                }
            }

            return rotated;
        }

        private int[][] getSpace(int[][] lock) {
            int n = lock.length;
            int[][] space = new int[3 * n][3 * n];
            for (int i = 0; i < n; i ++) {
                for (int j = 0; j < n; j ++) {
                    space[i + n][j + n] = lock[i][j];
                }
            }
            return space;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // true
        boolean solution1 = solution.solution(new int[][]{new int[]{0, 0, 0}, new int[]{1, 0, 0}, new int[]{0, 1, 1}}, new int[][]{new int[]{1, 1, 1}, new int[]{1, 1, 0}, new int[]{1, 0, 1}});
        System.out.println("solution1 = " + solution1);

    }

}
