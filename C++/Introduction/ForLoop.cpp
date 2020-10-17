#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int a, b;
    string num[10] = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

    cin >> a >> b;

    for (int n = a; n <= b; n++){
        cout << ((n<=9)?num[n]:((n%2==0)?"even":"odd")) << endl;
    }

    return 0;
}
