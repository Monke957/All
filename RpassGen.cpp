#include <iostream>
#include <string>

using namespace std;

int main() {
    string finalpass;
    int options;
    string charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
    char YorN;

    srand(time(NULL));


    cout << "RANDOM PASSWORD GENERATOR" << endl;
    do
    {
        cout << "----------------------------------------------" << endl;
        cout << "\n\n";
        cout << "How long do you want your password?: ";
        cin >> options;

        int length = options;

        if(options == 0) {
            cout << "\n";
            cout << "ERROR: That is not a valid number.";
            cout << "\n";
            return 1;
        }


        cout << "\n\nNew password: ";
        
        for (int i = 0; i < options; i++)
        {
            int randomIndex = rand() % charset.length();

            cout << charset[randomIndex];
        }


        
        cout << "\n\nType 'Y' to generate a new pass or type anything else to exit: ";

        cin >> YorN;

    } while (YorN == 'Y' || YorN == 'y');
    




    return 0;



}