
import org.junit.Assert;
import org.junit.Test;
import java.util.List;

public class PalindromeTests {
    Palindrome instance = new Palindrome();
    @Test
    public void should_find_bases(){
        String content = "aaabbacaa";
        List<Palindrome.Base> result =instance.findBase(content);
        Assert.assertTrue(result.size()==6);
        String content2 = "3411122211144322123";
        result = instance.findBase(content2);
        Assert.assertTrue(result.size()==12);
        String content3 = "32132";
        result = instance.findBase(content3);
        Assert.assertTrue(result.size()==0);
    }

    @Test
    public void should_extend_one(){
        String content = "aaabbacaa";
        Palindrome.Base base = instance.new Base(0, Palindrome.BaseType.base2,content);
        Palindrome.Full full = instance.doExtend(base);
        Assert.assertTrue(full.lookslike.equals("aa"));
        Palindrome.Base base2 = instance.new Base(3, Palindrome.BaseType.base2,content);
        Palindrome.Full full2 = instance.doExtend(base2);
        Assert.assertTrue(full2.lookslike.equals("abba"));
    }

    @Test
    public void should_extend_all(){
        String content = "aaabbacaa";
        List<Palindrome.Base> result =instance.findBase(content);
        List<Palindrome.Full> fullList = instance.ExtendsBase(result);
        Assert.assertTrue(fullList.get(3).lookslike.equals("abba"));
        String content2 = "3411122211144322123";
        result =instance.findBase(content2);
        List<Palindrome.Full> fullList2 = instance.ExtendsBase(result);
        Assert.assertTrue(fullList2.get(5).equals("41112221114"));
    }
}
