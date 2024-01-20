package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * 문제요약
 *<br>
 * 규칙<br>
 * 1. 조각은 한 번에 하나씩 채워넣기<br>
 * 2. 조각 회전 가능<br>
 * 3. 조각 뒤집기 불가능<br>
 * 4. 채워넣은 후 빈 칸이 남으면 안 됨 (빈 공간과 채운 칸이 딱 맞아야 함)<br>
 * <br>
 * 제한사항<br>
 *
 * 3 <= game_board, table 행, 열 길이 <= 50<br>
 * game_board[i][j] = 0(빈칸) / 1(채워진칸)<br>
 * 퍼즐조각은 행열 길이가 최대 6인 경우까지만 주어짐<br>
 * <br>
 * 해결전략<br>
 *
 * 1. table 조각 추출 (6*6 칸에 왼쪽 위로 정규화)<br>
 * 2. game_board 순회하면서 빈칸 찾기<br>
 * 3. 빈칸이면 table 조각 하나씩 순회, 회전하면서 조각이 맞춰지면 다음 빈칸으로<br>
 * 4. 최종적으로 사용한 table 조각 수 반환하기<br>
 */

public class 퍼즐_조각_채우기 {

    private static class Solution {

        private enum PuzzleType {
            KEY(1),
            LOCK(0);

            final int value;

            PuzzleType (int value) {
                this.value = value;
            }
        }

        private static class Coordi {
            int x;
            int y;

            Coordi(int x, int y) {
                this.x = x;
                this.y = y;
            }
        }

        private static class Puzzle {
            public static final int BOUND = 6;

            int[][] piece;
            boolean used;

            Puzzle (List<Coordi> coordis, PuzzleType puzzleType) {
                this.piece = getMatrix(coordis, puzzleType);
                this.used = false;
            }

            Puzzle (int[][] piece) {
                this.piece = piece;
                this.used = false;
            }

            Puzzle rotate() {
                int[][] newPiece = new int[BOUND][BOUND];
                for (int i = 0; i < BOUND; i ++) {
                    for (int j = 0; j < BOUND; j ++) {
                        newPiece[j][BOUND - (i + 1)] = piece[i][j];
                    }
                }
                return new Puzzle(regulate(newPiece));
            }

            private int[][] getMatrix(List<Coordi> coordis, PuzzleType puzzleType) {
                int[][] temp = new int[BOUND][BOUND];
                for (int i = 0; i < BOUND; i ++) {
                    for (int j = 0; j < BOUND; j ++) {
                        temp[i][j] = (puzzleType.value + 1) % 2;
                    }
                }
                int[] regulateCoordi = getRegulateCoordi(coordis);
                for (Coordi coordi : coordis) {
                    int x = coordi.x - regulateCoordi[0];
                    int y = coordi.y - regulateCoordi[1];
                    temp[x][y] = puzzleType.value;
                }
                return temp;
            }

            private int[] getRegulateCoordi(List<Coordi> coordis) {
                int x = Integer.MAX_VALUE, y = Integer.MAX_VALUE;
                for (Coordi coordi : coordis) {
                    x = Math.min(x, coordi.x);
                    y = Math.min(y, coordi.y);
                }
                return new int[]{x, y};
            }

            private int[][] regulate(int[][] piece) {
                int[][] temp = new int[BOUND][BOUND];
                Coordi regulateCoordi = getRegulateCoordi(piece);
                for (int i = 0; i < BOUND; i ++) {
                    for (int j = 0; j < BOUND; j ++) {
                        if (piece[i][j] == PuzzleType.KEY.value) {
                            int x = i - regulateCoordi.x;
                            int y = j - regulateCoordi.y;
                            temp[x][y] = PuzzleType.KEY.value;
                        }
                    }
                }
                return temp;
            }

            private Coordi getRegulateCoordi(int[][] coordis) {
                int x = BOUND, y = BOUND;
                for (int i = 0; i < BOUND; i ++) {
                    for (int j = 0; j < BOUND; j ++) {
                        if (coordis[i][j] == PuzzleType.KEY.value) {
                            x = Math.min(x, i);
                            y = Math.min(y, j);
                        }
                    }
                }
                return new Coordi(x, y);
            }

        }

