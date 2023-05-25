public class Solution {
    public int InversePairs(int[] array) {
        if (array == null || array.length == 0) {
            return (int) (res % 1000000007);
        }
        int n = array.length;
        temp = new int[n];
        for (int i = 1; i < n; i = i + i) {
            for (int j = 0; j < n - i; j += i + i) {
                work(array, j, j + i - 1, Math.min(j + i + i - 1, n - 1));
            }
        }
        return (int) (res % 1000000007);
    }

    private int[] temp;
    private long res = 0;

    private void work(int[] array, int l, int m, int h) {
        int i = l, j = m + 1;
        for (int k = l; k <= h; k++) {
            temp[k] = array[k];
        }
        for (int k = l; k <= h; k++) {
            if (i > m) {
                array[k] = temp[j++];
            } else if (j > h) {
                array[k] = temp[i++];
            } else if (temp[j] < temp[i]) {
                array[k] = temp[j++];
                res += 1 + m - i;
            } else {
                array[k] = temp[i++];
            }
        }
    }
}