package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 문제요약
 * <p>
 * - 시계방향으로 한 번에 90도 돌아가는 시계
 * - 시계 돌리면 상하좌우 인접 시계도 돌아감
 * - 모서리 시계 돌아가면 -> 주변 3개 시계 돌아감
 * - 꼭지점 시계 돌아가면 -> 주변 2개 시계 돌아감
 * - 모든 시계가 12시를 가리키면 잠금해제
 * - 최소한의 조작으로 잠금해제할 때 조작 횟수 구하기
 * - 2 <= len(clockHands) <= 8 (정사각형)
 * - 0 <= clockHands[i] <= 3
 * - 해결 가능한 퍼즐만 주어짐
 * <p>
 * 해결전략
 * <p>
 * - 1행부터 시작해서 바로 위 값이 0이 아니라면 돌림
 */

public class 고고학_최고의_발견 {

    private static class Solution {

        private static final int timeBound = 4;

        private static final int[] dx = {-1, 0, 0, 1, 0};
        private static final int[] dy = {0, 1, -1, 0, 0};

        public int solution(int[][] clockHands) {
            int n = clockHands.length;

            int answer = Integer.MAX_VALUE;

            List<List<Integer>> initialRotateAmount = generateProducts(n);

            for (List<Integer> amounts : initialRotateAmount) {
                int[][] clocks = arrayCopy(clockHands);

                rotateInitialLine(amounts, n, clocks);

                int count = rotateRemainLines(n, clocks) + amounts.stream()
                        .mapToInt(Integer::intValue)
                        .sum();

                if (isAll12Clock(clocks, n)) {
                    answer = Math.min(answer, count);
                }
            }

            return answer;
        }

        private void rotateInitialLine(List<Integer> amounts, int n, int[][] clocks) {
            for (int col = 0; col < n; col ++) {
                for (int time = 0; time < amounts.get(col); time ++) {
                    rotate(0, col, clocks);
                }
            }
        }

        private int rotateRemainLines(int n, int[][] clocks) {
            int count = 0;
            for (int i = 1; i < n; i ++) {
                for (int j = 0; j < n; j ++) {
                    while (clocks[i - 1][j] != 0) {
                        count ++;
                        rotate(i, j, clocks);
                    }
                }
            }
            return count;
        }

        private boolean isAll12Clock(int[][] clocks, int n) {
            return sum(clocks[n - 1]) == 0;
        }

        private int sum(int[] clock) {
            return Arrays.stream(clock)
                    .sum();
        }

        private int[][] arrayCopy(int[][] array) {
            int[][] copy = new int[array.length][array.length];
            for (int i = 0; i < array.length; i ++) {
                System.arraycopy(array[i], 0, copy[i], 0, array.length);
            }
            return copy;
        }

        private List<List<Integer>> generateProducts(int n) {
            List<List<Integer>> combinations = new ArrayList<>();
            generateProduct(n, combinations, new ArrayList<>());
            return combinations;
        }

        private void generateProduct(int n, List<List<Integer>> combinations, List<Integer> temp) {
            if (temp.size() == n) {
                combinations.add(new ArrayList<>(temp));
                return;
            }

            for (int value = 0; value < timeBound; value++) {
                temp.add(value);
                generateProduct(n, combinations, temp);
                temp.remove(temp.size() - 1);
            }
        }

        private void rotate(int row, int col, int[][] array) {
            for (int i = 0; i < dx.length; i++) {
                int x = row + dx[i];
                int y = col + dy[i];

                if (x < 0 || x >= array.length || y < 0 || y >= array.length) {
                    continue;
                }

                array[x][y] = (array[x][y] + 1) % 4;
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 3
        int[][] clockHands1 = {{0, 3, 3, 0}, {3, 2, 2, 3}, {0, 3, 2, 0}, {0, 3, 3, 3}};
        int solution1 = solution.solution(clockHands1);
        System.out.println("solution1 = " + solution1);
    }

}
