#include <iostream>
#include <fstream>
using namespace std;


int main() {

    ifstream f("bac.txt");
    
    int a;

    while (f >> a) {

        cout << a << "\n";

    cout << endl;

    return 0;

}