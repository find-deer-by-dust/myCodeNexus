import java.util.*;


public class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param n int整型 
     * @param m int整型 
     * @return int整型
     */
    public int LastRemaining_Solution (int n, int m) {
        // write code here
        ArrayList<Integer> a=new ArrayList<>();
        int s;
        int tmp;
        int tag=0;
        for(int i=0;i<n;i++)
            a.add(i);

        while(a.size()!=1){
            s=a.size();
            tmp=(m%s-1+tag+s)%s;
            tag=tmp;
            // System.out.println(tmp);
            // System.out.println(a.get(tmp));
            a.remove(tmp);
        }
        return a.get(0);
    }
}