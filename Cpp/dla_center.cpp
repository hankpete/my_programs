//diffusion limited aggregation with object starting at center

#include <iostream>
#include <fstream>
using namespace std;

class Particle {
	private:
		int x, y;
	public:
		void set_x_y(int x0, int y0) { //have a func to change them
			x = x0; y = y0;
		}
		void print_x_y() {
			cout << "(" << x << ", " << y << ")\n";
		}
		int get_x() { return x; }
		int get_y() { return y; }
		void move() { // take a step
			int r = rand();
			r = r % 4; // mod 4 for the 4 cases
			switch (r) {
				case 0:
					x++;
					break;
				case 1:
					x--;
					break;
				case 2:
					y++;
					break;
				case 3:
					y--;
					break;
			}
		}
};

int mod(int a, int b) {
	int result = a % b;
	if (result < 0) {
		result += b;
	}
	return result;
}

int main() {

	srand( time(0) );

	int i, j, k, n, g, h;

	//create grid w spots at center
	int N;
	cout << "N: ";
	cin >> N;
	int A[N][N] = {};
	A[N / 2 - 1][N / 2 - 1] = 1;
	A[N / 2 - 1][N / 2] = 1;
	A[N / 2][N / 2 - 1] = 1;
	A[N / 2][N / 2] = 1;

	int unused[N * N][2] = {}; //array to keep track of which points arent taken
	int index = 0;
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			if (A[i][j] == 0) {
				unused[index][0] = i;
				unused[index][1] = j;
				index++;
			}
		}
	}

	int unused_len = index;

	int loops = 10000;
	int rand_i;

	Particle part;

	int iL,iR,jD,jU;
	int new_x, new_y;

	//ask for visual
	char visual;
	cout << "Do you want a terminal visual displayed (y or n)? ";
	cin >> visual;
	for (n = 0; n < loops; n++) {
		//visual
		if (visual == 'y') {
			cout << "Loop number:" << n << "\n";
        		for (g = 0; g < N; g++) {
        		    for (h = 0; h < N; h++) {
				if (A[g][h] == 0) {
					cout << ". ";
				} else {
					cout << "O ";
				}
			    }
        		    cout << "\n";
        		}
		}
		//break if reached edge
		if (i == 0 || j == 0 || i == N - 1 || j == N - 1) {
			break;
		}
		//pick from unused
		rand_i = rand() % unused_len;
		i = unused[rand_i][0];
	       	j = unused[rand_i][1];
		part.set_x_y(i, j);

		while (1) {
			//periodic boundary conditions
			iL = mod(i - 1, N);
			iR = mod(i + 1, N);
			jD = mod(j - 1, N);
			jU = mod(j + 1, N);
			//if next to a point, stick. else continue drifting
			if (A[iL][j] == 1 || A[iR][j] == 1 || A[i][jD] == 1 || A[i][jU] == 1) {
				A[i][j] = 1;
				for (k = rand_i; k < unused_len - 1; k++) {
					unused[k][0] = unused[k + 1][0];
					unused[k][1] = unused[k + 1][1];
				}
				unused_len--;
				break;
			} else {
				part.move();
				i = mod(part.get_x(), N);
				j = mod(part.get_y(), N);
				part.set_x_y(i, j); //pbc
			}
		}
	}

	ofstream file;
	file.open("dla_grid.txt");
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			file << A[i][j];
			if (j < N - 1) {
				file << ", ";
			} else {
				file << "\n";
			}
		}
	}
	file.close();


	//run the python code
	system("python3 ../python/dla_center.py");

	//delete file
	system("rm dla_grid.txt");


	return 0;
}

