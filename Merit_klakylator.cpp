#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

int main()
{
    vector<double> gradeVal;
    string grades;
    string clean_grades;
    double sum = 0;
    double merit = 0;
    const double a = 20, b = 17.5, c_val = 15, d = 12.5, e = 10, f = 0;

    




    cout << "       MERIT KALKYLATOR\n";
    cout << "------------------------------\n\n\n";

    cout << "Skriv dina betyg: ";
    cin >> grades;
    cout << "\n\n";


    if (grades.length() > 18)
    {
        cout << "Error: du kan inte räkna mer betyg än 18.\n\n";
        system("pause");
        return 1;
    }
    



    for (char ch : grades)
    {
        char upperCH = toupper(ch);

        if (upperCH == 'A')
        {
            gradeVal.push_back(a);
        }
        else if (upperCH == 'B')
        {
            gradeVal.push_back(b);
        }
        else if (upperCH == 'C')
        {
            gradeVal.push_back(c_val);
        }
        else if (upperCH == 'D')
        {
            gradeVal.push_back(d);
        }
        else if (upperCH == 'E')
        {
            gradeVal.push_back(e);
        }
        else if (upperCH == 'F')
        {
            gradeVal.push_back(f);
        }
        
        
    }
    

    if (gradeVal.empty())
    {
        cout << "Inga giltiga betyg hittades.\n\n";
        system("pause");
        return 1;  
    }


    double total_poang = gradeVal.size() * 100;
    for (double value : gradeVal) {
        merit += value * 100;  
    }
    merit /= total_poang;  

    for (double value : gradeVal)
    {
        sum += value;
    }

    cout << "din betygs summa: " << sum << "\n";
    cout << "ditt merit varde: " << merit << "\n\n";

    system("pause");

    return 0;
}