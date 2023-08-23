public class Solution{


    void getNext(String p, int next[]) {
        int j = 0;
        int k = -1;
        next[0] = -1;
        while (j < p.length()-1) {
          if (k == -1 || p.charAt(j) == p.charAt(k)) {
            j++;
            k++;
            next[j] = k; 
          } else {
            k = next[k];
          }
        }
      }
      
      int kmp(String s, String p) {
        int i = 0;
        int j = 0;
        int[] next=new int[p.length()];
        getNext(p, next);
      
        while (i < s.length() && j < p.length()) {
          if (j == -1 || s.charAt(i) == p.charAt(j)) {
            i++;
            j++;
          } else {
            j = next[j]; 
          }
        }
      
        if (j == p.length()) {
          return i - j;
        } else {
          return -1;
        }
      }



}