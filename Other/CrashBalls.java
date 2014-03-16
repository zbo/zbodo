
class CrashBalls {
	int[] Number;

	public CrashBalls(int[] number) {
		this.Number = number;
	}

	public Integer Run() {

		LinkedList<Integer> sep1 = NumberSeparate(Number[0]);
		LinkedList<Integer> sep2 = NumberSeparate(Number[1]);
		LinkedList<LinkedList<Integer>> legalSep1 = FindLegalSep(sep1);
		LinkedList<LinkedList<Integer>> legalSep2 = FindLegalSep(sep2);
		legalSep1 = RemoveBad(legalSep1);
		legalSep2 = RemoveBad(legalSep2);
		Boolean compatiable = ISCompatiable(legalSep1, legalSep2);
		if (compatiable) {
			return Max(Number);
		} else {
			return Min(Number);
		}
	}

	private Integer Min(int[] number2) {
		if (number2[0] > number2[1])
			return number2[1];
		else
			return number2[0];

	}

	private Integer Max(int[] number2) {
		if (number2[0] < number2[1])
			return number2[1];
		else
			return number2[0];
	}

	private Boolean ISCompatiable(LinkedList<LinkedList<Integer>> legalSep1,
			LinkedList<LinkedList<Integer>> legalSep2) {
		for (int i = 0; i < legalSep1.size(); i++)
			for (int j = 0; j < legalSep2.size(); j++) {
				Boolean compatiable = ISCompatiableList(legalSep1.get(i),
						legalSep2.get(j));
				if (compatiable)
					return true;
			}
		return false;
	}

	private Boolean ISCompatiableList(LinkedList<Integer> linkedList,
			LinkedList<Integer> linkedList2) {
		
		for (int i = 0; i < linkedList.size(); i++)
			for (int j = 0; j < linkedList2.size(); j++) {
				if (linkedList.get(i) == linkedList2.get(j))
					return false;
			}
		return true;
	}

	private LinkedList<LinkedList<Integer>> RemoveBad(
			LinkedList<LinkedList<Integer>> legalSep) {
		for (int i = legalSep.size() - 1; i >= 0; i--) {// need remove form last
			// to first
			LinkedList<Integer> list = legalSep.get(i);
			Boolean bad = false;
			for (int j = 0; j < list.size(); j++) {
				if (list.get(j) > 100) {
					bad = true;
					break;
				}
				for (int k = j + 1; k < list.size(); k++) {
					if (list.get(j) == list.get(k)) {
						bad = true;
						break;
					}

				}
				if (bad)
					break;
			}
			if (bad)
				legalSep.remove(list);
		}
		return legalSep;
	}

	private LinkedList<LinkedList<Integer>> FindLegalSep(LinkedList<Integer> sep) {
		LinkedList<LinkedList<Integer>> result = new LinkedList<LinkedList<Integer>>();
		LinkedList<LinkedList<Integer>> subList = new LinkedList<LinkedList<Integer>>();
		subList.add(sep);
		result.addAll(subList);
		while (subList.getFirst().size() > 1) {
			subList = GetSubLists(subList);
			result.addAll(subList);
		}
		return result;
	}

	@SuppressWarnings("unchecked")
	private LinkedList<LinkedList<Integer>> GetSubLists(
			LinkedList<LinkedList<Integer>> orgList) {
		LinkedList<LinkedList<Integer>> result = new LinkedList<LinkedList<Integer>>();
		for (int index = 0; index < orgList.size(); index++) {
			LinkedList<Integer> list = orgList.get(index);
			for (int i = 0; i < list.size(); i++) {
				for (int j = i + 1; j < list.size(); j++) {
					LinkedList<Integer> temp = (LinkedList<Integer>) list
							.clone();
					temp.add(list.get(i) * list.get(j));
					temp.remove(j);// we are sure j>i
					temp.remove(i);
					if (!result.contains(temp))
						result.add(temp);
				}
			}
		}
		return result;
	}

	private LinkedList<Integer> NumberSeparate(int input) {
		LinkedList<Integer> sep = new LinkedList<Integer>();
		int leftNumber = input;
		int devider = 2;
		while (devider <= 100) {
			while (leftNumber % devider == 0) {
				sep.add(devider);
				leftNumber = leftNumber / devider;
			}
			devider++;
		}
		return sep;
	}
}
