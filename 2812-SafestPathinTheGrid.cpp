#include <vector>
#include <queue>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        auto isInBound = [&](int r, int c) {
            return r >= 0 && r < n && c >= 0 && c < n;
        };

        // Initialize distances and queue
        vector<vector<int>> dist(n, vector<int>(n, INT_MAX));
        queue<pair<int, int>> q;

        // Add all 1s to the queue and set their distance to 0
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1) {
                    dist[r][c] = 0;
                    q.push({r, c});
                }
            }
        }

        // BFS to calculate minimum distance from each cell to nearest 1
        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();
            for (const auto& dir : directions) {
                int nr = r + dir.first;
                int nc = c + dir.second;
                if (isInBound(nr, nc) && dist[nr][nc] == INT_MAX) {
                    dist[nr][nc] = dist[r][c] + 1;
                    q.push({nr, nc});
                }
            }
        }

        // Initialize maxDistance and queue for the second BFS
        vector<vector<int>> maxDistance(n, vector<int>(n, 0));
        q.push({0, 0});
        maxDistance[0][0] = dist[0][0];

        // BFS to calculate maximum safeness factor for each cell
        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();
            for (const auto& dir : directions) {
                int nr = r + dir.first;
                int nc = c + dir.second;
                if (isInBound(nr, nc)) {
                    int newDistance = min(maxDistance[r][c], dist[nr][nc]);
                    if (newDistance > maxDistance[nr][nc]) {
                        maxDistance[nr][nc] = newDistance;
                        q.push({nr, nc});
                    }
                }
            }
        }

        return maxDistance[n - 1][n - 1];
    }
};