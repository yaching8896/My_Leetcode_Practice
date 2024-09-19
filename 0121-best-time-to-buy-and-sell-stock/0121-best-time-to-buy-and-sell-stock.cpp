class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = 0, profit = 0;

        for(int i = 1; i < prices.size(); i++){
            if(prices[i] < prices[buy]) 
            buy = i;
            else 
            profit = std::max(profit, prices[i]-prices[buy]);
        }
        return profit;
    }
};