/*

#1 1 4
#2 1 2 3 5 7

*/

import java.io.IOException;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

class 민석이의과제체크하기 {
	public static void main(String[] args) throws IOException {
// 		BufferedReader br = new BufferedReader(new FileReader("./SWEA/D3/민석이의과제체크하기.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int t = Integer.parseInt(br.readLine());

		for (int tc = 1; tc < t + 1; tc ++) {
			String[] temp = br.readLine().split(" ");
			int n = Integer.parseInt(temp[0]);
			int k = Integer.parseInt(temp[1]);

			temp = br.readLine().split(" ");

			// String 배열 -> Int 배열로 변환하는 방법 2가지
			// 1번 방법 (문자열 배열 -> Int 배열)
			int[] students = Arrays.stream(temp).mapToInt(Integer::parseInt).toArray();
			// 2번 방법 (String 배열 -> Int 배열)
			// int[] students = Arrays.asList(temp).stream().mapToInt(Integer::parseInt).toArray();

			// 제출했는지 확인용
			boolean[] submit = new boolean[n];

			for (int st : students) {
				submit[st-1] = true;
			}

			System.out.print("#" + tc + " ");
			for (int i = 0 ; i < n; i ++) {
				if (!submit[i]) {
					System.out.print((i+1) + " ");
				}
			}
			System.out.println();
		}
	}
}