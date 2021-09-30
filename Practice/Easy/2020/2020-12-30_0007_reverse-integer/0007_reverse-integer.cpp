class Solution {
public:
    int reverse(int x) {
        long long int longx = x;
        long long int ans = 0;
        while (longx != 0)
        {
            ans = ans * 10 + longx % 10;
            longx = longx / 10;
        }
        if (ans > INT_MAX || ans < INT_MIN) return 0;
        return (int) ans;
    }
};
