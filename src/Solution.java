import java.util.*;

public class Solution {
    int[][] table;
    int result = 0;

    public int rectCover(int target) {
        if (target == 0)
            return 0;
        table = new int[target][target];

        return result;
    }

    void function() {
        int tmp = 0;
        for (int[] i : table) {
            for (int j : i) {
                tmp = tmp | j;
            }
        }

    }
}
