#include <iostream>
#include <algorithm> // for std::remove
#include <fstream>
#include <string>
#include <minizip/unzip.h>

int main() {
    std::string zipPath, passList;
    int number = 0;

    // Clear console (cross-platform)
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif

    // Input ZIP path
    std::cout << "File path = ";
    std::getline(std::cin, zipPath);
    // Remove quotes if any
    zipPath.erase(std::remove(zipPath.begin(), zipPath.end(), '\"'), zipPath.end());
    zipPath.erase(std::remove(zipPath.begin(), zipPath.end(), '\''), zipPath.end());

    // Input password list
    std::cout << "Password list = ";
    std::getline(std::cin, passList);
    passList.erase(std::remove(passList.begin(), passList.end(), '\"'), passList.end());
    passList.erase(std::remove(passList.begin(), passList.end(), '\''), passList.end());

    // Open ZIP file
    unzFile zipFile = unzOpen(zipPath.c_str());
    if (!zipFile) {
        std::cout << "Cannot open ZIP file.\n";
        return 1;
    }

    std::ifstream file(passList);
    if (!file.is_open()) {
        std::cout << "Cannot open password list.\n";
        unzClose(zipFile);
        return 1;
    }

    std::string password;
    bool success = false;

    while (std::getline(file, password)) {
        number++;
        password.erase(password.find_last_not_of(" \n\r\t") + 1); // trim newline

        std::cout << "Testing: " << password;

        if (unzGoToFirstFile(zipFile) != UNZ_OK) {
            std::cout << " Archive.broken(failed)\n";
            continue;
        }

        if (unzOpenCurrentFilePassword(zipFile, password.c_str()) == UNZ_OK) {
            std::cout << "\nArchive.broken(success)\n";
            std::cout << "Password: " << password << "\n";
            std::cout << "Attempts: " << number << "\n";
            success = true;
            unzCloseCurrentFile(zipFile);
            break;
        } else {
            std::cout << " Archive.broken(failed)\n";
        }
    }

    if (!success) {
        std::cout << "Password not found after " << number << " attempts.\n";
    }

    unzClose(zipFile);
    std::cout << "Press enter to exit...";
    std::cin.ignore();
    return 0;
}