        private static final int[] dx = {1, 0, 0, -1};
        private static final int[] dy = {0, 1, -1, 0};

        private int n;
        private boolean[][] visited;
        private List<Puzzle> keys;
        private List<Puzzle> locks;

        public int solution(int[][] game_board, int[][] table) {
            n = table.length;

            keys = new ArrayList<>();
            locks = new ArrayList<>();

            visited = new boolean[n][n];
            for (int i = 0; i < n; i ++) {
                for (int j = 0; j < n; j ++) {
                    if (!visited[i][j] && table[i][j] == PuzzleType.KEY.value) {
                        keys.add(bfs(i, j, table, PuzzleType.KEY));
                    }
                }
            }

            visited = new boolean[n][n];
            for (int i = 0; i < n; i ++) {
                for (int j = 0; j < n; j ++) {
                    if (!visited[i][j] && game_board[i][j] == PuzzleType.LOCK.value) {
                        locks.add(bfs(i, j, game_board, PuzzleType.LOCK));
                    }
                }
            }

            int answer = 0;
            for (Puzzle lock : locks) {
                for (Puzzle key : keys) {
                    if (key.used) {
                        continue;
                    }
                    Puzzle rotateKey = key;
                    for (int k = 0; k < 4; k ++) {
                        rotateKey = rotateKey.rotate();

                        if (isMatched(lock.piece, rotateKey.piece)) {
                            answer += getCount(lock.piece, PuzzleType.LOCK);
                            key.used = true;
                            break;
                        }
                    }
                    if (key.used) {
                        break;
                    }
                }
            }

            return answer;
        }

        private int getCount(int[][] piece, PuzzleType puzzleType) {
            int count = 0;
            for (int i = 0; i < piece.length; i ++) {
                for (int j = 0; j < piece.length; j ++) {
                    if (piece[i][j] == puzzleType.value) {
                        count ++;
                    }
                }
            }
            return count;
        }

        private Puzzle bfs(int x, int y, int[][] board, PuzzleType puzzleType) {
            visited[x][y] = true;

            List<Coordi> coordis = new ArrayList<>();

            Queue<Coordi> q = new LinkedList<>();
            q.add(new Coordi(x, y));

            while (!q.isEmpty()) {
                Coordi coordi = q.poll();

                coordis.add(coordi);

                for (int i = 0; i < dx.length; i ++) {
                    int nx = coordi.x + dx[i];
                    int ny = coordi.y + dy[i];

                    if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
                        continue;
                    }

                    if (!visited[nx][ny] && board[nx][ny] == puzzleType.value) {
                        visited[nx][ny] = true;
                        q.add(new Coordi(nx, ny));
                    }
                }
            }

            return new Puzzle(coordis, puzzleType);
        }

        private boolean isMatched(int[][] lock, int[][] key) {
            for (int i = 0; i < Puzzle.BOUND; i ++) {
                for (int j = 0; j < Puzzle.BOUND; j ++) {
                    if (lock[i][j] + key[i][j] != 1) {
                        return false;
                    }
                }
            }
            return true;
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 14
        int solution1 = solution.solution(new int[][]{new int[]{1, 1, 0, 0, 1, 0}, new int[]{0, 0, 1, 0, 1, 0}, new int[]{0, 1, 1, 0, 0, 1}, new int[]{1, 1, 0, 1, 1, 1}, new int[]{1, 0, 0, 0, 1, 0}, new int[]{0, 1, 1, 1, 0, 0}}, new int[][]{new int[]{1, 0, 0, 1, 1, 0}, new int[]{1, 0, 1, 0, 1, 0}, new int[]{0, 1, 1, 0, 1, 1}, new int[]{0, 0, 1, 0, 0, 0}, new int[]{1, 1, 0, 1, 1, 0}, new int[]{0, 1, 0, 0, 0, 0}});
        System.out.println("solution1 = " + solution1);

        // 0
        int solution2 = solution.solution(new int[][]{new int[]{0, 0, 0}, new int[]{1, 1, 0}, new int[]{1, 1, 1}}, new int[][]{new int[]{1, 1, 1}, new int[]{1, 0, 0}, new int[]{0, 0, 0}});
        System.out.println("solution2 = " + solution2);

    }
}
