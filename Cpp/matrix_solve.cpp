//take a simple matrix and put it in reduced row echelon form
#include <iostream>
using namespace std;

int main() {
	int r = 2, c =3;
	double A[r][c] = { {2, 4, 8}, {3, 2, 1} };

	cout << "Initial Matrix:\n";
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			cout << A[i][j] << " ";
		}
		cout << "\n";
	}

	//first, divide row by its main entry
	double leading = A[0][0];
	for (int i = 0; i < c; i++) {
		A[0][i] /= leading;
	}
	cout << "Scaled:\n";
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			cout << A[i][j] << " ";
		}
		cout << "\n";
	}
	//now add a scaled version of that row to the one below it to cancel
	leading = A[1][0];
	for (int i = 0; i < c; i++) {
		A[1][i] += -leading * A[0][i]; 
	}
	cout << "One elimination:\n";
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			cout << A[i][j] << " ";
		}
		cout << "\n";
	}
	//divide again
	leading = A[1][1];
	for (int i = 0; i < c; i++) {
		A[1][i] /= leading; 
	}
	cout << "Row Echelon:\n";
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			cout << A[i][j] << " ";
		}
		cout << "\n";
	}
	//add scaled version of lower row to higher to eliminate
	leading = A[0][1];
	for (int i = 0; i < c; i++) {
		A[0][i] += -leading * A[1][i];
	}
	cout << "Reduced Row Echelon:\n";
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			cout << A[i][j] << " ";
		}
		cout << "\n";
	}

	return 0;
}
