import java.util.LinkedList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		LinkedList<char[][]> allArrays = new LinkedList<char[][]>();

		FireNet fn = new FireNet();
		Scanner in = new Scanner(System.in);
		int rowsIn = 0;
		while (in.hasNext()) {
			String s = in.next();
			int scope = Integer.parseInt(s);
			if (scope == 0) {
				fn.CalculateAllArray(allArrays);
				//fn.printAllArray(allArrays);
				return;
			} else {
				rowsIn = 0;
				char[][] array = new char[scope][scope];
				while (in.hasNext()) {
					s = in.next();
					for (int i = 0; i < s.length(); i++) {
						array[rowsIn][i] = s.charAt(i);
					}
					rowsIn++;
					if (rowsIn == scope)
						break;
				}
				allArrays.add(array);
			}
		}
	}
}

class FireNet {
	public void print(String s) {
		System.out.print(s);
	}

	public void CalculateAllArray(LinkedList<char[][]> list) {
		while(!list.isEmpty()){
			this.maxCount=0;
			System.out.println(this.CalculateArray(list.pop())); 
		}
	}

	public void print(char s) {
		System.out.print(s);
	}

	public void printArray(char[][] array) {
		int scope = array.length;
		for (int i = 0; i < scope; i++) {
			for (int j = 0; j < scope; j++) {
				print(array[i][j]);
			}
			print("\n");
		}
	}

	public void printAllArray(LinkedList<char[][]> list) {
		while (!list.isEmpty()) {
			printArray(list.pop());
		}
	}
	
	private char[][] myArray;
	LinkedList<cell> arrangedList = new LinkedList<cell>();
	int maxCount = 0;

	public int CalculateArray(char[][] array) {

		this.myArray = array;
		PutGun(0, 0);
		return maxCount;
	}

	private void PutGun(int row, int column) {
		cell next = FindNext(row, column);
		if (Canput(row, column)) {
			this.myArray[row][column] = 'O';
			this.arrangedList.add(new cell(row, column));
		}
		if (next == null) {
			// finish and print all
			// fn.printArray(this.myArray);
			if (this.maxCount < arrangedList.size()) {
				this.maxCount = arrangedList.size();
			}
		} else {
			PutGun(next.row, next.column);
		}
		if (!this.arrangedList.isEmpty()) {
			cell lastGun = this.arrangedList.pollLast();
			this.myArray[lastGun.row][lastGun.column] = '.';
			next = FindNext(lastGun.row, lastGun.column);
			if (next != null)
				PutGun(next.row, next.column);
		}
	}

	private cell FindNext(int row, int column) {
		int scope = this.myArray.length;
		cell c = new cell(0, 0);
		if (column < scope - 1) {
			c.row = row;
			c.column = column + 1;
			return c;
		} else if (column == scope - 1 && row < scope - 1) {
			c.row = row + 1;
			c.column = 0;
			return c;
		}
		return null;
	}

	private boolean Canput(int row, int column) {
		if (this.myArray[row][column] == 'X') {
			return false;
		} else {
			boolean up = canShootFromUp(row, column);
			boolean down = canShootFromDown(row, column);
			boolean left = canShootFromLeft(row, column);
			boolean right = canShootFromRight(row, column);
			if (up || down || left || right) {
				return false;
			} else {
				return true;
			}
		}
	}

	private boolean canShootFromRight(int row, int column) {
		while (row > 0) {
			row--;
			if (this.myArray[row][column] == 'X')
				return false;
			else if (this.myArray[row][column] == 'O')
				return true;
		}
		return false;
	}

	private boolean canShootFromLeft(int row, int column) {
		while (column > 0) {
			column--;
			if (this.myArray[row][column] == 'X')
				return false;
			else if (this.myArray[row][column] == 'O')
				return true;
		}
		return false;
	}

	private boolean canShootFromDown(int row, int column) {
		while (row < this.myArray.length - 1) {
			row++;
			if (this.myArray[row][column] == 'X')
				return false;
			else if (this.myArray[row][column] == 'O')
				return true;
		}
		return false;
	}

	private boolean canShootFromUp(int row, int column) {
		while (column < this.myArray.length - 1) {
			column++;
			if (this.myArray[row][column] == 'X')
				return false;
			else if (this.myArray[row][column] == 'O')
				return true;
		}
		return false;
	}
}
class cell {
	public cell(int row, int column) {
		this.row = row;
		this.column = column;
	}

	public int row;
	public int column;
}