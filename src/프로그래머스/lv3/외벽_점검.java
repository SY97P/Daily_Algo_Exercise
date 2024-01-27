package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.List;

/**
 * 문제요약<br>
 * <br>
 * N 미터 둘레를 가진 외벽에 취약지점 존재<br>
 * 친구들은 1시간만 점검 가능<br>
 * 친구들은 1시간 동안 이동할 수 있는 거리가 다름<br>
 * 외벽점검은 시계/반시계 방향 모두 가능<br>
 * 모든 취약지점을 점검하기 위해 보내야할 최소 친구 수 구하기<br>
 * 모든 친구를 다 보내도 모든 점검이 불가한 경우 -1 반환<br>
 * <br>
 * 제한사항<br>
 * <br>
 * 1 <= 외벽 길이 <= 200<br>
 * 1 <= 취약지점 수 <= 15<br>
 * 0 <= 취약지점 위치 < 외벽길이<br>
 * 취약지점은 중복되지 않음<br>
 * 취약지점은 오름차순 정렬되어 있음<br>
 * 1 <= 친구 수 <= 8<br>
 * 1 <= 친구 시간당 이동거리 <= 100<br>
 * <br>
 * 해결전략<br>
 * <br>
 * 외벽 둘레 2배 늘리기<br>
 *  취약지점 탐색을 시계방향으로 통일<br>
 * 친구 순번 순열 구하기<br>
 * 친구 별로 취약지점 탐색<br>
 * 모든 지점 탐색이 가능한 경우 정답 갱신<br>
 *
 */

public class 외벽_점검 {

    private static class Solution {

        private int weakCount;
        private int[] weakPoints;
        private int[] distances;
        private boolean[] visited;

        public int solution(int n, int[] weak, int[] dist) {
            weakCount = weak.length;
            weakPoints = regulateWeakPoints(n, weak);
            distances = dist;
            visited = new boolean[dist.length];

            int answer = dfs(new ArrayList<>());

            return answer == Integer.MAX_VALUE ? -1 : answer;
        }

        private int dfs(ArrayList<Integer> friends) {
            if (friends.size() >= distances.length) {
                return getManPower(friends);
            }

            int minManPower = Integer.MAX_VALUE;
            for (int i = 0; i < distances.length; i ++) {
                if (!visited[i]) {
                    visited[i] = true;
                    friends.add(distances[i]);
                    minManPower = Math.min(minManPower, dfs(friends));
                    visited[i] = false;
                    friends.remove(friends.size() - 1);
                }
            }

            return minManPower;
        }

        private int getManPower(ArrayList<Integer> friends) {
            int minManPower = Integer.MAX_VALUE;

            for (int start = 0; start < weakCount; start ++) {
                int count = 1;
                int point = weakPoints[start] + friends.get(count - 1);

                for (int offset = 0; offset < weakCount; offset ++) {
                    if (point < weakPoints[start + offset]) {
                        if (count >= distances.length) {
                            count = Integer.MAX_VALUE;
                            break;
                        }
                        point = weakPoints[start + offset] + friends.get(count ++);
                    }
                }

                minManPower = Math.min(minManPower, count);
            }

            return minManPower;
        }

        private int[] regulateWeakPoints(int n, int[] weak) {
            int[] temp = new int[weak.length * 2];

            for (int i = 0; i < weak.length; i ++) {
                temp[i] = weak[i];
                temp[i + weak.length] = weak[i] + n;
            }

            return temp;
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 2
        int solution1 = solution.solution(12, new int[]{1, 5, 6, 10}, new int[]{1, 2, 3, 4});
        System.out.println("solution = " + solution1);

        // 1
        int solution2 = solution.solution(12, new int[]{1, 3, 4, 9, 10}, new int[]{3, 5, 7});
        System.out.println("solution = " + solution2);

        // 2
        int solution3 = solution.solution(200, new int[]{0, 100}, new int[]{1, 1});
        System.out.println("solution3 = " + solution3);

    }

}
