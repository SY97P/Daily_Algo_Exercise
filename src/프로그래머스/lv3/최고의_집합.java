package 프로그래머스.lv3;

import java.util.Arrays;

/**
 * 문제요약
 *
 * 자연수 N 개로 구성된 중복집합 중 두 조건을 만족하는 최고의 집합 구하기
 * 최고의 집합 조건
 * 1. 각 원소 합이 S
 * 2. 각 원소 곱이 최대
 *
 * 제한사항
 *
 * 오름차순 정렬된 1차원 배열
 * 최고의 집합이 존재하지 않는 경우에는 [-1] 반환
 * 1 <= n <= 10^4
 * 1 <= s <= 10^8
 *
 * 해결전략
 *
 * 자연수 n 개의 합이 S 이하인 수로 초기화
 * 집합의 합이 S보다 작은 경우에는 골고루 1씩 증가
 *
 * 문제해결
 *
 * Q. 효율성 시간초과
 * 집합 초기값과 S 차이 만큼 반복하면서 값을 갱신하는 과정에서 시간초과가 발생하는 것으로 보임
 * 두 값의 차이만큼에 해당되는 인덱스까지 한번에 값을 올려 값을 갖도록 하면 될 것 같음
 */

public class 최고의_집합 {

    private static class Solution {
        public int[] solution(int n, int s) {
            int[] answer = new int[n];

            int initSumValue = (s / n) * n;
            int diff = s - initSumValue;

            for (int i = 0; i < n; i ++) {
                if (i >= n - diff) {
                    answer[i] = s / n + 1;
                } else {
                    answer[i] = s / n;
                }
            }

            for (int i = 0; i < n; i ++) {
                if (answer[i] == 0) {
                    answer = new int[]{-1};
                    break;
                }
            }

            return answer;
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // [-1]
        int[] answer1 = s.solution(2, 1);
        System.out.println("answer = " + Arrays.toString(answer1));

        // [4, 5]
        int[] answer2 = s.solution(2, 9);
        System.out.println("answer = " + Arrays.toString(answer2));

        // [4, 4]
        int[] answer3 = s.solution(2, 8);
        System.out.println("answer = " + Arrays.toString(answer3));

        // [1, 1, 1, 2]
        int[] answer4 = s.solution(4, 5);
        System.out.println("answer = " + Arrays.toString(answer4));

        // [2, 3, 3]
        int[] answer5 = s.solution(3, 8);
        System.out.println("answer = " + Arrays.toString(answer5));

    }

}
