// Increment content of a variable using pointers
// Complexity= M

#include<iostream>

using namespace std;
int main(){
	int a = 10;
	int* p=a;   //Solved bug
	cout << ++p << endl; 
	return 0;
}

