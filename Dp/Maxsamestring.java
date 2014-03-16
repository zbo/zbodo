//找出这两个字符串中的子序列，例子中就是ghj882
//假设可以不连续，就成了找字符相似度那道题目了，就是个dp
//假设按照连续来做就是一个循环
public class Maxsamestring {
    public static void main(String[] args) {
        String str1 = "asdfghj882kl";
        String str2 = "1qasdfrtghj88291";
        Maxsamestring instance = new Maxsamestring();
        int max = instance.CaculateMaxSameString(str1, str2);
        System.out.print(max);
    }
    int CaculateMaxSameString(String str1, String str2) {
        int firstLength = str1.length();
        int maxMatch = 0;
        int currentMatch = 0;
        for (int i = 0; i < firstLength; i++) {
            currentMatch = getMaxMatch(i, str1, str2);
            if (currentMatch > maxMatch)
                maxMatch = currentMatch;
        }
        return maxMatch;
    }
    
    private int getMaxMatch(int firstStringBegin, String str1, String str2) {
        int matchLenght = 0;
        Boolean canMatchWithSecond = false;
        do {
            matchLenght++;
            String firstTryMatch = str1.substring(firstStringBegin,
                    firstStringBegin + matchLenght);
            canMatchWithSecond = tryMatch(firstTryMatch, str2);
        } while (canMatchWithSecond);
        return matchLenght-1;
    }
    
    private Boolean tryMatch(String firstTryMatch, String str2) {
        if (str2.contains(firstTryMatch))
            return true;
        else
            return false;
    }
}