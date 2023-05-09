public class Solution {
    public int FindGreatestSumOfSubArray(int[] array) {
        if (array == null)
            return 0;
        if (array.length == 0)
            return 0;
        int min = 0;
        int minNum = 0;
        int tmp = 0;
        for (int i = 0; i < array.length; i++) {
            tmp = tmp + array[i];
            if (tmp < min) {
                min = tmp;
                minNum = i;
            }
        }
        return 1;
    }
}
