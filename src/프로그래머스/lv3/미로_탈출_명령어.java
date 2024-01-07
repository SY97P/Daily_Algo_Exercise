package 프로그래머스.lv3;

import java.util.Objects;

/**
 * 요약
 * <p>
 * - n * m 크기 미로 - (x, y) -> (r, c) 이동 - l, r, u, d -> d, l, r, u (사전순) - 탈출 불가면 "impossible" 반환 - 미로 탈출 조건 1. 격자 바깥으로
 * 이동 불가 2. (x, y) -> (r, c) 거리가 k 3. 재방문 가능 4. 탈출 가능한 경로 중 사전 순으로 가장 빠른 경로
 * <p>
 * 해결전략 핵심 : DFS 탈출 불가 조건 1. (탈출위치 - 현재위치) = 남은거리 > k 인 경우 2. (k - 남은거리 - 이동한거리 = 추가이동거리) % 2 != 0 인 경우 3. trunning
 */

public class 미로_탈출_명령어 {

    private static class Solution {

        private enum Command {
            D("d", 1, 0),
            L("l", 0, -1),
            R("r", 0, 1),
            U("u", -1, 0);

            final String value;
            final int dx;
            final int dy;

            Command(String value, int dx, int dy) {
                this.value = value;
                this.dx = dx;
                this.dy = dy;
            }
        }

        private int n;
        private int m;
        private int r;
        private int c;
        private int k;

        public String solution(int n, int m, int x, int y, int r, int c, int k) {
            this.n = n;
            this.m = m;
            this.r = r - 1;
            this.c = c - 1;
            this.k = k;

            return solveMaze(x - 1, y - 1, new StringBuilder());
        }

        private String solveMaze(int x, int y, StringBuilder sb) {
            if (isEscapable(x, y, sb)) {
                return sb.toString();
            }

            if (isImpossible(x, y, sb.toString())) {
                return "impossible";
            }

            for (Command command : Command.values()) {
                int nx = x + command.dx;
                int ny = y + command.dy;

                if (isOutOfBound(nx, ny)) {
                    continue;
                }

                sb.append(command.value);
                String result = solveMaze(nx, ny, sb);
                if (!Objects.equals(result, "impossible")) {
                    return result;
                }

                sb.deleteCharAt(sb.length() - 1);
            }

            return "imposssible";
        }

        private boolean isOutOfBound(int nx, int ny) {
            return nx < 0 || nx >= n || ny < 0 || ny >= m;
        }

        private boolean isImpossible(int x, int y, String path) {
            int pathLength = path.length();
            int restDistance = Math.abs(x - r) + Math.abs(y - c);
            int additionalDistance = k - restDistance - pathLength;

            return restDistance > k - pathLength || additionalDistance % 2 != 0;
        }

        private boolean isEscapable(int x, int y, StringBuilder sb) {
            return x == r && y == c && sb.length() == k;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // "dllrl"
        String solution1 = solution.solution(3, 4, 2, 3, 3, 1, 5);
        System.out.println("solution1 = " + solution1);

        // "dr"
        String solution2 = solution.solution(2, 2, 1, 1, 2, 2, 2);
        System.out.println("solution2 = " + solution2);

        // "impossible"
        String solution3 = solution.solution(3,	3,	1,	2,	3,	3,	4);
        System.out.println("solution3 = " + solution3);

    }

}
