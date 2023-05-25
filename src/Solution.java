public class Solution {
    public int InversePairs(int[] array) {
        int p = 0;

        return getP(p);
    }

    int getP(int p) {
        return p % 1000000007;
    }
}
