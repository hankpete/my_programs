//diffusion limited aggregation with object starting at center

#include <iostream>
#include <fstream>
using namespace std;

class Particle {
	private:
		int x, y;
	public:
		Particle(int x0, int y0) { // make it so that initialized particle has postion
			x = x0; y = y0;
		}
		void set_x_y(int x0, int y0) { //also have a func to change them
			x = x0; y = y0;
		}
		void print_x_y() {
			cout << "(" << x << ", " << y << ")\n";
		}
		int get_x() { return x; }
		int get_y() { return y; }
		void move() { // take a step
			int r = rand();
			r = r % 5; // mod 5 for the 5 cases 
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
				case 4: 
					break; //stay in same spot
			}
		}
};



int main() {
	
	srand( time(0) );

	int i, j, k, n, x;

	//create grid w spots at center
	int N = 6;
	int A[N][N] = {0};
	A[N / 2 - 1][N / 2 - 1] = 1;
	A[N / 2 - 1][N / 2] = 1;
	A[N / 2][N / 2 - 1] = 1;
	A[N / 2][N / 2] = 1;

	int unused[N * N][2] = {0}; //array to keep track of which points arent taken
	int index = 0;
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			cout << A[i][j] << " ";
			if (A[i][j] == 0) {
				unused[index][0] = i;
				unused[index][1] = j;
				index++;
			} 
		}
		cout << "\n";
	}

	int unused_len = index;

	int loops = 10;
	int rand_i;

	Particle part(0, 0);

	/*
	int iL,iR,jD,jU;
	for (n = 0; n < loops; n++) {
		cout << n;
		
		rand_i = rand() % unused_len;
		i = unused[rand_i][0];
	       	j = unused[rand_i][1];
		part.set_x_y(i, j);

		while (1) {
			//periodic boundary conditions
			iL = i - 1 % N;
			iR = i + 1 % N;
			jD = j - 1 % N;
			jU = j + 1 % N;
			if (A[iL][j] == 1 || A[iR][j] == 1 || A[i][jD] == 1 || A[i][jU] == 1) {
				A[i][j] = 1;
				for (k = 0; k < unused_len; k++) {
					if (unused[k][0] == i && unused[k][1] == j) {
						for (x = k; x < unused_len - 1; x++) {
							unused[x][0] = unused[x + 1][0];
							unused[x][1] = unused[x + 1][1];
						}
						unused_len--;
					}
				}
				break;
			} else {
				part.move();
				part.set_x_y( part.get_x() % N, part.get_y() % N); //pbc
			}
		}
	}
						
	ofstream file;
	file.open("dla_grid.txt");
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			file << A[i][j] << " ";
		}
		file << "\n";
	}
	file.close();
		

	
	//run the python code
	//system("python3 ../python/dla_center.py");

*/	
	return 0;
}

