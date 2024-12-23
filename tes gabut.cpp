#include <iostream>
#include <string>

using namespace std;

int main() {
    string nim;

    cout << "Masukkan nim (contoh: F55124001): ";
    cin >> nim;

    // Mengambil bagian angka dari nim
    string t = nim.substr(6,3);
    int angka = stoi(t); // Mengonversi string menjadi integer

    // Menentukan kelas berdasarkan rentang
    if (angka >= 1 && angka <= 40) {
        cout << "nim " << nim << " termasuk dalam Kelas A." << endl;
    } else if (angka >= 41 && angka <= 80) {
        cout << "nim " << nim << " termasuk dalam Kelas B." << endl;
    } else if (angka >= 81 && angka <= 120) {
        cout << "nim " << nim << " termasuk dalam Kelas C." << endl;
    } else {
        cout << "nim " << nim << " tidak termasuk dalam kelas yang valid." << endl;
    }
    //menentukan angkatan
    string t2 = nim.substr(4,2);
    int angka2 = stoi(t2);

    if (angka2 == 22) {
        cout << " Angkatan 22 " << endl;
    } else if (angka2 == 23) {
        cout << " Angkatan 23 " << endl;
    } else if (angka2 == 24) {
        cout << " Angkatan 24 " << endl;
    } else {
        cout << " lu Angkatan Anomali " << endl;
    }


    return 0;
}
