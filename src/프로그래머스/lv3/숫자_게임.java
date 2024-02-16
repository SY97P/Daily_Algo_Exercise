package 프로그래머스.lv3;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 문제요약<br>
 *<br>
 * 2*n 명의 사원이 n 명씩 팀 구성 (A팀, B팀)<br>
 * 모든 사원이 무작위로 자연수 하나씩 부여<br>
 * 각 사원 한 번씩 경기 수행<br>
 * 각 경기 당 각 팀에서 한 명씩 나와 서로의 수 공개<br>
 * 숫자가 큰 쪽이 승리 (승리팀은 승점 1점)<br>
 * 숫자가 같은 경우 둘 다 승점 얻지 못함<br>
 * A팀이 해당 팀 각 사원의 번호를 미리 정해서 알려줬을때, B 팀이 최고 점수 차이로 이길 수 있을때의 승점 구하기<br>
 *<br>
 * 제한사항<br>
 *<br>
 * 1 <= A, B 길이 <= 10^5<br>
 * 1 <= 숫자 <= 10^9<br>
 *<br>
 * 해결전략<br>
 *<br>
 * 그리디<br>
 * 이긴다면 이길 수 있는 숫자 중에서 최소인 값을 내기<br>
 * 진다면 확실하게 가장 낮은 값을 내기<br>
 *<br>
 * A팀을 내림차순 정렬<br>
 * B팀도 내림차순 정렬<br>
 *<br>
 * i, j : B팀 큰 수 인덱스, B팀 작은 수 인덱스<br>
 * A 내림차순 순서대로 순회하면서 이길 수 있으면 i 늘리기<br>
 * 지거나 비기는 경우에는 j 낮추기<br>
 *<br>
 */

public class 숫자_게임 {

    private static class Solution {
        public int solution(int[] A, int[] B) {
            int answer = 0;

            List<Integer> alist = Arrays.stream(A)
                    .boxed()
                    .collect(Collectors.toList());
            List<Integer> blist = Arrays.stream(B)
                    .boxed()
                    .collect(Collectors.toList());

            Comparator<Integer> comparator = (a, b) -> b - a;

            alist.sort(comparator);
            blist.sort(comparator);

            int i = 0;
            int j = blist.size();

            for (int a : alist) {
                if (a < blist.get(i)) {
                    answer ++;
                    i ++;
                } else {
                    j --;
                }
            }

            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 3
        int solution1 = solution.solution(new int[]{5, 1, 3, 7}, new int[]{2, 2, 6, 8});
        System.out.println("solution = " + solution1);

        // 0
        int solution2 = solution.solution(new int[]{2, 2, 2, 2}, new int[]{1, 1, 1, 1});
        System.out.println("solution = " + solution2);

    }

}
