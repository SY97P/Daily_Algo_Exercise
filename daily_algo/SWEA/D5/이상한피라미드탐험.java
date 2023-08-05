/*

#1 1
#2 0
#3 31

*/

import java.util.Scanner;
import java.io.FileInputStream;
import java.util.ArrayList;

class Solution
{
	static ArrayList<ArrayList<Integer>> room;

	static ArrayList<Integer> maxRoom;

	static int ai;
	static int aj;

	static int count;
	
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		// Scanner sc = new Scanner(new FileInputStream("./SWEA/D5/이상한피라미드탐험.txt"));

		int t = sc.nextInt();

		room = new ArrayList<>();
		maxRoom = new ArrayList<>();

		makePyramid();

		// for (int i = 0; i < 46; i++) {
		// 	System.out.println(room.get(i));
		// }

		for (int tc = 1; tc < t + 1; tc ++) {
			count = 0;
			
			int a = sc.nextInt();
			int b = sc.nextInt();

			if (a > b) {
				int temp = a;
				a = b;
				b = temp;
			}

			getALoc(a);

			getCount(b);

			System.out.printf("#%d %d \n", tc, count);
		}
	}

	public static void getCount(int b) {
		for (int i = 0; i + ai < 141; i ++) {
			// System.out.println(room.get(ai+i).get(aj) + " " + room.get(ai+i).get(aj+i));
			if (b <= room.get(ai+i).get(aj+i) && b >= room.get(ai+i).get(aj)) {
				count = i;
				break;
			} else if (b < room.get(ai+i).get(aj)) {
				if (b - room.get(ai+i).get(aj+i) <= room.get(ai+i+1).get(aj) - b) {
					count = i + b - room.get(ai+i).get(aj+i) + 1;
				} else {
					count = i + room.get(ai+i+1).get(aj) - b + 1;
				}
				break;
			}
		}
	}


	public static void getALoc(int a) {
		for(int i = 0; i < maxRoom.size(); i ++) {
			if (a <= maxRoom.get(i)) {
				ai = i;
				aj = room.get(i).size() - 1 - (maxRoom.get(i) - a);
				break;
			}
		}
	}

	// 프로세스 당 한 번만 써야 함. 
	// TC 별로 호출되면 망함.
	public static void makePyramid() {
		for (int i = 0; i < 141; i++) {
			room.add(new ArrayList<>());
		}

		int index = 0;
		int value = 1;
		int bound = 1; 
		while (value <= 10000) {
			room.get(index).add(value++);
			if (room.get(index).size() == bound) {
				bound ++;
				index ++;
				maxRoom.add(value-1);
			}
		}
	}
}