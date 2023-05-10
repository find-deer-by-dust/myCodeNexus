public class Solution {
    public int FindGreatestSumOfSubArray(int[] array) {
        if (array == null)
            return 0;
        if (array.length == 0)
            return 0;
        int min = 0;
        int minNum1 = -1;
        int minNum2 = array.length;
        int tmp = 0;
        for (int i = 0; i < array.length; i++) {
            tmp = tmp + array[i];
            System.out.println(min);
            System.out.println(tmp);
            if (tmp < min) {
                min = tmp;
                minNum1 = i;
            }
        }
        min = 0;
        tmp = 0;
        for (int i = array.length - 1; i >= 0; i--) {
            tmp = tmp + array[i];
            if (tmp < min) {
                min = tmp;
                minNum2 = i;
            }
        }
        int re = 0;

        // System.out.println(minNum1);
        // System.out.println(minNum2);

        for (int i = minNum1 + 1; i < minNum2; i++)
            re = re + array[i];
        return re;
    }
}
