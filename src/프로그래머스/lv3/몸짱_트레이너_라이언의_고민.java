package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 문제요약
 *
 * 정사각형 락커에서 손님들이 서로 최대한 멀리 떨어지도록 락커룸을 배정
 * 헬스장 이용 손님 중 가장 가까웠던 손님 간 거리 구하기
 *
 * 제한사항
 *
 * 락커는 정사각형
 * 락커간 거리는 상하좌우 1, 대각선 2
 * 손님은 철저히 예약시간에 맞춰 락커룸 사용
 * 영업시간은 오전 10시 ~ 오후 10시
 * 락커 수보다 많은 수의 손님이 올 수 없음
 * 0 < 락커 한 변의 길이 <= 10
 * 0 <= 손님 수 <= 1_000
 * 600 <= 입퇴실 시간 <= 1_320
 * 손님 간 이용시간이 한 번도 겹치지 않는 경우에는 0 반환
 *
 * 해결잔략
 *
 * 모든 시간에 최대로 손님이 몰렸을때의 손님 수보다만 많으면 됨
 * 최대거리차(sqrt(2) * n) 부터 1씩 줄여가면서 연산
 * 해당 거리차로 모든 손님 수용이 가능한 경우 break 해서 trunning
 * 첫 행의 어떤 열에서 시작해야 거리차에 맞게 락커룸 배정할지 모르니, 모든 행에서 시작해보기
 * 현재 좌표에서 거리차 만큼 떨어진 곳을 다 넣어서 연산해보기
 * 만약에 좌표 습득이 불가능한 경우가 한 번이라도 생기면 해당 순회는 모두 무효화
 *
 * 문제해결
 *
 * Q. 최대거리차가 틀림
 * 정사각형이고, 한 락커칸의 길이가 1, 대각선의 길이가 2이므로 최대거리차는 2 * (n - 1)
 */

public class 몸짱_트레이너_라이언의_고민 {

    private static class Solution {

        private static final int END_TIME = 22 * 60;

        public int solution(int n, int m, int[][] timetable) {

            int customerCount = getMaxCustomerCount(timetable);
            if (customerCount <= 1) {
                return 0;
            }

            for (int dist = 2 * (n - 1); dist > 0; dist --) {
                for (int y = 0; y < n; y ++) {
                    List<Rocker> rockers = findOtherRockers(y, n, dist);
                    if (rockers.size() >= customerCount) {
                        return dist;
                    }
                }
            }

            return 0;
        }

        private List<Rocker> findOtherRockers(int y, int n, int dist) {
            List<Rocker> rockers = new ArrayList<>();
            rockers.add(new Rocker(0, y));

            for (int i = 0; i < n; i ++) {
                for (int j = 0; j < n; j ++) {
                    if (i == 0 && j <= y) {
                        continue;
                    }
                    if (isTargetDiffRocker(dist, rockers, i, j)) {
                        rockers.add(new Rocker(i, j));
                    }
                }
            }

            return rockers;
        }

        private boolean isTargetDiffRocker(int dist, List<Rocker> rockers, int i, int j) {
            for (Rocker rocker : rockers) {
                if (getDiff(rocker, i, j) < dist) {
                    return false;
                }
            }
            return true;
        }

        private int getDiff(Rocker rocker, int i, int j) {
            return Math.abs(rocker.x - i) + Math.abs(rocker.y - j);
        }

        private int getMaxCustomerCount(int[][] timetable) {
            int[] dp = new int[END_TIME + 1];

            for (int[] time : timetable) {
                dp[time[0]] ++;
                dp[time[1] + 1] --;
            }

            for (int i = 1; i <= END_TIME; i ++) {
                dp[i] += dp[i - 1];
            }

            return Arrays.stream(dp)
                    .max()
                    .orElse(0);
        }

        private static class Rocker {
            int x;
            int y;

            Rocker(int x, int y) {
                this.x = x;
                this.y = y;
            }
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // 4
        int answer1 = s.solution(3, 2, new int[][]{new int[]{1170, 1210}, new int[]{1200, 1260}});
        System.out.println("answer1 = " + answer1);

        // 0
        int answer2 = s.solution(2, 1, new int[][]{new int[]{840, 900}});
        System.out.println("answer2 = " + answer2);

        // 2
        int answer3 = s.solution(2, 2, new int[][]{new int[]{600, 630}, new int[]{630, 700}});
        System.out.println("answer3 = " + answer3);

        // 4
        int answer4 = s.solution(4, 5, new int[][]{new int[]{1140, 1200}, new int[]{1150, 1200}, new int[]{1100, 1200}, new int[]{1210, 1300}, new int[]{1220, 1280}});
        System.out.println("answer4 = " + answer4);

    }

}
