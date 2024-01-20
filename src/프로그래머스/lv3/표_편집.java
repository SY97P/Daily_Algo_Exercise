package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Stack;

/**
 * 문제요약<br>
 *
 * 0행 부터 시작하는 표가 있음<br>
 * 한 번에 한 행만 선택 가능<br>
 * 명령어<br>
 *  U X : 현재 칸에서 X 칸 위에 있는 행 선택<br>
 *  D X : 현재 칸에서 X 칸 아래 있는 행 선택<br>
 *  C   : 현재 행 삭제 후 바로 아래 행 선택. 삭제된 행이 마지막 행인 경우 바로 윗 행 선택<br>
 *  Z   : 최근 삭제된 행 복구. 선택한 행은 바뀌지 않음<br>
 * 삭제되지 않은 행은 O, 삭제된 행은 X로 표시해 문자열 형태로 반환하는 문제<br>
 *<br>
 * 제한사항<br>
 *
 * 5 <= n <= 10^6<br>
 * 0 <= k < n<br>
 * 1 <= cmd 길이 <= 2 * 10^6<br>
 * 1 <= x <= 3 * 10^6<br>
 * sum(x) <= 10^6<br>
 * 모든 표가 제거되는 경우는 주어지지 않음<br>
 * 표 범위 벗어나는 이동은 주어지지 않음<br>
 * 복구될 행이 없을때 Z 명령어가 나오지 않음<br>
 *<br>
 * 해결전략<br>
 *
 * DP 혹은 연결리스트 구현<br>
 * Node = [이전노드, 이후노드]<br>
 * Node 로 구성된 연결리스트 구현해서 명령어 수행<br>
 * U -> 이전노드가 null 이 아닌 상태로 x 만큼 pointer 를 이전노드로 이동<br>
 * D -> 이후노드가 null 이 아닌 상태로 x 만큼 pointer 를 이전노드로 이동<br>
 * C -> 현재노드 스택 추가, 현재 노드 X 표시, 이전노드.이후노드 = 이후노드, 이후노드.이전노드 = 이전노드<br>
 * Z -> C 작업 반대로.<br>
 *
 */

public class 표_편집 {

    private static class Solution {

        private static class Node {
            Integer prevIndex;
            Integer postIndex;

            Node (Integer prevIndex, Integer postIndex) {
                this.prevIndex = prevIndex;
                this.postIndex = postIndex;
            }
        }

        private int n;
        private List<Node> list;
        private Stack<Integer> stack;
        private char[] status;
        private int pointer;

        public String solution(int _n, int k, String[] cmds) {
            n = _n;
            pointer = k;
            stack = new Stack<>();
            status = new char[n];
            list = new ArrayList<>();
            for (int i = 0; i < n; i ++) {
                status[i] = 'O';
                list.add(new Node(i - 1 < 0 ? null : i - 1, i + 1 >= n ? null : i + 1));
            }

            for (String cmd : cmds) {
                String[] split = cmd.split(" ");
                if (Objects.equals(split[0], "U")) {
                    up(Integer.parseInt(split[1]));
                } else if (Objects.equals(split[0], "D")) {
                    down(Integer.parseInt(split[1]));
                } else if (Objects.equals(split[0], "C")) {
                    clear();
                } else {
                    revive();
                }
            }

            return String.valueOf(status);
        }

        private void up(int x) {
            int count = 0;
            while (count < x) {
                Integer prevIndex = list.get(pointer).prevIndex;
                if (prevIndex == null) {
                    break;
                }
                pointer = prevIndex;
                count ++;
            }
        }

        private void down(int x) {
            int count = 0;
            while (count < x) {
                Integer postIndex = list.get(pointer).postIndex;
                if (postIndex == null) {
                    break;
                }
                pointer = postIndex;
                count ++;
            }
        }

        private void clear() {
            stack.add(pointer);
            status[pointer] = 'X';
            Integer prevIndex = list.get(pointer).prevIndex;
            Integer postIndex = list.get(pointer).postIndex;
            if (prevIndex != null) {
                pointer = prevIndex;
                list.get(prevIndex).postIndex = postIndex;
            }
            if (postIndex != null) {
                pointer = postIndex;
                list.get(postIndex).prevIndex = prevIndex;
            }
        }

        private void revive() {
            Integer pop = stack.pop();
            status[pop] = 'O';
            Integer prevIndex = list.get(pop).prevIndex;
            Integer postIndex = list.get(pop).postIndex;
            if (prevIndex != null) {
                list.get(prevIndex).postIndex = pop;
            }
            if (postIndex != null) {
                list.get(postIndex).prevIndex = pop;
            }
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // OOOOXOOO
        String solution1 = solution.solution(8, 2, new String[]{"D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"});
        System.out.println("solution1 = " + solution1);

        // OOXOXOOO
        String solution2 = solution.solution(8, 2, new String[]{"D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"});
        System.out.println("solution2 = " + solution2);

    }

}
