package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;

/**
 * 해결전략
 *
 * - 표 크기 = 50 * 50
 * - 유니온 파인드
 */

public class 표_병합 {

    private static class Solution {

        private enum Command {
            UPDATE, MERGE, UNMERGE, PRINT
        }

        private static final int LENGTH = 51;

        private int[][][] parent;
        private String[][] table;
        private List<String> answer;

        public String[] solution(String[] commands) {
            answer = new ArrayList<>();

            initDP();

            for (String command : commands) {
                String[] split = command.split(" ");
                String operation = split[0];

                if (Objects.equals(operation, Command.UPDATE.name())) {
                    if (split.length == 4) {
                        update(Integer.parseInt(split[1]), Integer.parseInt(split[2]), split[3]);
                    } else {
                        update(split[1], split[2]);
                    }
                } else if (Objects.equals(operation, Command.MERGE.name())) {
                    merge(
                            Integer.parseInt(split[1]),
                            Integer.parseInt(split[2]),
                            Integer.parseInt(split[3]),
                            Integer.parseInt(split[4])
                    );
                } else if (Objects.equals(operation, Command.UNMERGE.name())) {
                    unmerge(
                            Integer.parseInt(split[1]),
                            Integer.parseInt(split[2])
                    );
                } else if (Objects.equals(operation, Command.PRINT.name())) {
                    print(
                            Integer.parseInt(split[1]),
                            Integer.parseInt(split[2])
                    );
                }
            }

            return answer.toArray(new String[0]);
        }

        private void initDP() {
            parent = new int[LENGTH][LENGTH][2];
            table = new String[LENGTH][LENGTH];
            for (int i = 0; i < LENGTH; i ++) {
                for (int j = 0; j < LENGTH; j ++) {
                    parent[i][j] = new int[]{i, j};
                    table[i][j] = "EMPTY";
                }
            }
        }

        private int[] find(int r, int c) {
            if (!Arrays.equals(parent[r][c], new int[]{r, c})) {
                parent[r][c] = find(parent[r][c][0], parent[r][c][1]);
            }
            return parent[r][c];
        }

        private void update(int r, int c, String value) {
            int[] target = find(r, c);

            for (int i = 1; i < LENGTH; i ++) {
                for (int j = 1; j < LENGTH; j ++) {
                    if (Arrays.equals(find(i, j), target)) {
                        table[i][j] = value;
                    }
                }
            }
        }

        private void update(String value1, String value2) {
            for (int i = 1; i < LENGTH; i ++) {
                for (int j = 1; j < LENGTH; j ++) {
                    if (Objects.equals(table[i][j], value1)) {
                        table[i][j] = value2;
                    }
                }
            }
        }

        private void merge(int r1, int c1, int r2, int c2) {
            String value = table[r1][c1] == "EMPTY" ? table[r2][c2] : table[r1][c1];

            int[] target = find(r1, c1);
            int[] subject = find(r2, c2);

            for (int i = 1; i < LENGTH; i ++) {
                for (int j = 1; j < LENGTH; j ++) {
                    if (Arrays.equals(find(i, j), subject) || Arrays.equals(find(i, j), target)) {
                        parent[i][j] = target;
                        table[i][j] = value;
                    }
                }
            }
        }

        private void unmerge(int r, int c) {
            int[] target = find(r, c);
            String value = table[r][c];

            for (int i  = 1; i < LENGTH; i ++) {
                for (int j = 1; j < LENGTH; j ++) {
                    if (Arrays.equals(find(i, j), target)) {
                        parent[i][j] = new int[]{i, j};
                        table[i][j] = "EMPTY";
                    }
                }
            }

            table[r][c] = value;
        }

        private void print(int r, int c) {
            answer.add(table[r][c]);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // ["EMPTY", "group"]
        String[] commands1 = new String[]{
                "UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean",
                "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle",
                "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3",
                "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"
        };
        String[] solution1 = solution.solution(commands1);
        System.out.println("solution1 = " + Arrays.toString(solution1));

        // ["d", "EMPTY"]
        String[] commands2 = new String[]{
                "UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1",
                "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"
        };
        String[] solution2 = solution.solution(commands2);
        System.out.println("solution2 = " + Arrays.toString(solution2));
    }

}
