#include <bits/stdc++.h>
#include <regex>

using namespace std;

int main()
{
    system("cls");

    string input;

    cout<< "Enter A String: ";
    getline(cin,input);

    regex reg("BA*");

    if (regex_match(input, reg))
    {
        cout << "Input matches the regex\n";
    }
    else
    {
        cout << "Input does not match the regex\n";
    }

    cout<<"Do you want to run again? (1 for Yes, 2 for No)"<<endl;
    int choice;
    cin>>choice;
    if(choice == 1)
    {
        closegraph();
        main();
    }
    else if(choice == 2)
    {
        return 0;
    }
}
