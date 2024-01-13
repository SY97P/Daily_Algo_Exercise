package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

/**
 * 문제요약
 * <p>
 * - 출입구A -> 산봉우리 -> 출입구A 구간을 이동하면서 얻은 최단 intensity 구하기
 * - 산봉우리는 반드시 하나만 지나야함
 * - (입구 = 출구)이어야 함
 * - 2 <= 노드 개수 <= 5 * 10^4
 * - 최소 intensity가 같은 경로는 산봉우리 번호가 가장 낮은 코드 선택
 * - [산봉우리 번호, 최소 intensity]
 * <p>
 * 해결전략 (다익스트라)
 * <p>
 * 1. 산봉우리 내림차순 정렬
 * 2. 각 산봉우리 별로 각 출입구에 대해서 다익스트라
 *  2-1. 경로 상에 다른 산봉우리가 들어가지 않도록 방어
 *  2-2. 경로 상에 서로 다른 출입구가 들어가지 않도록 방어
 * 3. 현재경로의 intensity가 최소 intensity 보다 작거나 같으면 갱신
 *  3-1. 산봉우리 번호를 기준으로 내림차순으로 정렬했기 때문
 */

public class 등산코스_정하기 {

    private static class Solution {

        private static class Node implements Comparable<Node> {
            int number;
            int intensity;

            Node (int number, int intensity) {
                this.number = number;
                this.intensity = intensity;
            }

            @Override
            public int compareTo(Node o) {
                return Integer.compare(this.intensity, o.intensity);
            }
        }

        private List<Map<Integer, Integer>> adj;

        public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
            initAdj(n, paths);

            PriorityQueue<Node> pq = new PriorityQueue<>();
            int[] dp = new int[n + 1];

            for (int i = 0; i <= n; i ++) {
                dp[i] = Integer.MAX_VALUE;
            }
            for (int gate : gates) {
                dp[gate] = 0;
                pq.add(new Node(gate, dp[gate]));
            }

            while (!pq.isEmpty()) {
                Node node = pq.poll();

                if (contains(node.number, summits) || dp[node.number] < node.intensity) {
                    continue;
                }

                for (int nextNode : adj.get(node.number).keySet()) {
                    int intensity = Math.max(dp[node.number], adj.get(node.number).get(nextNode));
                    if (dp[nextNode] > intensity) {
                        dp[nextNode] = intensity;
                        pq.add(new Node(nextNode, dp[nextNode]));
                    }
                }
            }

            Arrays.sort(summits);
            int[] answer = new int[]{Integer.MAX_VALUE, Integer.MAX_VALUE};

            for (int summit : summits) {
                if (answer[1] > dp[summit]) {
                    answer = new int[]{summit, dp[summit]};
                }
            }

            return answer;
        }

        private boolean contains(int number, int[] array) {
            for (int a : array) {
                if (a == number) {
                    return true;
                }
            }
            return false;
        }

        private void initAdj(int n, int[][] paths) {
            adj = new ArrayList<>();
            for (int i = 0; i <= n; i ++) {
                adj.add(new HashMap<>());
            }

            for (int[] path : paths) {
                adj.get(path[0]).put(path[1], path[2]);
                adj.get(path[1]).put(path[0], path[2]);
            }
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // [5, 3]
        int[] solution1 = solution.solution(6,
                new int[][]{{1, 2, 3}, {2, 3, 5}, {2, 4, 2}, {2, 5, 4}, {3, 4, 4}, {4, 5, 3}, {4, 6, 1}, {5, 6, 1}},
                new int[]{1, 3}, new int[]{5});
        System.out.println("solution1 = " + Arrays.toString(solution1));

        // [3, 4]
        int[] solution2 = solution.solution(7,
                new int[][]{{1, 4, 4}, {1, 6, 1}, {1, 7, 3}, {2, 5, 2}, {3, 7, 4}, {5, 6, 6}},
                new int[]{1}, new int[]{2, 3, 4});
        System.out.println("solution2 = " + Arrays.toString(solution2));

        // [5, 1]
        int[] solution3 = solution.solution(7,
                new int[][]{{1, 2, 5}, {1, 4, 1}, {2, 3, 1}, {2, 6, 7}, {4, 5, 1}, {5, 6, 1}, {6, 7, 1}},
                new int[]{3, 7}, new int[]{1, 5});
        System.out.println("solution3 = " + Arrays.toString(solution3));

        // [5, 6]
        int[] solution4 = solution.solution(5,
                new int[][]{{1, 3, 10}, {1, 4, 20}, {2, 3, 4}, {2, 4, 6}, {3, 5, 20}, {4, 5, 6}}, new int[]{1, 2},
                new int[]{5});
        System.out.println("solution4 = " + Arrays.toString(solution4));
    }

}
