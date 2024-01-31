package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

/**
 * 문제요약<br>
 *<br>
 * n 개 노드 그래프<br>
 * 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하기<br>
 *<br>
 * 제한사항<br>
 *<br>
 * 2 <= 노드 개수 <= 20_000<br>
 * 1 <= 간선 개수 <= 50_000<br>
 * [a, b] : a <-> b 간선 존재<br>
 *<br>
 * 해결전략 (다익스트라)<br>
 *<br>
 * 별거 없는 다익스트라 문제
 */

public class 가장_먼_노드 {

    private static class Solution {
        public int solution(int n, int[][] edge) {
            List<List<Integer>> adj = initAdj(n, edge);

            int[] dp = dijkstra(n, adj);

            int maxValue = Arrays.stream(dp)
                    .boxed()
                    .mapToInt(Integer::intValue)
                    .filter(value -> value != Integer.MAX_VALUE)
                    .max()
                    .orElse(0);

            return (int) Arrays.stream(dp)
                    .filter(value -> value == maxValue)
                    .count();
        }

        private int[] dijkstra(int n, List<List<Integer>> adj) {
            int[] dp = new int[n + 1];

            for (int i = 2; i <= n; i ++) {
                dp[i] = Integer.MAX_VALUE;
            }

            PriorityQueue<int[]> q = new PriorityQueue<>((a, b) -> a[0] - b[0]);
            q.add(new int[]{0, 1});

            while (!q.isEmpty()) {
                int[] info = q.poll();

                if (info[0] > dp[info[1]]) {
                    continue;
                }

                for (int next : adj.get(info[1])) {
                    if (dp[next] > info[0] + 1) {
                        dp[next] = info[0] + 1;
                        q.add(new int[]{dp[next], next});
                    }
                }
            }
            return dp;
        }

        private List<List<Integer>> initAdj(int n, int[][] edges) {
            List<List<Integer>> temp = new ArrayList<>();

            for (int i = 0; i <= n; i ++) {
                temp.add(new ArrayList<>());
            }

            for (int[] edge: edges) {
                temp.get(edge[0]).add(edge[1]);
                temp.get(edge[1]).add(edge[0]);
            }

            return temp;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // 3
        int solution1 = solution.solution(6, new int[][]{new int[]{3, 6}, new int[]{4, 3}, new int[]{3, 2}, new int[]{1, 3}, new int[]{1, 2}, new int[]{2, 4}, new int[]{5, 2}});
        System.out.println("solution1 = " + solution1);

    }

}
