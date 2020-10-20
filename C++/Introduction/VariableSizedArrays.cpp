#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n, q, value, size, r, c;
    cin >> n >> q;

    vector<vector<int>> nvec;

    // populate
    for (int i = 0; i < n; ++i){
        cin >> size;
        vector<int> ivec;
        for (int j = 0; j < size; ++j){
            cin >> value;
            ivec.push_back(value);
        }
        nvec.push_back(ivec);
    }

    // query
    for (int k = 0; k < q; ++k){
        cin >> r >> c;
        cout << nvec[r][c] << endl; 
    }

    return 0;
}