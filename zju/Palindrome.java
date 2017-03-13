
import java.util.ArrayList;
import java.util.List;

public class Palindrome {

    public List<Base> findBase(String content) {
        ArrayList<Base> result = new ArrayList<Base>();
        for(int i = 0;i<content.length();i++){
            if(IsBase2(i,content)){result.add(addBase2(i,content));}
            if(IsBase3(i,content)){result.add(addBase3(i,content));}
        }
        return result;
    }

    public List<Full> ExtendsBase(List<Base> baselist){
        ArrayList<Full> result = new ArrayList<Full>();
        for(Base base : baselist){
            result.add(doExtend(base));
        }
        return result;
    }

    public Full doExtend(Base base) {
        String content= base.content;
        Full full = new Full(base.index,base.lookslike);
        if(base.index==0) return full;
        while(CanExtend(full,content)){
            full = doOneStep(full,base.content);
        }
        return full;
    }

    private Full doOneStep(Full full,String content) {
        if(full.lookslike.length()%2==0)
            return new Full(full.index-1,String.format("%c%s%c",content.charAt(full.index-1),
                full.lookslike,content.charAt(full.index+full.lookslike.length())));
        else
            return new Full(full.index,String.format("%c%s%c",
                    content.charAt(full.index-full.lookslike.length()/2-1),
                    full.lookslike,content.charAt(full.index+full.lookslike.length()/2+1)));
    }

    private boolean CanExtend(Full full,String content) {
        if(full.lookslike.length()%2==0) {
            if (full.index == 0 || full.index + full.lookslike.length() == content.length())
                return false;
            else if (content.charAt(full.index - 1) != content.charAt(full.index + full.lookslike.length()))
                return false;
            else return true;
        }
        else {
            int width = full.lookslike.length() / 2;
            if (full.index == 1 || full.index + full.lookslike.length()/2 == content.length())
                return false;
            else if (content.charAt(full.index - width-1) != content.charAt(full.index + width+1))
                return false;
            else return true;
        }

    }

    private boolean IsBase3(int i, String content) {
        if(i>0 && i<content.length()-1){
            if(content.charAt(i+1)==content.charAt(i-1)){
                return true;
            }
        }
        return false;
    }

    private Base addBase3(int i,String content) {
        return new Base(i,BaseType.base3,content);
    }

    private Base addBase2(int i,String content) {
        return new Base(i,BaseType.base2,content);
    }

    private boolean IsBase2(int i, String content) {
        if(i<content.length()-1){
            if(content.charAt(i+1)==content.charAt(i)){
                return true;
            }
        }
        return false;
    }

    public class Full{
        int index=0; String lookslike="";

        public Full(int index, String lookslike) {
            this.index = index;
            this.lookslike = lookslike;
        }
    }

    public class Base{
        int index=0; BaseType type; String content;String lookslike;
        public Base(int index, BaseType type, String content) {
            this.index = index;
            this.type = type;
            this.content = content;
            if(type==BaseType.base2)
                this.lookslike=content.substring(index,index+2);
            else
                this.lookslike=content.substring(index-1,index+2);
        }
    }
    public enum BaseType{ base2, base3}
}

