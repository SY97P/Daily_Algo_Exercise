package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;

/**
 * 문제요약<br>
 *<br>
 * 기둥<br>
 * 1. 바닥 위<br>
 * 2. 보 한쪽 끝 부분<br>
 * 3. 다른 기둥 위<br>
 * 보<br>
 * 1. 한쪽 끝 부분이 기둥 위<br>
 * 2. 양쪽 끝 부분이 다른 보와 동시에 연결<br>
 *<br>
 * 주어진 작업 정보 순서대로 건축<br>
 * 조건을 만족하지 않으면 해당 작업 무시<br>
 * 모든 작업을 수행한 후의 구조물 상태 반환<br>
 *<br>
 * 제한사항<br>
 *<br>
 * 5 <= 벽면 크기 <= 100<br>
 * 1 <= 작업 수 <= 10^4<br>
 * 작업 = [가로 좌표, 세로 좌표, 기둥(0)/보(1), 삭제(0)/설치(1)]<br>
 * 결과 = [가로 좌표, 세로 좌표, 기둥(0)/보(1)]<br>
 * 결과는 (가로 좌표, 세로 좌표, 구조물 종류) 오름차순 정렬<br>
 *<br>
 * 해결전략<br>
 *<br>
 * 최종 구조물에 해당하는 빈 프레임(리스트)를 만듬<br>
 * 작업 순서대로 구조물 설치 혹은 제거 후 전체 프레임이 정상적인 상태인지 확인<br>
 * 정상이면 진행, 비정상이면 롤백<br>
 *
 */

public class 기둥과_보_설치 {

    private static class Solution {

        public int[][] solution(int n, int[][] build_frame) {
            List<Struct> structs = new ArrayList<>();

            for (int[] frame : build_frame) {
                Struct newFrame = new Struct(frame[0], frame[1], frame[2]);
                if (frame[3] == 0) {
                    structs.remove(newFrame);
                    if (isInValid(structs)) {
                        structs.add(newFrame);
                    }
                } else {
                    structs.add(newFrame);
                    if (isInValid(structs)) {
                        structs.remove(newFrame);
                    }
                }
            }

            structs.sort((s1, s2) -> {
                if (s1.x == s2.x) {
                    if (s1.y == s2.y) {
                        return s1.type - s2.type;
                    }
                    return s1.y - s2.y;
                }
                return s1.x - s2.x;
            });
            int[][] answer = new int[structs.size()][4];
            for (int i = 0; i < structs.size(); i ++) {
                answer[i] = structs.get(i).to();
            }
            return answer;
        }

        private boolean isInValid(List<Struct> structs) {
            for (Struct struct : structs) {
                if (struct.type == 0) {
                    if (struct.y == 0
                        || structs.contains(new Struct(struct.x - 1, struct.y, 1))
                        || structs.contains(new Struct(struct.x, struct.y, 1))
                        || structs.contains(new Struct(struct.x, struct.y - 1, 0))) {
                        continue;
                    }
                } else {
                    if (structs.contains(new Struct(struct.x, struct.y - 1, 0))
                        || structs.contains(new Struct(struct.x + 1, struct.y - 1, 0))
                        || (structs.contains(new Struct(struct.x + 1, struct.y, 1))
                            && structs.contains(new Struct(struct.x - 1, struct.y, 1)))) {
                        continue;
                    }
                }
                return true;
            }
            return false;
        }

        private static class Struct {
            int x;
            int y;
            int type;

            public Struct(int x, int y, int type) {
                this.x = x;
                this.y = y;
                this.type = type;
            }

            @Override
            public boolean equals(Object o) {
                if (o == this) return true;
                if (o == null || o.getClass() != this.getClass()) return false;
                Struct s = (Struct) o;
                return s.x == this.x && s.y == this.y && s.type == this.type;
            }

            @Override
            public int hashCode() {
                return Objects.hash(x, y, type);
            }

            public int[] to() {
                return new int[]{x, y, type};
            }

        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]]
        int[][] solution1 = solution.solution(5, new int[][]{new int[]{1, 0, 0, 1}, new int[]{1, 1, 1, 1}, new int[]{2, 1, 0, 1}, new int[]{2, 2, 1, 1}, new int[]{5, 0, 0, 1}, new int[]{5, 1, 0, 1}, new int[]{4, 2, 1, 1}, new int[]{3, 2, 1, 1}});
        System.out.println("solution = " + Arrays.deepToString(solution1));

        // [[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]]
        int[][] solution2 = solution.solution(5, new int[][]{new int[]{0, 0, 0, 1}, new int[]{2, 0, 0, 1}, new int[]{4, 0, 0, 1}, new int[]{0, 1, 1, 1}, new int[]{1, 1, 1, 1}, new int[]{2, 1, 1, 1}, new int[]{3, 1, 1, 1}, new int[]{2, 0, 0, 0}, new int[]{1, 1, 1, 0}, new int[]{2, 2, 0, 1}});
        System.out.println("solution = " + Arrays.deepToString(solution2));

    }

}
