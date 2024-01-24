package 프로그래머스.lv3;

/**
 * 문제요약 <br>
 *<br>
 * 인접한 두 풍선 중 하나를 터트림<br>
 * 단, 번호가 더 작은 풍선 터트리는건(조커) 단 한 번만 가능함<br>
 * 위 과정을 풍선이 하나 남을때까지 반복<br>
 * 최후까지 살아남을 수 있는 풍선의 개수 구하기<br>
 *<br>
 * 제한사항<br>
 *<br>
 * 1 <= 풍선 개수 <= 10^6<br>
 * - 10^9 <= 풍선 값 <= 10^9<br>
 * 주어지는 풍선 값은 모두 다름<br>
 *<br>
 * 해결전략<br>
 *<br>
 * 왼쪽, 오른쪽 각 방향에서 조커 안 쓰고 살아남는 풍선(해당 구간에서 가장 작은 값) 구함<br>
 * (원본 풍선 값 > 왼쪽, 오른쪽 풍선값) 이면 조커를 써도 해당 풍선은 살아남을 수 없음<br>
 * 이런 경우를 제외하고 카운트<br>
 * 맨 마지막 풍선 두 개는 어떻게 해도 살아남을 수 있음<br>
 *
 */

public class 풍선_터트리기 {

    private static class Solution {
        public int solution(int[] a) {
            int n = a.length;

            int[] l = a.clone();
            int[] r = a.clone();

            for (int i = 1; i < n; i ++) {
                l[i] = Math.min(l[i], l[i - 1]);
                r[n - i - 1] = Math.min(r[n - i - 1], r[n - i]);
            }

            int answer = 2;

            for (int i = 1; i < n - 1; i ++) {
                if (a[i] > l[i] && a[i] > r[i]) {
                    continue;
                }
                answer ++;
            }

            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 3
        int solution1 = solution.solution(new int[]{9, -1, -5});
        System.out.println("solution1 = " + solution1);

        // 6
        int solution2 = solution.solution(new int[]{-16, 27, 65, -2, 58, -92, -71, -68, -61, -33});
        System.out.println("solution2 = " + solution2);

    }

}
