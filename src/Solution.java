import java.util.*;

public class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param num  int整型一维数组
     * @param size int整型
     * @return int整型ArrayList
     */
    public ArrayList<Integer> maxInWindows(int[] num, int size) {
        // write code here
        ArrayList<Integer> re = new ArrayList<>();
        if (num == null) {
            return null;
        }
        if (num.length == 0) {
            return null;
        }
        int max = num[0];
        int i = 0;

        for (i = 0; i < size; i++) {
            if (num[i] > max) {
                max = num[i];
            }
        }
        re.add(max);
        for (i = size; i < num.length; i++) {
            if (num[i] > max) {
                max = num[i];
            }
            re.add(max);
        }
        return re;
    }

    int getMax(int[] num, int size, int x) {

        return 1;
    }
}