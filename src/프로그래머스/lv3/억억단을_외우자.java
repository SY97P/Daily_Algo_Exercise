package 프로그래머스.lv3;

import java.util.Arrays;

/**
 * 문제요약
 * <p>
 * - s <= e (<= 5 * 10^6)
 * - e >= t >= s 구간 최소값인 최빈수
 * - len(starts) <= min(5 * 10^6, 10 ^ 5)
 * - starts 에 중복 요소 없음
 * <p>
 * 해결전략
 * <p>
 * 1. 각 숫자별 빈도수 구하기
 *  - i * j (i == j) -> count[i*j] ++
 *  - i * j (i != j) -> count[i*j] += 2
 * 2. 각 숫자 ~ e 구간 최빈수 구하기 (최소값이 되도록)
 * 3. 정답 배열 구하기
 */

public class 억억단을_외우자 {

    private static class Solution {

        public int[] solution(int e, int[] starts) {
            int[] frequency = getFrequency(e);
            int[] mostFrequentArray = getMostFrequentArray(frequency);

            return getAnswer(mostFrequentArray, starts);
        }

        private int[] getAnswer(int[] mostFrequentArray, int[] starts) {
            return Arrays.stream(starts)
                    .map(s -> mostFrequentArray[s])
                    .toArray();
        }

        private int[] getMostFrequentArray(int[] frequency) {
            int length = frequency.length;
            int maxFrequentValue = Integer.MIN_VALUE;
            int[] mostFrequentArray = new int[length];

            for (int i = length - 1; i >= 1; i --) {
                if (frequency[i] >= maxFrequentValue) {
                    maxFrequentValue = frequency[i];
                    mostFrequentArray[i] = i;
                } else {
                    mostFrequentArray[i] = mostFrequentArray[i + 1];
                }
            }

            return mostFrequentArray;
        }

        private int[] getFrequency(int e) {
            int[] countArray = new int[e + 1];

            for (int i = 1; i <= (int) Math.sqrt(e); i ++) {
                countArray[i * i] ++;
                for (int j = i + 1; i * j <= e; j ++) {
                    countArray[i * j] += 2;
                }
            }

            return countArray;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // [6, 6, 8]
        int[] solution1 = solution.solution(8, new int[]{1, 3, 7});
        System.out.println("solution1 = " + Arrays.toString(solution1));
    }

}
