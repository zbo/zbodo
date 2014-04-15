//so tricky
import java.util.ArrayList;
import java.util.Hashtable;
//zju 3508
//assume f(slist,wlist) can caaulate the max number with giving soliderList and weaponList
//then f(slist,wlist) = max{f(slist-one,wlist-one) + g(onesolider,oneweapon)}

public class war {
    public static void main(String[] args) {
        int soliderCount = 3;
        int weaponCount = 3;
        int[] minArray = {1, 3, 5};
        int[] maxArray = {5, 7, 10};
        int[] weaponArray = {4, 8, 9};
        war w = new war(soliderCount, weaponCount, minArray, maxArray,
                weaponArray);
        int maxSoliders = w.CaculateMaxSoliders();
        System.out.println(maxSoliders);
    }

    class solider {
        public solider(int max, int min) {
            this.max = max;
            this.min = min;
        }

        public int max = 0;
        public int min = 0;
    }

    Hashtable<String, Integer> HistoryNodes = new Hashtable<String, Integer>();

    public war(int soliderCount, int weaponCount, int[] min, int[] max,
            int[] weaponArray) {
        for (int i = 0; i < soliderCount; i++) {
            solider s = new solider(max[i], min[i]);
            this.soliderlist.add(s);
        }
        for (int i = 0; i < weaponCount; i++) {
            this.weaponList.add(weaponArray[i]);
        }
    }

    public ArrayList<solider> soliderlist = new ArrayList<solider>();
    public ArrayList<Integer> weaponList = new ArrayList<Integer>();

    public int CaculateMaxSoliders() {
        int maxSolider = GetMax(this.soliderlist, this.weaponList);
        return maxSolider;
    }

    private int GetMax(ArrayList<solider> soliderlist2,
            ArrayList<Integer> weaponList2) {
        int maxvalue = 0;
        String currentStatusKey = GenerateKey(soliderlist2, weaponList2);
        if (this.HistoryNodes.containsKey(currentStatusKey)) {
            return HistoryNodes.get(currentStatusKey);
        } else if (soliderlist2.size() == 1) {
            solider s = soliderlist2.get(0);
            for (int i = 0; i < weaponList2.size(); i++) {
                if (weaponList2.get(i) >= s.min && weaponList2.get(i) <= s.max)
                    maxvalue = 1;
            }
            maxvalue = 0;
        } else if (weaponList2.size() == 1) {
            int w = weaponList2.get(0);
            for (int i = 0; i < soliderlist2.size(); i++) {
                if (w >= soliderlist2.get(i).min
                        && w <= soliderlist2.get(i).max)
                    maxvalue = 1;
            }
            maxvalue = 0;
        } else {
            for (int removeSoliderIndex = 0; removeSoliderIndex < soliderlist2
                    .size(); removeSoliderIndex++) {
                ArrayList<solider> subSoliderList = GetSubSoliderList(
                        removeSoliderIndex, soliderlist2);
                for (int removeWeaponIndex = 0; removeWeaponIndex < weaponList2
                        .size(); removeWeaponIndex++) {
                    ArrayList<Integer> subWeaponList = GetSubWeaponList(
                            removeWeaponIndex, weaponList2);
                    int subvalue = GetMax(subSoliderList, subWeaponList);
                    int totalvalue = subvalue
                            + GetMatch(soliderlist2.get(removeSoliderIndex),
                                    weaponList2.get(removeWeaponIndex));
                    if (totalvalue > maxvalue)
                        maxvalue = totalvalue;
                }
            }
        }
        this.HistoryNodes.put(currentStatusKey, maxvalue);
        return maxvalue;
    }

    private String GenerateKey(ArrayList<solider> soliderlist2,
            ArrayList<Integer> weaponList2) {
        String key = "";
        for (int i = 0; i < soliderlist2.size(); i++) {
            key += "m" + soliderlist2.get(i).min + "M"
                    + soliderlist2.get(i).max;
        }
        for (int i = 0; i < weaponList2.size(); i++) {
            key += "w" + weaponList2.get(i);
        }
        return key;
    }

    private int GetMatch(solider solider, Integer integer) {
        if (integer >= solider.min && integer <= solider.max)
            return 1;
        else
            return 0;
    }

    private ArrayList<Integer> GetSubWeaponList(int removeIndex,
            ArrayList<Integer> parentList) {
        ArrayList<Integer> subList = new ArrayList<Integer>();
        for (int i = 0; i < parentList.size(); i++) {
            if (i == removeIndex) {
                continue;
            } else {
                subList.add(parentList.get(i));
            }
        }
        return subList;
    }

    private ArrayList<solider> GetSubSoliderList(int removeIndex,
            ArrayList<solider> parentList) {
        ArrayList<solider> subList = new ArrayList<war.solider>();
        for (int i = 0; i < parentList.size(); i++) {
            if (i == removeIndex) {
                continue;
            } else {
                subList.add(parentList.get(i));
            }
        }
        return subList;
    }

}
