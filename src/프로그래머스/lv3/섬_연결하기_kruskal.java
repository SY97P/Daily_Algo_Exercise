package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

/**
 * 문제요약<br>
 * <br>
 * n 개 섬 사이에 다리 건설 비용 costs 주어질때 최소 비용으로 모든 섬 통행가능토록 할때 필요한 최소 비용 구하기<br>
 * 다리를 여러번 건너도 도달할 수만 있으면 통행 가능<br>
 * <br>
 * 제한사항<br>
 * <br>
 * 1 <= 섬 개수 <= 100<br>
 * costs : [u, v, 비용]<br>
 * 중복 연결 주어지지 않음<br>
 * 양방향 그래프<br>
 * 연결할 수 없는 섬은 입력으로 주어지지 않음<br>
 * <br>
 * 해결전략 (MST - 프림)<br>
 * <br>
 * MST 집합을 만들기<br>
 * 모든 노드가 MST에 존재하도록 연산<br>
 * 현재 MST에 있는 노드와 연결된 모든 비MST 노드 중에서 가장 연결비용이 작은 것을 선택<br>
 *  costs 를 비용기준 오름차순 정렬해야 함.<br>
 * 모든 노드가 MST 에 있게 되면 현재까지 모든 비용을 더해서 반환<br>
 *
 * Kruskal 알고리즘
 *
 * O(ElogE) -> E < V 이면 이득
 * 유니온-파인드 알고리즘 활용
 *
 */

public class 섬_연결하기_kruskal {

    private static class Solution {

        private int[] parent;

        public int solution(int n, int[][] costs) {
            int answer = 0;

            parent = new int[n];
            for (int i = 0; i < n; i ++) {
                parent[i] = i;
            }

            Arrays.sort(costs, (a, b) -> Integer.compare(a[2], b[2]));

            for (int[] cost : costs) {
                int u = cost[0];
                int v = cost[1];
                int c = cost[2];

                if (find(u) != find(v)) {
                    answer += c;
                    union(u, v);
                }
            }

            return answer;
        }

        private int find(int num) {
            if (parent[num] != num) {
                parent[num] = find(parent[num]);
            }
            return parent[num];
        }

        private void union(int a, int b) {
            int fa = find(a);
            int fb = find(b);

            if (fa < fb) {
                parent[fb] = fa;
            } else if (fa > fb) {
                parent[fa] = fb;
            }
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 4
        int solution1 = solution.solution(4, new int[][]{new int[]{0, 1, 1}, new int[]{0, 2, 2}, new int[]{1, 2, 5}, new int[]{1, 3, 1}, new int[]{2, 3, 8}});
        System.out.println("solution1 = " + solution1);

        // 15
        int solution2 = solution.solution(5, new int[][]{new int[]{0, 1, 5}, new int[]{1, 2, 3}, new int[]{2, 3, 3}, new int[]{3, 1, 2}, new int[]{3, 0, 4}, new int[]{2, 4, 6}, new int[]{4, 0, 7}});
        System.out.println("solution2 = " + solution2);

    }

}
