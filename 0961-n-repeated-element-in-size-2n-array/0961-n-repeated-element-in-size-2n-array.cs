public class Solution {
    public int RepeatedNTimes(int[] nums) {
        var dict = new Dictionary<int, int>();
        foreach (var num in nums){
            dict.TryGetValue(num, out int count);
            dict[num] = count + 1;
        }
        foreach(var pair in dict)
            if (pair.Value > 1)
                return pair.Key;
        return 0;
    }
}