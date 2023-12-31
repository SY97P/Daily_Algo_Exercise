package SWEA.D3;
/*
	
#1 53
#2 16200

*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

class 진용이의주차타워 {

    static int n;
    static int m;

    static int[] cost;
    static int[] weight;
    static int[] lot;

    static Queue<Integer> wait;

    static int charge;

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // BufferedReader br = new BufferedReader(new FileReader("./SWEA/D3/진용이의주차타워.txt"));

        int t = Integer.parseInt(br.readLine());

        for (int tc = 1; tc < t + 1; tc++) {
            String[] temp = br.readLine().split(" ");
            n = Integer.parseInt(temp[0]);
            m = Integer.parseInt(temp[1]);

            cost = new int[n];
            weight = new int[m];
            lot = new int[n];

            wait = new LinkedList<>();

            charge = 0;

            for (int i = 0; i < n; i++) {
                cost[i] = Integer.parseInt(br.readLine());
                lot[i] = -1;
            }
            for (int i = 0; i < m; i++) {
                weight[i] = Integer.parseInt(br.readLine());
            }

            for (int i = 0; i < 2 * m; i++) {
                int car = Integer.parseInt(br.readLine());
                if (car > 0) {    // 진입
                    if (getIn(car) == -1) {
                        wait.add(car);
                    }
                } else {        // 진출
                    if (getOut(car) == -1) {
                        wait.add(car);
                    } else {
                        while (!wait.isEmpty()) {
                            int curr = wait.peek();
                            if (curr > 0) {
                                if (getIn(curr) == -1) {
                                    break;
                                } else {
                                    wait.poll();
                                }
                            } else {
                                if (getOut(curr) == -1) {
                                    break;
                                } else {
                                    wait.poll();
                                }
                            }
                        }
                    }
                }
            }

            System.out.printf("#%d %d \n", tc, charge);
        }
    }

    // 차량 진입
    public static int getIn(int car) {
        boolean success = false;
        for (int i = 0; i < n; i++) {
            if (lot[i] == -1) {
                lot[i] = car;
                success = true;
                break;
            }
        }
        // 공간이 없었을 시 -1 반환
		if (!success) {
			return -1;
		}
        return 0;
    }

    // 차량 제거 및 요금 정산
    public static int getOut(int car) {
        boolean success = false;
        for (int i = 0; i < n; i++) {
            if (lot[i] == -1 * car) {
                lot[i] = -1;
                charge += weight[-1 * car - 1] * cost[i];
                success = true;
            }
        }
        // 뺄 차량이 없었으면 -1 반환 (대기 중인 차량)
		if (!success) {
			return -1;
		}
        return 0;
    }
}