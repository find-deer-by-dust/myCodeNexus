import java.util.*;


public class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param s string字符串 
     * @return int整型
     */
    public int StrToInt (String s) {
        // write code here
        char[] tmp=s.toCharArray();
        int re=0;
        boolean findNum=false;
        boolean negative=false;
        int i;
        for(i=0;i<s.length();i++){
            if(tmp[i]!=' ')
                break;
        }
        if(i==s.length())
            return re;
        if(tmp[i]=='+'){
            i++;
        }
           
        else if(tmp[i]=='-')
            negative=true;
        for(;i<s.length();i++){



        }
        if(negative)
            return -re;
        return re;
    }
}
