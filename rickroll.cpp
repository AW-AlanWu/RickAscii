#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <stdlib.h>

using namespace std;

int main() {
    //把檔案全部讀到stringstream裡面
    stringstream ss;

    char temp[15];
    for(int i = 1; i <= 3180; i++) {
        sprintf(temp, "ascii/%04d.txt", i);
        ifstream ifs(temp, ios::in);
        if (!ifs.is_open()) {
            cout << "Can't Open Image File";
            return 1;
        }
        ss << ifs.rdbuf();
        ifs.close();
    }

    //前置動作
    system("cls");
    cout << "Hey kids! you're gonna have a good time..\nPress to continue";
    getchar();
    system("cls");

    //從stringstream中印出來
    string str;
    int i = 0;
    while(getline(ss, str)) {
        if(i >= 72) {
            system("cls");
            i = 0;
        }
        cout << str << "\n";
        i++;
    }
    return 0;
}