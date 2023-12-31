import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.io.InputStreamReader;

public class 우수마을 {
    static int INIT_VALUE = 1;

    static int n;
    static int[] w;
    static ArrayList<Integer>[] adj;
    static int[][] dp;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "C:\\Users\\onetu\\IdeaProjects\\Daily_Algo_Exercise\\백준\\단계별\\트리dp\\우수마을.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());

        w = new int[n+1];
        st = new StringTokenizer(br.readLine());
        for (int i=1; i<n+1; i++) {
            w[i] = Integer.parseInt(st.nextToken());
        }

        adj = new ArrayList[n+1];
        for (int i=0; i<n+1; i++)
            adj[i] = new ArrayList<>();
        for (int i=0; i < n-1; i ++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            adj[a].add(b);
            adj[b].add(a);
        }

        dp = new int[n+1][2];

        visited = new boolean[n+1];

        visited[INIT_VALUE] = true;
        solve(INIT_VALUE);

        System.out.println(Arrays.stream(dp[INIT_VALUE]).max().getAsInt());
    }

    public static void solve(int node) {
        for (int next_node : adj[node]) {
            if (!visited[next_node]) {
                visited[next_node] = true;
                solve(next_node);
                dp[node][0] += Arrays.stream(dp[next_node]).max().getAsInt();
                dp[node][1] += dp[next_node][0];
            }
        }
        dp[node][1] += w[node];
    }
}
