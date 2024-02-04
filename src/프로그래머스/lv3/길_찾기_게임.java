package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 문제요약<br>
 *<br>
 * 트리의 모든 노드 x, y 좌표는 정수<br>
 * 모든 노드는 서로 다른 x 값<br>
 * 같은 레벨의 노드는 모두 같은 y 값<br>
 * 자식노드 y < 부모노드 y<br>
 * 왼쪽 서브트리 x < 노드 x < 오른쪽 서브트리 x<br>
 *<br>
 * 이런 조건의 이진트리가 있을떼 전위순회, 후위순회한 결과 구하기<br>
 *<br>
 * 제한사항<br>
 *<br>
 * 각 노드 정보는 순서내돌 주어짐 (1부터 시작하는 인덱스 가짐)<br>
 * 1 <= 노드 수 <= 10^4<br>
 * 노드 : [x 좌표, y 좌표]<br>
 * 0 <= 노드 좌표 <= 10^5<br>
 * 트리 깊이 <= 10^3<br>
 * 잠소된 노드가 주어지는 경우는 없음<br>
 *<br>
 * 해결전략<br>
 *<br>
 * y 좌표 내림차순 정렬<br>
 * 최고 노드를 루트로 하위 트리 구분<br>
 *  왼쪽 서브트리 : 루트보다 x 값 작은 애들<br>
 *  오른쪽 서브트리 : 루트보다 x 값 큰 애들<br>
 * 전위 / 후위에 따라 인덱스 저장<br>
 *  전위 : V L R<br>
 *  후위 : L R V<br>
 *
 */

public class 길_찾기_게임 {

    private static class Solution {

        private List<Integer> prevOrder = new ArrayList<>();
        private List<Integer> postOrder = new ArrayList<>();

        public int[][] solution(int[][] nodeinfo) {
            List<NodeInfo> nodeInfos = new ArrayList<>();

            for (int i = 0; i < nodeinfo.length; i ++) {
                nodeInfos.add(new NodeInfo(i + 1, nodeinfo[i][0], nodeinfo[i][1]));
            }

            nodeInfos.sort((a, b) -> Integer.compare(b.y, a.y));

            playGame(nodeInfos);

            int[][] answer = new int[2][nodeinfo.length];
            answer[0] = prevOrder.stream().mapToInt(Integer::intValue).toArray();
            answer[1] = postOrder.stream().mapToInt(Integer::intValue).toArray();
            return answer;
        }

        private void playGame(List<NodeInfo> nodeInfos) {
            NodeInfo root = nodeInfos.get(0);
            List<NodeInfo> leftTree = getLeftTree(root, nodeInfos);
            List<NodeInfo> rightTree = getRightTree(root, nodeInfos);

            prevOrder.add(root.idx);
            if (!leftTree.isEmpty()) {
                playGame(leftTree);
            }
            if (!rightTree.isEmpty()) {
                playGame(rightTree);
            }
            postOrder.add(root.idx);
        }

        private List<NodeInfo> getLeftTree(NodeInfo root, List<NodeInfo> nodeInfos) {
            return nodeInfos.stream()
                    .filter(nodeInfo -> nodeInfo.x < root.x)
                    .collect(Collectors.toList());
        }

        private List<NodeInfo> getRightTree(NodeInfo root, List<NodeInfo> nodeInfos) {
            return nodeInfos.stream()
                    .filter(nodeInfo -> nodeInfo.x > root.x)
                    .collect(Collectors.toList());
        }

        private static class NodeInfo {
            int idx;
            int x;
            int y;

            NodeInfo(int idx, int x, int y) {
                this.idx = idx;
                this.x = x;
                this.y = y;
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]
        int[][] solution1 = solution.solution(new int[][]{new int[]{5, 3}, new int[]{11, 5}, new int[]{13, 3}, new int[]{3, 5}, new int[]{6, 1}, new int[]{1, 3}, new int[]{8, 6}, new int[]{7, 2}, new int[]{2, 2}});
        System.out.println("solution1 = " + Arrays.deepToString(solution1));
    }

}
