#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>

using namespace std;

int correctAnswer = 0;
bool Q1 = true;
bool Q2 = false;
bool Q3 = false;
bool Q4 = false;
bool Q5 = false;
bool Q6 = false;
bool Q7 = false;
bool Q8 = false;
bool Q9 = false;
bool Q10 = false;

string toLower(string str) {
    transform(str.begin(), str.end(), str.begin(), ::tolower);
    return str;
}

void question1()
{
    string choice;   
    cout << "What coding language is known as 'C' with more features?\n\n";
    cout << "1. 'C++' \n";
    cout << "2. 'C#' \n";
    cout << "3. 'C-ex' \n";
    cout << "4. 'Rust' \n\n";
    cout << "Type your answer: ";
    cin >> choice;
    
    string lowerChoice = toLower(choice);
    
    if (lowerChoice == "c#" || lowerChoice == "c-ex" || lowerChoice == "rust" || lowerChoice == "2" || lowerChoice == "3" || lowerChoice == "4") {
        Q1 = false;
        Q2 = true;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else if (lowerChoice == "c++" || lowerChoice == "1") {
        correctAnswer++;
        Q1 = false;
        Q2 = true;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else {
        cout << "ERROR: That was not a valid choice.";
        system("cls"); 
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
}

void question2()
{
    string choice;
    cout << "Which keyword is used to include a library in C++?\n\n";
    cout << "1. '#include' \n";
    cout << "2. '#use' \n";
    cout << "3. '#import' \n";
    cout << "4. '--->' \n\n";
    cout << "Type your answer: ";
    cin >> choice;
    
    string lowerChoice = toLower(choice);
    
    if (lowerChoice == "#use" || lowerChoice == "#import" || lowerChoice == "--->" || lowerChoice == "2" || lowerChoice == "3" || lowerChoice == "4") {
        Q2 = false;
        Q3 = true;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else if (lowerChoice == "#include" || lowerChoice == "1") {
        correctAnswer++;
        Q2 = false;
        Q3 = true;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else {
        cout << "ERROR: That was not a valid choice.";
        system("cls"); 
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
}

void question3()
{
    string choice;
    cout << "What symbol is used for single line Comments in C++?\n\n";
    cout << "1. '//' \n";
    cout << "2. '/*' \n";
    cout << "3. '#' \n";
    cout << "4. '--' \n\n";
    cout << "Type your answer: ";
    cin >> choice;
    
    string lowerChoice = toLower(choice);
    
    if (lowerChoice == "/*" || lowerChoice == "#" || lowerChoice == "--" || lowerChoice == "2" || lowerChoice == "3" || lowerChoice == "4") {
        Q3 = false;
        Q4 = true;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else if (lowerChoice == "//" || lowerChoice == "1") {
        correctAnswer++;
        Q3 = false;
        Q4 = true;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else {
        cout << "ERROR: That was not a valid choice.";
        system("cls"); 
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
}

void question4()
{
    string choice;
    cout << "Which of these is NOT a valid programming loop structure in C++?\n\n";
    cout << "1. 'for' \n";
    cout << "2. 'while' \n";
    cout << "3. 'do-while' \n";
    cout << "4. 'repeat-until' \n\n";
    cout << "Type your answer: ";
    cin >> choice;
    
    string lowerChoice = toLower(choice);
    
    if (lowerChoice == "for" || lowerChoice == "while" || lowerChoice == "do-while" || lowerChoice == "1" || lowerChoice == "2" || lowerChoice == "3") {
        Q4 = false;
        Q5 = true;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else if (lowerChoice == "repeat-until" || lowerChoice == "4") {
        correctAnswer++;
        Q4 = false;
        Q5 = true;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else {
        cout << "ERROR: That was not a valid choice.";
        system("cls"); 
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
}

void question5()
{
    string choice;
    cout << "What is the name of this operator(%) in C++?\n\n";
    cout << "1. 'Percent' \n";
    cout << "2. 'Modulus' \n";
    cout << "3. 'Divider' \n";
    cout << "4. 'Bitwise' \n\n";
    cout << "Type your answer: ";
    cin >> choice;
    
    string lowerChoice = toLower(choice);
    
    if (lowerChoice == "percent" || lowerChoice == "divider" || lowerChoice == "bitwise" || lowerChoice == "1" || lowerChoice == "3" || lowerChoice == "4") {
        Q5 = false;
        Q6 = true;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else if (lowerChoice == "modulus" || lowerChoice == "2") {
        correctAnswer++;
        Q5 = false;
        Q6 = true;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else {
        cout << "ERROR: That was not a valid choice.";
        system("cls"); 
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
}

void question6()
{
    string choice;
    cout << "Which language is known for primarily being used to style websites?\n\n";
    cout << "1. 'JavaScript' \n";
    cout << "2. 'Python' \n";
    cout << "3. 'CSS' \n";
    cout << "4. 'SQL' \n\n";
    cout << "Type your answer: ";
    cin >> choice;
    
    string lowerChoice = toLower(choice);
    
    if (lowerChoice == "javascript" || lowerChoice == "python" || lowerChoice == "sql" || lowerChoice == "1" || lowerChoice == "2" || lowerChoice == "4") {
        Q6 = false;
        Q7 = true;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else if (lowerChoice == "css" || lowerChoice == "3") {
        correctAnswer++;
        Q6 = false;
        Q7 = true;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else {
        cout << "ERROR: That was not a valid choice.";
        system("cls"); 
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
}

void question7()
{
    string choice;
    cout << "What is the file extension for a C++ file?\n\n";
    cout << "1. '.c' \n";
    cout << "2. '.cpp' \n";
    cout << "3. '.cplus' \n";
    cout << "4. '.cs' \n\n";
    cout << "Type your answer: ";
    cin >> choice;
    
    string lowerChoice = toLower(choice);
    
    if (lowerChoice == ".c" || lowerChoice == ".cplus" || lowerChoice == ".cs" || lowerChoice == "1" || lowerChoice == "3" || lowerChoice == "4") {
        Q7 = false;
        Q8 = true;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else if (lowerChoice == ".cpp" || lowerChoice == "2") {
        correctAnswer++;
        Q7 = false;
        Q8 = true;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else {
        cout << "ERROR: That was not a valid choice.";
        system("cls"); 
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
}

void question8()
{
    string choice;
    cout << "Which keyword is used to create a constant variable in C++?\n\n";
    cout << "1. 'static' \n";
    cout << "2. 'const' \n";
    cout << "3. 'dynamic' \n";
    cout << "4. 'repeat' \n\n";
    cout << "Type your answer: ";
    cin >> choice;
    
    string lowerChoice = toLower(choice);
    
    if (lowerChoice == "static" || lowerChoice == "dynamic" || lowerChoice == "repeat" || lowerChoice == "1" || lowerChoice == "3" || lowerChoice == "4") {
        Q8 = false;
        Q9 = true;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else if (lowerChoice == "const" || lowerChoice == "2") {
        correctAnswer++;
        Q8 = false;
        Q9 = true;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else {
        cout << "ERROR: That was not a valid choice.";
        system("cls"); 
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
}

void question9()
{
    string choice;
    cout << "What is the name of a whole number that can be positive, negative, or zero in C++?\n\n";
    cout << "1. 'Float' \n";
    cout << "2. 'Double' \n";
    cout << "3. 'Integer' \n";
    cout << "4. 'String' \n\n";
    cout << "Type your answer: ";
    cin >> choice;
    
    string lowerChoice = toLower(choice);
    
    if (lowerChoice == "float" || lowerChoice == "double" || lowerChoice == "string" || lowerChoice == "1" || lowerChoice == "2" || lowerChoice == "4") {
        Q9 = false;
        Q10 = true;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else if (lowerChoice == "integer" || lowerChoice == "3") {
        correctAnswer++;
        Q9 = false;
        Q10 = true;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else {
        cout << "ERROR: That was not a valid choice.";
        system("cls"); 
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
}

void question10()
{
    string choice;
    cout << "Which of these are used for comparing in C++?\n\n";
    cout << "1. '&&' \n";
    cout << "2. '++' \n";
    cout << "3. '==' \n";
    cout << "4. '<->' \n\n";
    cout << "Type your answer: ";
    cin >> choice;
    
    string lowerChoice = toLower(choice);
    
    if (lowerChoice == "&&" || lowerChoice == "++" || lowerChoice == "<->" || lowerChoice == "1" || lowerChoice == "2" || lowerChoice == "4") {
        Q10 = false;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else if (lowerChoice == "==" || lowerChoice == "3") {
        correctAnswer++;
        Q10 = false;
        system("cls");
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
    else {
        cout << "ERROR: That was not a valid choice.";
        system("cls"); 
        cout << "    !The {code} Quiz!       \n";
        cout << "-------------------------\n\n\n";
    }
}

int main() 
{
    cout << "    !The {code} Quiz!       \n";
    cout << "-------------------------\n\n\n";

    do
    {
        question1();
    } while (Q1 == true);
    
    do
    {
        question2();
    } while (Q2 == true);

    do
    {
        question3();
    } while (Q3 == true);

    do
    {
        question4();
    } while (Q4 == true);

    do
    {
        question5();
    } while (Q5 == true);

    do
    {
        question6();
    } while (Q6 == true);

    do
    {
        question7();
    } while (Q7 == true);

    do
    {
        question8();
    } while (Q8 == true);

    do
    {
        question9();
    } while (Q9 == true);

    do
    {
        question10();
    } while (Q10 == true);
        
    cout << "You completed the quiz! your score was: " << to_string(correctAnswer) << "/10!\n\n";

    system("pause");

    

    
    
    
    return 0;
}