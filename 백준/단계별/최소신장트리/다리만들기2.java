import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;
import java.util.PriorityQueue;
import java.io.InputStreamReader;

public class 다리만들기2 {

    static boolean log = true;
    static int[][] d = new int[][]{{0,1}, {0,-1}, {1,0}, {-1, 0}};

    static int n, m;
    static int[][] matrix;
    static int island;
    static int[][] adj;
    static PriorityQueue<Pair> q;
    static boolean[] mst;

    static class Pair implements Comparator<Pair> {
        static int cost, node;

        Pair(int cost_num, int node_num) {
            this.cost = cost_num;
            this.node = node_num;
        }

        @Override
        public int compare(Pair o1, Pair o2) {
            return Integer.compare(o1.cost, o2.cost);
        }

        public void print() {
            System.out.println(this.cost + " " + this.node);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new FileReader(
                    "C:\\Users\\onetu\\IdeaProjects\\Daily_Algo_Exercise\\백준\\단계별\\최소신장트리\\다리만들기2.txt"
            )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        matrix = new int[n][m];

        for (int i = 0; i < n; i ++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        if (log) {
            for (int[] mat : matrix) {
                System.out.println(Arrays.toString(mat));
            }
        }

        // 1. 각 섬에 고유번호 부여
        numbering();

        if (log) {
            System.out.println();
            for (int[] mat : matrix)
                System.out.println(Arrays.toString(mat));
            System.out.println("island : " + island);
        }

        // 2. 섬 사이 거리 구하기
        distancing();

        if (log) {
            System.out.println();
            for (int[] ad : adj) {
                for (int j = 0; j < island; j++)
                    System.out.print((ad[j] == Integer.MAX_VALUE ? 0 : ad[j]) + ", ");
                System.out.println();
            }
        }

        // 3. MST 구하기
        // 4. 모든 섬을 연결할 수 있는지 확인
        System.out.println(prim());
    }

    private static void numbering() {
        island = 1;
        boolean[][] visited = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (matrix[i][j] == 1) {
                    island += 1;
                    matrix[i][j] = island;
                    number(i, j, island);
                }
            }
        }
    }

    private static void number(int i, int j, int island) {
        for (int[] dir : d) {
            int di = i + dir[0];
            int dj = j + dir[1];

            if ((0 <= di) && (di < n) && (0 <= dj) && (dj < m) && matrix[di][dj] == 1) {
                matrix[di][dj] = island;
                number(di, dj, island);
            }
        }
    }

    private static void distancing() {
        adj = new int[island][island];

        for (int i = 1; i < island; i++) {
            for (int j = 1; j < island; j++) {
                adj[i][j] = Integer.MAX_VALUE;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j ++) {
                if (matrix[i][j] != 0) {
                    for (int dir = 0; dir < 4; dir++) {
                        dist(i, j, dir, matrix[i][j], 0);
                    }
                }
            }
        }
    }

    // param_s : 현재 거리계산 중인 시작섬 (2부터 시작)
    // start : 현재 거리계산 중인 시작점 (= param_s - 1)
    private static void dist(int i, int j, int dir, int param_s, int count) {
        int di = i + d[dir][0];
        int dj = j + d[dir][1];

        if ((0 <= di) && (di < n) && (0 <= dj) && (dj < m)) {
            if (matrix[di][dj] == 0)
                dist(di, dj, dir, param_s, count+1);
            else if (matrix[di][dj] == param_s-1)
                return;
            else {
                if (count < 2)
                    return;
                int start = param_s - 1;
                int end = matrix[di][dj] - 1;
                adj[start][end] = adj[end][start] = Math.min(Math.min(adj[start][end], adj[end][start]), count);
                return;
            }
        }
    }

    // adj 초기값은 Integer.MAX_VALUE
    private static int prim() {
        int result = 0;

        mst = new boolean[island];

        q = new PriorityQueue<>();
        q.add(new Pair(0, 1));

        while (!q.isEmpty()) {
            Pair curr = q.poll();

            if (!mst[curr.node]) {
                mst[curr.node] = true;
                result += curr.cost;

                for (int next_node = 1; next_node < adj[curr.node].length; next_node++) {
                    int next_cost = adj[curr.node][next_node];
                    if (next_cost != Integer.MAX_VALUE) {
                        System.out.println(next_cost + " " + next_node);
                        q.add(new Pair(next_cost, next_node));
                    }
                }
            }
        }

        return result;
    }
}
