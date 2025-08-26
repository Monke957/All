#include <iostream>
#include <string>
using namespace std;

string charToBinary(char c) {
    int asciivalue = (int)c;
    string binary = "";



    for (int i = 7; i >= 0; i--)
    {
        int bit = (asciivalue >> i) & 1;
        
        if (bit == 0)
        {
            binary += to_string(rand() % 5);
        }
        else 
        {
            binary += to_string(5 + (rand() % 5));
        }
    }

    return binary;
}




int main() {
    
    srand((unsigned) time(NULL));


    string sentence;
    char YorN;


    cout << "___TEXT TO BIN___" << endl;
    cout << " " << endl;

    do
    {
        cout << "Encrypt: ";
        getline(cin, sentence);

        cout << endl;
        cout << "binary encryption: ";
        for (int i = 0; i < sentence.length(); i++)
        {
            cout << charToBinary(sentence[i]) << " ";
        }
        
        cout << endl;
        cout << endl;
        cout << "would you like to encrypt something more? type 'Y' to contiue. Type anything else to quit: ";
        cin >> YorN;  
    } while (YorN == 'Y' || YorN == 'y');
    

    return 0;

}