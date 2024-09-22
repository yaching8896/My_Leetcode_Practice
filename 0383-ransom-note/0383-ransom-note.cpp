class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int rp = 0;
        int mp = 0;

        while(rp < ransomNote.length() && mp < magazine.length()){
            if (ransomNote[rp] == magazine[mp]){
                rp++;
            }
            mp++;
        }
        return ransomNote.length() == rp;
    }
};