package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.List;

/**
 * 해결 전략
 * <p>
 * 1. 원본 수열에 펄스 수열 곱하기
 * 2. 펄스된 수열의 누적합 구하기
 * 3. 정답 = max(누적합) - min(누적합)
 * <p></p>
 * 펄스 수열 두 종류는 서로 반대 부호를 갖게되므로, 결과는 절대값을 씌운것과 다름없음
 * 따라서 두 펄스 수열을 모두 적용할 필요 없음
 */

class 연속_펄스_부분_수열의_합 {

    private static class Solution {

        public long solution(int[] sequence) {
            long initialValue = 0L;

            List<Long> result = new ArrayList<>();
            result.add(initialValue);

            long maxValue = initialValue;
            long minValue = initialValue;

            int lastIndex = 0;

            for (int i = 0; i < sequence.length; i ++) {
                int pulse = i % 2 == 0 ? 1 : -1;

                long lastElement = result.get(lastIndex++);

                long cumulativeSumValue = lastElement + pulse * sequence[i];

                result.add(cumulativeSumValue);

                maxValue = Math.max(maxValue, cumulativeSumValue);
                minValue = Math.min(minValue, cumulativeSumValue);
            }

            return maxValue - minValue;
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 10
        long solution1 = solution.solution(new int[]{2, 3, -6, 1, 3, -1, 2, 4});

        System.out.println("solution1 = " + solution1);
    }

}
