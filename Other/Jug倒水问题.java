import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		int[] input = { 3, 5, 4 };
		Jug j = new Jug(input);
		j.RunJug();
	}
}

class Jug {
	private int[] data;
	private ArrayList<JugState> StateList = new ArrayList<JugState>();

	public Jug(int[] input) {
		this.data = input;
	}

	public void RunJug() {
		JugState state = new JugState();
		state.waterInA = 0;
		state.waterInB = 0;
		this.StateList.add(state);
		FindNext(state);
	}

	private void FindNext(JugState state) {
		if (state.waterInA == data[2] || state.waterInB == data[2]) {
			this.PrintStateList();
			System.out.println("success");
		} else {
			if (CanPourOut(state)) {
				PourOut(state);
			}
			if (CanPourIn(state)) {
				PourIn(state);
			}
			// Pour A to B
			if (state.waterInB < data[1] && state.waterInA > 0) {
				PourAToB(state);
			}
			// Pour B to A
			if (state.waterInB > 0 && state.waterInA < data[0]) {
				PourBToA(state);
			}

		}

	}

	private boolean ContainState(JugState state)
	{
		for(int i=0;i<this.StateList.size();i++)
		{
			if(StateList.get(i).waterInA==state.waterInA&&StateList.get(i).waterInB==state.waterInB)
				return true;
		}
		return false;
	}
	private void PourBToA(JugState state) {
		JugState nextState = new JugState();
		if (state.waterInB > data[0] - state.waterInA) {
			nextState.waterInA = data[0];
			nextState.waterInB = state.waterInB - (data[0] - state.waterInA);
		} else {
			nextState.waterInB = 0;
			nextState.waterInA = state.waterInA + state.waterInB;
		}
		if (!ContainState(nextState)) {
			this.StateList.add(nextState);
			FindNext(nextState);
			this.StateList.remove(nextState);
		}

	}

	private void PourAToB(JugState state) {
		JugState nextState = new JugState();
		if (state.waterInA > data[1] - state.waterInB) {
			nextState.waterInB = data[1];
			nextState.waterInA = state.waterInA - (data[1] - state.waterInB);
		} else {
			nextState.waterInA = 0;
			nextState.waterInB = state.waterInB + state.waterInA;
		}
		if (!ContainState(nextState)) {
			this.StateList.add(nextState);
			FindNext(nextState);
			this.StateList.remove(nextState);
		}
	}

	private void PourIn(JugState state) {
		JugState nextState = new JugState();
		if (state.waterInA < data[0]) {
			nextState.waterInA = data[0];
			nextState.waterInB = state.waterInB;
			if (!ContainState(nextState)) {
				this.StateList.add(nextState);
				FindNext(nextState);
				this.StateList.remove(nextState);
			}
		}
		if (state.waterInB < data[1]) {
			nextState.waterInA = state.waterInA;
			nextState.waterInB = data[1];
			if (!ContainState(nextState)) {
				this.StateList.add(nextState);
				FindNext(nextState);
				this.StateList.remove(nextState);
			}
		}

	}

	private boolean CanPourIn(JugState state) {
		if (state.waterInA < data[0] || state.waterInB < data[1])
			return true;
		return false;
	}

	private void PourOut(JugState state) {
		JugState nextState = new JugState();
		if (state.waterInA > 0) {
			nextState.waterInA = 0;
			nextState.waterInB = state.waterInB;
			if (!ContainState(nextState)) {
				this.StateList.add(nextState);
				FindNext(nextState);
				this.StateList.remove(nextState);
			}
		}
		if (state.waterInB > 0) {
			nextState.waterInA = state.waterInA;
			nextState.waterInB = 0;
			if (!ContainState(nextState)) {
				this.StateList.add(nextState);
				FindNext(nextState);
				this.StateList.remove(nextState);
			}
		}

	}

	private boolean CanPourOut(JugState state) {
		if (state.waterInA > 0 || state.waterInB > 0)
			return true;
		return false;
	}
	public void PrintStateList()
	{
		for(int i=0;i<this.StateList.size();i++)
		{
			System.out.println(this.StateList.get(i).waterInA+" , "+this.StateList.get(i).waterInB);
		}
	}
	public void PrintArray() {
		for (int i = 0; i < this.data.length; i++) {
			System.out.print(this.data[i]);
		}
	}
}

class JugState {
	int waterInA = 0;
	int waterInB = 0;
}
