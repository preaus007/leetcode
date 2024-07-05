#include<bits/stdc++.h>
using namespace std;

int main()
{
    int test_case;
    scanf("%d",&test_case);
    while(test_case--)
    {
        string s;
        cin >> s;

        int arr[26] = {0};

        for(int i=0; i<s.size(); i++)
        {
            arr[s[i] - 'a']++;
        }

        bool flag = false;
        for(int i=0; i<26; i++)
        {
            if(arr[i] > 1)
            {
                flag = true;
                break;
            }
        }

        flag ? cout << "Yes\n" : cout << "No\n";

    }
}
