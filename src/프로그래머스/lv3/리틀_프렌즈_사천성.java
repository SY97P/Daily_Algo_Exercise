package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * 문제요약
 * <p>
 * 2차원 배열 게임판
 * 같은 모양 타일 두 개씩 배치
 * 규칙에 따라 모든 타일을 제거할 때 제거하는 순서 구하기
 * 해가 존재하지 않는 경우 IMPOSSIBLE 반환
 * 해가 여러가지인 경우 알파벳 순으로 가장 먼저인 문자열 리턴
 * <p>
 * 규칙
 * 경로의 양 끝은 제거하려는 두 타일
 * 경로를 한 번 이하로 꺾어서 연결
 * 경로 상에는 다른 타일이나 장애물이 없어야 함
 * <p>
 * 제한사항
 * <p>
 * 1 <= 행, 열 <= 100
 * . : 빈칸
 * * : 막힌칸
 * board 타일에는 항상 같은 글자가 두 개씩 주어짐
 * 글자가 주어지지 않는 경우는 없음
 * <p>
 * 해결전략
 * <p>
 * 1회 이하로 꺽인 경우
 *  직선인 경우 (같은 행이거나 같은 열인 경우)
 *  다른 행, 열이지만 둘 사이의 두 경로 중 아무런 장애물이 없는 경로가 하나 이상 존재하는 경우
 *      (x, y), (a, b) -> (x, y) ~ (a, y) ~ (a, b) / (x, y) ~ (x, b) ~ (a, b)
 * <p>
 * board 를 2차원 배열로 변환
 * 모든 글자 좌표를 맵에 저장
 * 맵을 글자(키 값) 기준으로 오름차순 정렬
 * 순서대로 해당 글자를 지울 수 있으면 지우고, 지울 수 없으면 남기고 다음 글자 연산
 * 지울 때는 맵과 게임판 모두에서 지워야 함
 * 최종적으로 맵에 남은 글자가 없으면 해를 구한것
 * 맵에 글자가 하나라도 남아있으면 해를 구하지 못한것 -> 임파서블
 */

public class 리틀_프렌즈_사천성 {

    private static class Solution {

        private static final char EMTPY = '.';
        private static final char WALL = '*';

        private char[][] board;
        private Map<Character, List<Coordination>> locations;
        private List<Character> sortedTiles;

        public String solution(int m, int n, String[] _board) {
            StringBuilder answer = new StringBuilder();

            board = getTileBoard(_board);
            locations = getTileLocation(board);
            sortedTiles = locations.keySet().stream()
                    .sorted()
                    .collect(Collectors.toList());

            int index = 0;
            while (!locations.isEmpty()) {
                if (index >= sortedTiles.size()) {
                    return "IMPOSSIBLE";
                }

                char currentTile = sortedTiles.get(index);
                if (canDeleteTile(currentTile)) {
                    deleteTile(currentTile, index);
                    answer.append(currentTile);
                    index = 0;
                } else {
                    index++;
                }
            }

            return answer.toString();
        }

        private boolean canDeleteTile(char tile) {
            List<Coordination> coordinations = locations.get(tile);
            Coordination cor1 = coordinations.get(0);
            Coordination cor2 = coordinations.get(1);

            return notExistsObstacleInColumn(cor1.x, cor2.x, cor1.y, tile) && notExistsObstacleInRow(cor2.x, cor1.y,
                    cor2.y, tile)
                    || notExistsObstacleInRow(cor1.x, cor1.y, cor2.y, tile) && notExistsObstacleInColumn(cor1.x, cor2.x,
                    cor2.y, tile);
        }

        private boolean notExistsObstacleInColumn(int x1, int x2, int y, char tile) {
            for (int i = Math.min(x1, x2); i <= Math.max(x1, x2); i++) {
                if (board[i][y] != EMTPY && board[i][y] != tile) {
                    return false;
                }
            }
            return true;
        }

        private boolean notExistsObstacleInRow(int x, int y1, int y2, char tile) {
            for (int i = Math.min(y1, y2); i <= Math.max(y1, y2); i++) {
                if (board[x][i] != EMTPY && board[x][i] != tile) {
                    return false;
                }
            }
            return true;
        }

        private void deleteTile(char tile, int index) {
            // delete tile in board
            for (int i = 0; i < board.length; i++) {
                for (int j = 0; j < board[i].length; j++) {
                    if (board[i][j] == tile) {
                        board[i][j] = EMTPY;
                    }
                }
            }

            // delete tile in map
            locations.remove(tile);

            // delete tile in list
            sortedTiles.remove(index);
        }

        private Map<Character, List<Coordination>> getTileLocation(char[][] board) {
            Map<Character, List<Coordination>> map = new HashMap<>();

            for (int i = 0; i < board.length; i++) {
                for (int j = 0; j < board[i].length; j++) {
                    if (board[i][j] != EMTPY && board[i][j] != WALL) {
                        List<Coordination> coordinations = map.getOrDefault(board[i][j], new ArrayList<>());
                        coordinations.add(new Coordination(i, j));
                        map.put(board[i][j], coordinations);
                    }
                }
            }

            return map;
        }

        private char[][] getTileBoard(String[] board) {
            char[][] matrix = new char[board.length][board[0].length()];

            for (int i = 0; i < board.length; i++) {
                for (int j = 0; j < board[0].length(); j++) {
                    matrix[i][j] = board[i].charAt(j);
                }
            }

            return matrix;
        }

        private static class Coordination {

            int x;
            int y;

            protected Coordination(int x, int y) {
                this.x = x;
                this.y = y;
            }
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // ABCD
        String answer1 = s.solution(3, 3, new String[]{"DBA", "C*A", "CDB"});
        System.out.println("answer = " + answer1);

        // RYAN
        String answer2 = s.solution(2, 4, new String[]{"NRYN", "ARYA"});
        System.out.println("answer = " + answer2);

        // MUZI
        String answer3 = s.solution(4, 4, new String[]{".ZI.", "M.**", "MZU.", ".IU."});
        System.out.println("answer = " + answer3);

        // IMPOSSIBLE
        String answer4 = s.solution(2, 2, new String[]{"AB", "BA"});
        System.out.println("answer = " + answer4);

        // ABCE
        String answer5 = s.solution(3, 3, new String[]{"CCB", "A.B", "AEE"});
        System.out.println("answer = " + answer5);

        // AZ
        String answer6 = s.solution(2, 2, new String[]{"ZA", "ZA"});
        System.out.println("answer = " + answer6);

    }

}
