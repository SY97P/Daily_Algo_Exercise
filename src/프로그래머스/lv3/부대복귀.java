package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

/**
 * 문제요약
 * <p>
 * - n : 지역 수 (3 <= n <= 10^5)
 * - roads : 길 정보 (2 <= len(roads) <= 5*10^5)
 * - sources : 부대원 시작위치 (1 <= len(sources) <= 500)
 * - destination : 복귀 지역
 * - sources 순서대로 부대복귀 최단시간 구하기
 * - 복귀 불가인 경우 -1 반환
 * <p>
 * 해결전략
 * <p>
 * - 다익스트라 알고리즘
 * - destination에서 sources로 가는 최단거리 구하기
 *
 * * PriorityQueue 는 내부적으로 Heap 자료구조를 사용함!
 */

public class 부대복귀 {

    private static class Solution {

        private class Path {
            int node;
            int cost;

            Path (int node, int cost) {
                this.node = node;
                this.cost = cost;
            }
        }

        public int[] solution(int n, int[][] roads, int[] sources, int destination) {
            List<List<Integer>> adj = initAdj(n, roads);
            int[] spentTimes = initSpentTimes(n);
            PriorityQueue<Path> pq = new PriorityQueue<>((p1, p2) -> Integer.compare(p1.cost, p2.cost));

            spentTimes[destination] = 0;
            pq.add(new Path(destination, 0));

            while (!pq.isEmpty()) {
                Path path = pq.poll();

                for (int next : adj.get(path.node)) {
                    if (spentTimes[next] <= path.cost + 1) {
                        continue;
                    }
                    spentTimes[next] = path.cost + 1;
                    pq.add(new Path(next, path.cost + 1));
                }
            }

            return Arrays.stream(sources)
                    .map(source -> {
                        if (spentTimes[source] == Integer.MAX_VALUE)
                            return -1;
                        return spentTimes[source];
                    })
                    .toArray();
        }

        private int[] initSpentTimes(int n) {
            int[] spentTimes = new int[n + 1];
            for (int i = 0; i <= n; i ++) {
                spentTimes[i] = Integer.MAX_VALUE;
            }
            return spentTimes;
        }

        private List<List<Integer>> initAdj(int n, int[][] roads) {
            List<List<Integer>> adj = new ArrayList<>();
            for (int i = 0; i <= n; i ++) {
                adj.add(new ArrayList<>());
            }

            for (int[] road : roads) {
                adj.get(road[0]).add(road[1]);
                adj.get(road[1]).add(road[0]);
            }

            return adj;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // [1, 2]
        int[] solution1 = solution.solution(3, new int[][]{{1, 2}, {2, 3}}, new int[]{2, 3}, 1);
        System.out.println("solution1 = " + Arrays.toString(solution1));

        // [2, -1, 0]
        int[] solution2 = solution.solution(5, new int[][]{{1, 2}, {1, 4}, {2, 4}, {2, 5}, {4, 5}}, new int[]{1, 3, 5}, 5);
        System.out.println("solution2 = " + Arrays.toString(solution2));
    }

}
