/*
============================================================
Platform   : LeetCode
Problem    : 1. Two Sum
Language   : C++
Difficulty : Easy

Approach:
- Iterate through all possible pairs of elements.
- Check if the sum of the current pair equals the target.
- If a matching pair is found, return their indices.
- If no pair is found, return an empty vector.

Time Complexity : O(n²)
Space Complexity: O(1)

Author : Abhijit Behera
============================================================
*/

#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //int sum = 0;
        int length = nums.size();
        for(int i = 0; i < length; i++){
            for (int j = i+1; j < length; j++){
                if((nums[i] + nums[j]) == target){
                    vector<int> result = {i, j};
                    return result;
                }
                    
            }
            
        }
        return {};
    }
};