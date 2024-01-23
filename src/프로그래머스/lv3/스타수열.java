package 프로그래머스.lv3;

/*
문제요약

주어진 수열의 모든 부분수열 중에 가장 길이가 긴 스타수열 길이 구하기
스타수열이 없다면 0 반환

스타수열 조건
- 짝수 길이 (빈 수열 x)
- 다른 모든 스타수열과 교집합 원소가 하나 이상 반드시 필요
- 스타수열 내 같은 숫자가 있을 수 없음

제한사항

- 1 <= 수열 길이 <= 5 * 10^5
0 <= 수열 내 원소 값 < 수열 길이

해결전략 (카운터, 구현)

수열의 모든 숫자가 수열 내에서 몇번 출현하는지 구하기
출현횟수를 기준으로 내림차순 정렬하여 연산하기
    answer > 출현횟수 인 경우 trunning 하기
해당 수를 기준으로 해당 수가 아닌 다른 수 하나를 더해서 스타수열 만들기
수타수열의 개수를 answer 에 갱신시키기

 */

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.stream.Collectors;

public class 스타수열 {

    private static class Solution {

        public int solution(int[] a) {
            Map<Integer, Integer> counter = getCounterOfArray(a);
            List<Entry<Integer, Integer>> collect = counter.entrySet()
                    .stream()
                    .sorted((entry, anotherEntry) -> Integer.compare(anotherEntry.getValue(), entry.getValue()))
                    .collect(Collectors.toList());

            int answer = 0;
            for (Entry<Integer, Integer> entry : collect) {
                if (answer > entry.getValue()) {
                    continue;
                }

                int index = 0;
                int count = 0;
                while (index < a.length - 1) {
                    if ((a[index] == entry.getKey() && a[index + 1] != entry.getKey()) || (a[index] != entry.getKey() && a[index + 1] == entry.getKey())) {
                        count ++;
                        index += 2;
                    } else {
                        index ++;
                    }
                }
                answer = Math.max(answer, count);
            }

            return answer * 2;
        }

        private Map<Integer, Integer> getCounterOfArray(int[] array) {
            Map<Integer, Integer> map = new HashMap<>();
            for (int a : array) {
                map.put(a, map.getOrDefault(a, 0) + 1);
            }
            return map;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 0
        int solution1 = solution.solution(new int[]{0});
        System.out.println("solution1 = " + solution1);

        // 4
        int solution2 = solution.solution(new int[]{5, 2, 3, 3, 5, 3});
        System.out.println("solution2 = " + solution2);

        // 8
        int solution3 = solution.solution(new int[]{0, 3, 3, 0, 7, 2, 0, 2, 2, 0});
        System.out.println("solution3 = " + solution3);

        // 0
        int solution4 = solution.solution(new int[]{5, 5, 5, 5, 5, 5});
        System.out.println("solution4 = " + solution4);

    }

}
