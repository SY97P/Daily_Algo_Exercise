/*

#1 2 2 1 1 4 
#2 4 1 2 5 1 2 4 4 3
#3 6 1 2 2 3 8 1 3 7 5 8 9 5
#4 10 1 8 2 5 11 1 12 2 5 6 8 4 6 9 4 15 9 10 10 11
#5 8 1 6 10 2 2 15 6 11 7 14 11 10 17 7 15 17
#6 10 1 10 16 1 7 4 4 18 11 7 6 16 18 6 12 11 15 12 13 15
#7 13 1 13 6 3 19 1 3 12 8 6 12 4 4 14 7 11 15 8 14 10 11 15 10 19 13 20
#8 15 2 1 3 4 1 22 4 13 8 9 25 3 12 8 9 11 10 17 15 12 13 15 11 18 22 10 18 23 17 25
#9 18 8 2 3 7 4 10 15 3 9 6 14 4 11 8 7 16 6 21 16 9 10 17 21 14 27 11 17 18 18 20 26 15 20 23 23 27
#10 20 2 1 13 2 5 6 4 13 14 5 6 15 25 4 9 16 12 14 21 8 16 11 22 9 20 10 10 21 8 29 11 25 15 22 30 12 29 28 28 30

*/

import java.io.InputStreamReader;
import java.io.BufferedReader;
// import java.io.FileReader;
import java.util.PriorityQueue;
import java.util.Comparator;
import java.util.Arrays;

class Solution
{
	static int n;

	static int[][] matrix; 
	static int[][] region;

	static int[][] dv = {
		{0, 1}, {1, 0}, {0, -1}, {-1, 0}	
	};

	static PriorityQueue<int[]> pq;

	static int count;

	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// BufferedReader br = new BufferedReader(new FileReader("./SWEA/D4/행렬찾기.txt"));

		int t = Integer.parseInt(br.readLine());

		for (int tc = 1; tc < t + 1; tc ++) {
			n = Integer.parseInt(br.readLine());

			matrix = new int[n][n];
			region = new int[n][n];

			// 2차원 우선순위큐 구현
			pq = new PriorityQueue<>(new Comparator<int[]>() {
				@Override
				public int compare(int[] o1, int[] o2) {
					if (o1[0] == o2[0]) {
						if (o1[1] == o2[1]) {
							return Integer.compare(o1[2], o2[2]);
						}
						return Integer.compare(o1[1], o2[1]);
					}
					return Integer.compare(o1[0], o2[0]);
				}
			});

			count = 0;

			for (int i = 0; i < n; i ++) {
				matrix[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
			}

			// if (tc != 1) {
			// 	continue;
			// }

			// DFS 해서 영역 만들기
			int index = 1;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j ++) {
					if (matrix[i][j] != 0 && region[i][j] == 0) {
						dfs(i, j, index);
						index++;
					}
				}
			}

			// for (int[] lst : region) {
			// 	System.out.println(Arrays.toString(lst));
			// }

			// 행렬 정보 추출
			index = 1;
			
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (region[i][j] == index) {
						extractMatrix(i, j, index);
						index++;
					}
				}
			}

			System.out.printf("#%d %d ", tc, count);
			while (!pq.isEmpty()) {
				int[] curr = pq.poll();
				System.out.printf("%d %d ", curr[1], curr[2]);
			}
			System.out.println();
		}
	}

	// 영역 구분 DFS
	public static void dfs(int i, int j, int index) {
		region[i][j] = index;
		for (int[] d : dv) {
			int di = i + d[0];
			int dj = j + d[1];
			
			if ((0 <= di && di < n) && (0 <= dj && dj < n) && matrix[di][dj] != 0 && region[di][dj] == 0) {
				dfs(di, dj, index);
			}
		}
	}

	// 영역 정보 추출
	public static void extractMatrix(int i, int j, int index) {
		int dx = 0;
		int dy = 0;
		for (int k = 0; k < n; k ++) {
			if (i + k < n && region[i+k][j] == index)
				dx++;
			if (j + k < n && region[i][j+k] == index)
				dy++;
		}
		pq.offer(new int[] {dx * dy, dx, dy});
		count ++;
	}
}