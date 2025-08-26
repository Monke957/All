#include <iostream>
#include <string>
#include <bitset>

using namespace std;




int main() {
    string binInput;
    string cleanInput;
    string end;
    


    

    cout << "____BINARY DECRYTPOR____\n";
    cout << " " << endl;
    cout << " " << endl;
    
    
    
    cout << "Enter your BIN: ";
    getline(cin, binInput);




    for (char c : binInput)
    {
        if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9') {
           cleanInput += c;
        }
        
    }
    
    bool isEncrypted = false;
    for (char c :cleanInput) {
        if (c != '0' && c != '1'){
            isEncrypted = true;
            break;
        }
    }


    if (isEncrypted) {
        string decrypted = "";
        for (char c : cleanInput) {
            if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4'){
                decrypted += '0';
            }
           else if(c == '5' || c == '6' || c == '7' || c == '8' || c == '9') {
            decrypted += '1';
            }
            else {
                decrypted += c;
            }
        }   
        cleanInput = decrypted;
    }





    if (cleanInput.length() % 8 != 0)
    {
        cout << "Error: BIN length must be '8' no more, no less\n";
        cout << "You entered " << cleanInput.length() << " bits.\n";
        return 1;
    }
    
    cout << "\nDecrypted: ";

    for (int i = 0; i < cleanInput.length(); i += 8)
    {
        string byte = cleanInput.substr(i, 8);
        bitset<8> bits(byte);
        char character = static_cast<char>(bits.to_ulong());
        cout << character;
    }
    



    cout << endl;
    cout << endl;
    cout << "Press enter to quit";
    cin.ignore();
    
    return 0;

}
