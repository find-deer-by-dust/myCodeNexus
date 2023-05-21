import java.util.*;

public class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param cost int整型一维数组
     * @return int整型
     */
    int[] tmp;

    public int minCostClimbingStairs(int[] cost) {
        tmp = new int[cost.length + 1];
        tmp[0] = 0;
        tmp[1] = 0;
        for (int i = 2; i < tmp.length; i++) {
            tmp[i] = Math.min((tmp[i - 1] + cost[i - 1]), (tmp[i - 2] + cost[i - 2]));
        }
        int[][] a = { { 0, 2, 0, 0, 0 },
                { 0, 2, 0, 1, 0 },
                { 1, 2, 0, 0, 1 },
                { 2, 1, 0, 0, 1 },
                { 2, 0, 1, 0, 1 },
                { 2, 0, 1, 1, 0 },
                { 1, 0, 1, 1, 1 },
                { 0, 1, 0, 0, 0 },
                { 0, 0, 1, 0, 1 },
                { 2, 1, 1, 0, 1 },
                { 0, 1, 1, 1, 1 },
                { 1, 1, 0, 1, 1 },
                { 1, 2, 1, 0, 1 },
                { 2, 1, 0, 1, 0 }, };
        return tmp[tmp.length - 1];
        // write code here
    }
}