package JanWeekFiveChallenges;
/**
 * MixedSorting
 */

import java.util.*;

public class MixedSorting {
    public static void main(String[] args) {

        int[] nums = new int[8, 13, 11, 90, -5, 4];
        solve(nums);

    }

    public int[] solve(int[] nums) {
        /*
        1) get sorted even list & sorted odds list
        2) create output array, int SortedEvenInt = 0, SortedOddInt = 0;
        3) for(int i = 0; i < nums.length(); i++){
            if(nums[i] % 2 = 0){
                output[i].push(SortedEvenList[SortedEvenInt]);
                SortedEvenInt++;
            }
            else{
                output[i].push(SortedOddsList[SortedOddInt]);
                SortedOddInt++;
            }
        }

        */

        int Ec = 0, Oc = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] % 2 == 0){
                Ec++;
            }
            else Oc++;
        }

        int[] SortedEvens = new int[Ec];
        int[] SortedOdds = new int[Oc];
        int[] Output = new int[nums.length];
        int sE = 0, sO = 0;

        for(int i = 0; i < nums.length; i++){
            if(nums[i] % 2 == 0){
                SortedEvens[sE] += nums[i];
                sE++;
            }
            else{
                SortedOdds[sO] += nums[i];
                sO++;
            }
        }
        Arrays.sort(SortedEvens);
        Arrays.sort(SortedOdds);
        sE = 0;
        Oc--;

        for(int i = 0; i < nums.length; i++){
            if(nums[i] % 2 == 0){
                Output[i] += SortedEvens[sE];
                sE++;
            }
            else{
                Output[i] += SortedOdds[Oc];
                Oc--;
            }
        }

        return Output;
    }
}


