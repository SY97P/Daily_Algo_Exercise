package 프로그래머스.lv3;

import java.util.Arrays;

/**
 * 문제요약 <br>
 *<br>
 * 모든 차량이 단속카메라를 한 번은 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지 구하기<br>
 *<br>
 * 제한사항<br>
 *<br>
 * 1 <= 차량 수 <+ 10^4<br>
 * route = [진입지점, 진출지점]<br>
 * 진입, 진출지점에 카메라가 있는것도 카메라를 만난것<br>
 * -3 * 10^4 <= 진입, 진출 지점 <= 3 * 10^4<br>
 *<br>
 * 해결전략<br>
 *<br>
 * route를 진출지점 기준 오름차순 정렬<br>
 * 항상 진출지점에 카메라 설치한다고 생각<br>
 * 최근 설치지점 < route 진입 시점 -> 카메라 추가 설치<br>
 *
 */

public class 단속카메라 {

    private static class Solution {
        public int solution(int[][] routes) {
            int answer = 0;

            Arrays.sort(routes, (a, b) -> Integer.compare(a[1], b[1]));

            int currentPoint = -3 * (int) 1e4;

            for (int[] route : routes) {
                if (currentPoint < route[0]) {
                    answer ++;
                    currentPoint = route[1];
                }
            }

            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 2
        int solution1 = solution.solution(new int[][]{new int[]{-20, -15}, new int[]{-14, -5}, new int[]{-18, -13}, new int[]{-5, -3}});
        System.out.println("solution1 = " + solution1);

    }

}
