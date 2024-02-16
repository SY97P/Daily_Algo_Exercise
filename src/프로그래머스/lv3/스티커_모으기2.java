package 프로그래머스.lv3;

import java.util.Arrays;

/**
 * 문제요약
 *
 * 원형 리스트 형태의 스티커에서 몇 장의 스티커를 띄어 그 안에 적힌 숫자 합이 최대가 될때의 값 구하기
 * 스티커 한 장을 뜯으면 양쪽 인접 스티커는 사용할 수 없음
 * 원형이라 첫 원소와 마지막 원소가 붙어있는 것으로 생각
 *
 * 제한사항
 *
 * 1 <= 스티커 길이 <= 10^5
 * 1 <= 스티커 값 <= 100
 *
 * 해결전략
 *
 * DP
 * 첫 원소를 가질 때의 최대합 구하기
 * 마지막 원소를 가질 때의 최대합 구하기
 * 두 값을 비교해서 더 큰 값 반환하기
 */

public class 스티커_모으기2 {

    private static class Solution {
        public int solution(int sticker[]) {
            int n = sticker.length;

            if (n <= 2) {
                return getMax(sticker);
            }

            int withFirst = getSumOfSticker(Arrays.copyOfRange(sticker, 0, n - 1));
            int withLast = getSumOfSticker(Arrays.copyOfRange(sticker, 1, n));

            return Math.max(withFirst, withLast);
        }

        private int getMax(int[] sticker) {
            return Arrays.stream(sticker)
                    .boxed()
                    .mapToInt(Integer::intValue)
                    .max()
                    .orElse(0);
        }

        private int getSumOfSticker(int[] array) {
            int[] dp = new int[array.length];

            dp[0] = array[0];
            dp[1] = Math.max(array[0], array[1]);

            for (int i = 2; i < array.length; i ++) {
                dp[i] = Math.max(dp[i - 1], dp[i - 2] + array[i]);
            }

            return getMax(dp);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 36
//        int solution1 = solution.solution(new int[]{14, 6, 5, 11, 3, 9, 2, 10});
//        System.out.println("solution = " + solution1);
//
//        // 8
//        int solution2 = solution.solution(new int[]{1, 3, 2, 5, 4});
//        System.out.println("solution = " + solution2);
//
//        // 2
//        int solution3 = solution.solution(new int[]{2});
//        System.out.println("solution = " + solution3);

        // 13
        int solution4 = solution.solution(new int[]{4, 3, 2, 9, 4});
        System.out.println("solution4 = " + solution4);

    }

}
