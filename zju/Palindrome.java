package zju;
import java.util.ArrayList;
import java.util.List;

public class Palindrome {
	static String[] strArray = { "aaabbacaa", "3411122211144322123", 
			"32132","123456789sdfg13" };

	public static void main(String[] args) {
		for (int i = 0; i < strArray.length; i++) {
			checkPalindrome(i);
		}
	}

	private static void checkPalindrome(int i) {
		String content = strArray[i];
		/**aba as 3char base aa as 2c base**/
		List<Base> baseList=findBase(content);
	}

	private static List<Base> findBase(String content) {
		System.out.println(content);
		ArrayList<Base> result = new ArrayList<Base>();
		for(int i = 0;i<content.length();i++){
			
		}
		if (result.isEmpty()){
			
		}
		return result;
	}
	private class Base{
		int length =0;int index=0;int switch_from=0;int switch_to=0;
		public Base(int length, int index, int switch_from, int switch_to) {
			super();
			this.length = length;
			this.index = index;
			this.switch_from = switch_from;
			this.switch_to = switch_to;
		}
		
	}
}

