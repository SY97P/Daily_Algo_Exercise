package 프로그래머스.lv3;

import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

/**
 * 문제요약
 * <p>
 * - 왼손 시작위치 : 4 / 오른손 시작위치 : 6 - 제자리 다시 누르기 : 1 - 상하좌우 인접 이동 : 2 - 대각선 인접 이동 : 3 - 인접하지 않을 경우 위 이동으로 최소가 되도록 이동 - 숫자
 * 문자열 numbers 에 대해서 모든 타이핑을 완료하는데 드는 최소 가중치 비용 구하기
 * <p>
 * 해결전략
 * <p>
 * 1. 각 숫자 이동별 가중치 구하기 2. numbers 각 digit 에 대해서 왼손 혹은 오른손이 이동했을때 구해지는 가중치 결과 구하기 (BFS - Queue 사용) 2.1 두 손가락이 같은 위치에 있을 수
 * 없음 3. Queue.weightSum 의 최소값 구하기
 */

public class 숫자_타자_대회 {

    private static class Solution {

        private static final int[][] weights = {
                {1, 7, 6, 7, 5, 4, 5, 3, 2, 3},
                {7, 1, 2, 4, 2, 3, 5, 4, 5, 6},
                {6, 2, 1, 2, 3, 2, 3, 5, 4, 5},
                {7, 4, 2, 1, 5, 3, 2, 6, 5, 4},
                {5, 2, 3, 5, 1, 2, 4, 2, 3, 5},
                {4, 3, 2, 3, 2, 1, 2, 3, 2, 3},
                {5, 5, 3, 2, 4, 2, 1, 5, 3, 2},
                {3, 4, 5, 6, 2, 3, 5, 1, 2, 4},
                {2, 5, 4, 5, 3, 2, 3, 2, 1, 2},
                {3, 6, 5, 4, 5, 3, 2, 4, 2, 1}};

        private static class Finger {
            int left;
            int right;

            Finger (int left, int right) {
                this.left = left;
                this.right = right;
            }

            @Override
            public boolean equals(Object o) {
                if (this == o) return true;
                if (o == null || getClass() != o.getClass()) return false;
                Finger finger = (Finger) o;
                return left == finger.left && right == finger.right;
            }

            @Override
            public int hashCode() {
                return Objects.hash(left, right);
            }
        }

        public int solution(String numbers) {
            Map<Finger, Integer> map = new HashMap<>();
            map.put(new Finger(4, 6), 0);

            for (char number : numbers.toCharArray()) {
                Map<Finger, Integer> temp = new HashMap<>();
                int digit = number - '0';

                for (Finger finger : map.keySet()) {
                    if (digit == finger.left) {
                        putLeftFinger(finger, digit, map, temp);
                    } else if (digit == finger.right) {
                        putRightFinger(finger, digit, map, temp);
                    } else {
                        putLeftFinger(finger, digit, map, temp);
                        putRightFinger(finger, digit, map, temp);
                    }
                }

                map = temp;
            }

            return map.values()
                    .stream()
                    .min(Integer::compareTo)
                    .orElse(0);
        }

        private void putRightFinger(Finger finger, int digit, Map<Finger, Integer> map, Map<Finger, Integer> temp) {
            Finger nextFinger = new Finger(finger.left, digit);
            int nextWeight = map.get(finger) + weights[finger.right][digit];
            if (isMovable(nextFinger, nextWeight, temp)) {
                temp.put(nextFinger, nextWeight);
            }
        }

        private void putLeftFinger(Finger finger, int digit, Map<Finger, Integer> map, Map<Finger, Integer> temp) {
            Finger nextFinger = new Finger(digit, finger.right);
            int nextWeight = map.get(finger) + weights[finger.left][digit];
            if (isMovable(nextFinger, nextWeight, temp)) {
                temp.put(nextFinger, nextWeight);
            }
        }

        private boolean isMovable(Finger finger, int weight, Map<Finger, Integer> temp) {
            return !temp.containsKey(finger) || temp.get(finger) > weight;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 10
        int solution1 = solution.solution("1756");
        System.out.println("solution1 = " + solution1);

        // 8
        int solution2 = solution.solution("5123");
        System.out.println("solution2 = " + solution2);
    }

}
