#include <iostream>
#include <fstream>
using namespace std;


int main() {

    ifstream f("bac.txt");
    int a, previous = -1, maxim = -1;

    while (f >> a) {

        if (a > maxim || a == previous) {
            cout << a << " ";
            maxim = a;
            previous = a;
        }
        else {
            previous = -1;
        }
    }

    cout << endl;

    return 0;
}