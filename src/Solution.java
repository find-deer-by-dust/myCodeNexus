import java.util.*;

public class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param prices int整型一维数组
     * @return int整型
     */
    public int maxProfit(int[] prices) {
        // write code here
        if (prices == null)
            return 0;
        if (prices.length == 0)
            return 0;
        int minIndex = 0;
        int maxIndex = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < prices[minIndex])
                minIndex = i;
            if (minIndex > maxIndex)
                maxIndex = minIndex;
            if (prices[i] > prices[maxIndex] && i > minIndex)
                maxIndex = i;
        }
        System.out.println(maxIndex);
        System.out.println(minIndex);

        if (maxIndex > minIndex)
            return prices[maxIndex] - prices[minIndex];
        return 0;
    }
}