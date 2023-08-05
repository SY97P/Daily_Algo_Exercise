import java.io.FileReader;
import java.io.BufferedReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.InputStreamReader;

/*
 * 크루스칼 알고리즘
 * 1. 모든 정점 가중치 기준 오름차순 정렬
 * 2. MST에 사이클 발생하지 않는 최소 가중치 간선 선택해 MST에 추가
 * 3. 모든 정점이 MST에 추가되도록 반복
 */
public class 별자리만들기_크루스칼 {

    static int n;
    static ArrayList<float[]> stars;
    static ArrayList<Edge> edges;
    static int[] parent;

    static class Edge implements Comparable<Edge> {
        float cost;
        int start;
        int end;

        Edge(float cost_num, int start_num, int end_num) {
            this.cost = cost_num;
            this.start = start_num;
            this.end = end_num;
        }

        @Override
        public int compareTo(Edge o) {
            return Float.compare(this.cost, o.cost);
        }

        public void print() {
            System.out.printf("%f %d %d\n", this.cost, this.start, this.end);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "C:\\Users\\onetu\\IdeaProjects\\Daily_Algo_Exercise\\백준\\단계별\\최소신장트리\\별자리만들기.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        stars = new ArrayList<>(n);
        edges = new ArrayList<>();
        parent = new int[n];

        for (int i = 0; i < n; i ++) {
            st = new StringTokenizer(br.readLine());
            stars.add(new float[]{Float.parseFloat(st.nextToken()), Float.parseFloat(st.nextToken())});
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j ++) {
                if (i != j)
                    edges.add(new Edge(dist(stars.get(i), stars.get(j)), i, j));
            }
        }
        // 오름차순 정렬 (ArrayList 정렬 -> List.sort())
        edges.sort(Comparator.naturalOrder());

        for (int i = 0; i < n; i ++)
            parent[i] = i;

        System.out.printf("%.2f", kruskal());
    }

    private static float dist(float[] a, float[] b) {
        return (float) Math.sqrt(Math.pow(a[0]-b[0], 2) + Math.pow(a[1]-b[1], 2));
    }

    private static float kruskal() {
        float result = 0f;

        for (Edge e : edges) {
            int fa = find(e.start);
            int fb = find(e.end);

            if (fa == fb)
                continue;
            else if (fa < fb)
                union(e.end, fa);
            else
                union(e.start, fb);
            result += e.cost;
        }

        return result;
    }

    private static int find(int num) {
        if (parent[num] == num)
            return num;
        return find(parent[num]);
    }

    private static void union(int num, int set_num) {
        if (parent[num] == num) {
            parent[num] = set_num;
            return;
        }
        union(parent[num], set_num);
    }
}
