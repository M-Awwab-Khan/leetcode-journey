class Solution {
public:
    vector<int> findPeakGrid(vector<vector<int>>& mat) {
        int lcol = 0;
        int rcol = mat[0].size() - 1;

        while (lcol <= rcol) {
            int mcol = (lcol + rcol) / 2;
            int mx_row = 0;

            for (int row = 0; row < mat.size(); row++) {
                if (mat[row][mcol] > mat[mx_row][mcol]) {
                    mx_row = row;
                }
            }

            bool leftIsBig = ( mcol - 1 >= 0) && (mat[mx_row][mcol-1] > mat[mx_row][mcol]);
            bool rightIsBig = ( mcol + 1 < mat[0].size()) && (mat[mx_row][mcol+1] > mat[mx_row][mcol]);

            if ((!leftIsBig) && (!rightIsBig)) {
                vector<int> result {mx_row, mcol};
                return result;
            } else if (rightIsBig) {
                lcol = mcol + 1;
            } else {
                rcol = mcol - 1;
            }
        }
        return vector<int> {};
    }
};