package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * 문제요약<br>
 *<br>
 * 토큰 숫자와 사칙연산만으로 주어진 숫자 표현<br>
 * 표현 가능한 모든 방법 중 토큰 숫자를 최소한으로 사용하는 횟수 구하기<br>
 *<br>
 * 제한사항<br>
 *<br>
 * 1 <= 토큰 숫자 <= 9<br>
 * 1 <= 만들고 싶은 숫자 <= 32_000<br>
 * 괄호, 사칙연산만 가능 (나누기 연산에서 나머지 무시)<br>
 * 최솟값이 8보다 크면 -1 반환<br>
 *<br>
 * 해결전략<br>
 *<br>
 * 토큰 숫자를 사용한 횟수로 만들 수 있는 모든 수를 집합에 담음<br>
 * set1, set2, set3, ... set8 (9번 사용하면 -1 이므로 없어도 됨)<br>
 *<br>
 * 1. 토큰 숫자를 이어붙인 값을 각 집합에 초기값으로 담음<br>
 * 2. 다음 집합 구하기<br>
 *  set2 = set1 사칙연산 set1<br>
 *  set3 = set1 사칙연산 set2 + set2 사칙연산 set1<br>
 *  set4 = set1 사칙연산 set3 + set2 사칙연산 set2 + set3 사칙연산 set1<br>
 *  ...<br>
 * 3. 각 집합 구할때 주어진 숫자 나오면 해당 회차 반환<br>
 *  끝까지 구해지지 않으면 -1 반환<br>
 *<br>
 * 신경쓸거<br>
 *<br>
 * 토큰 숫자를 이어붙여서 만든 숫자 중에서 number 와 같은 숫자가 있을 수 있음<br>
 * n == number 만 신경써서는 안 됨<br>
 *
 */

public class N으로_표현 {

    private static class Solution {

        private static final int BOUND = 9;

        public int solution(int N, int number) {

            List<Set<Long>> numberSets = new ArrayList<>();

            for (int i = 0; i < BOUND; i ++) {
                numberSets.add(new HashSet<>());
                Long l = makeNTimeNumber(N, i);

                if (l != null) {
                    if (l == number) {
                        return i;
                    }

                    numberSets.get(i).add(l);
                }
            }

            for (int k = 2; k < BOUND; k ++) {
                for (int i = 1; i < k; i ++) {
                    Set<Long> setA = numberSets.get(i);
                    Set<Long> setB = numberSets.get(k - i);

                    Set<Long> targetSet = getTargetSet(setA, setB);

                    if (targetSet.contains((long) number)) {
                        return k;
                    }

                    for (long target : targetSet) {
                        numberSets.get(k)
                                .add(target);
                    }
                }
            }

            return -1;
        }

        private Set<Long> getTargetSet(Set<Long> setA, Set<Long> setB) {
            Set<Long> targetSet = new HashSet<>();
            for (long aNumber : setA) {
                for (Long bNumber : setB) {
                    targetSet.add(aNumber + bNumber);
                    targetSet.add(aNumber - bNumber);
                    targetSet.add(aNumber * bNumber);
                    if (bNumber != 0) {
                        targetSet.add(aNumber / bNumber);
                    }
                }
            }
            return targetSet;
        }

        private Long makeNTimeNumber(int tokenNumber, int time) {
            String number = String.valueOf(tokenNumber)
                    .repeat(time);

            if (number.isBlank()) {
                return null;
            }

            return Long.parseLong(number);
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 4
        int solution1 = solution.solution(5, 12);
        System.out.println("solution1 = " + solution1);

        // 3
        int solution2 = solution.solution(2, 11);
        System.out.println("solution2 = " + solution2);

    }

}
