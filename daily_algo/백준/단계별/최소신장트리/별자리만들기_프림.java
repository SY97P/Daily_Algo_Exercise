import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

/*
 * 프림 알고리즘
 * 1. 임의의 정점을 MST에 추가
 * 2. MST에 포함된 정점과 아닌 정점 사이 최소 간선을 MST에 추가 (우선순위 큐)
 * 3. 모든 정점이 MST에 포함되도록 반복
 */

public class 별자리만들기_프림 {
    static int n;
    static ArrayList<float[]> stars;
    static ArrayList<Edge>[] adj;
    static PriorityQueue<Edge> pq;

    static class Edge implements Comparable<Edge> {
        float cost;
        int node;

        Edge(float cost_num, int node_num) {
            this.cost = cost_num;
            this.node = node_num;
        }

        @Override
        public int compareTo(Edge o) {
            return Float.compare(this.cost, o.cost);
        }

        public void print() {
            System.out.println(this.cost + " " + this.node);
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
        adj = new ArrayList[n];

        for (int i = 0; i < n; i ++) {
            st = new StringTokenizer(br.readLine());
            stars.add(new float[]{Float.parseFloat(st.nextToken()), Float.parseFloat(st.nextToken())});
        }

        for (int i = 0; i < n; i ++) {
            adj[i] = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    adj[i].add(new Edge(dist(stars.get(i), stars.get(j)), j));
                }
            }
        }

        System.out.printf("%.2f\n", prim());
    }

    public static float dist(float[] a, float[] b) {
        return (float) Math.sqrt(Math.pow(a[0] - b[0], 2) + Math.pow(a[1] - b[1], 2));
    }

    public static float prim() {
        boolean[] visited = new boolean[n];

        pq = new PriorityQueue<>();
        pq.add(new Edge(0, 0));

        float result = 0.0f;

        while (!pq.isEmpty()) {
            Edge curr = pq.poll();

            if (!visited[curr.node]) {
                visited[curr.node] = true;
                result += curr.cost;

                for (Edge next : adj[curr.node]) {
                    if (!visited[next.node]) {
                        pq.add(new Edge(next.cost, next.node));
                    }
                }
            }
        }

        return result;
    }
}
