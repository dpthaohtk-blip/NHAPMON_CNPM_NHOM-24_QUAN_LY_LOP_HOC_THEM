#include <iostream>
#include <string>

using namespace std;

int main() {
    // Khai báo biến lưu thông tin gia sư
    string maSo, hoTen, lichDay;

    // Nhập thông tin từ bàn phím
    cout << "Nhap ma so gia su: ";
    getline(cin, maSo);
    
    cout << "Nhap ho ten: ";
    getline(cin, hoTen);
    
    cout << "Nhap lich day: ";
    getline(cin, lichDay);

    // Xuất thông tin vừa nhập ra màn hình
    cout << "\n--- THONG TIN GIA SU ---\n";
    cout << "Ma so: " << maSo << endl;
    cout << "Ho ten: " << hoTen << endl;
    cout << "Lich day: " << lichDay << endl;

    return 0;
}