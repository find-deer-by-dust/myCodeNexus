import java.util.*;

public class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param array int整型一维数组
     * @return int整型一维数组
     */
    public int[] FindNumsAppearOnce(int[] array) {
        // write code here
        int[] re = new int[2];
        int[] tmp = new int[1000001];
        for (int i = 0; i < array.length; i++) {
            tmp[array[i]] += 1;
        }
        for (int i = 0; i < 1000001; i++) {
            if (tmp[i] == 1 && re[0] == 0)
                re[0] = i;
            else if (tmp[i] == 1 && re[1] == 0)
                re[1] = i;
        }
        return re;
    }
}