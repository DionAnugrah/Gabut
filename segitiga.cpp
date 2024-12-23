#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    cout << endl;

    //1
    for (int i = 1 ; i <= n ; i++){
        for (int j = 1 ; j <= i; j++){
            cout << "*";
        } cout << endl;
    }
    cout << endl;

    //2
    for (int i = 1 ; i <= n ; i++){
        for (int j = n ; j >= i; j--){
            cout << "*";
        } cout << endl;
    }
    cout << endl;

    //3
    for (int i = 1 ; i <= n ; i++){
        for (int j = 1 ; j <= i; j++){
            cout << " ";
        }
        for (int k = n ; k >= i ; k--){
            cout << "*";
        }
        cout << endl;
    }
    cout << endl;

    //4
    for (int i = 1 ; i <= n ; i++){
        for (int j = n ; j >= i; j--){
            cout << " ";
        }
        for (int k = 1 ; k <= i ; k++){
            cout << "*";
        }
        cout << endl;
    }
    cout << endl;

    //5
    for (int i = 5 ; i <= n ; i++){
        for (int j = n ; j >= i; j--){
            cout << " ";
        }
        for (int k = 1 ; k <= (2*i-1) ; k++){
            cout << "*";
        }
        cout << endl;
    }
    cout << endl;

    //6
    for (int i = 1 ; i <= n ; i++){
        for (int j = 1 ; j <= i; j++){
            cout << " ";
        }
        for (int k = n ; k >= (2*i-n) ; k--){
            cout << "*";
        }
        cout << endl;
    }
    cout << endl;

    //7
    for (int i = 1 ; i <= n ; i++){
        for (int j = n ; j >= i; j--){
            cout << " ";
        }
        for (int k = 1 ; k <= (2*i-1) ; k++){
            cout << "*";
        }
        cout << endl;
    }
    for (int i = 1 ; i <= n ; i++){
        for (int j = 1 ; j <= i; j++){
            cout << " ";
        }
        for (int k = n ; k >= (2*i-n) ; k--){
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}

