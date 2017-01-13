//working up to dla

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



int main() {
	
	srand( time(0) ); // use current time as seed

	Particle part(0, 0);

	ofstream file; // output points to a file
	file.open("rand_pts.txt");

	int n;
        cout << "n: ";
	cin >> n;	
	for (int i = 0; i < n; i++) {
		file << part.get_x() << "," << part.get_y() << "\n";
		part.move();
	}
	file.close();

	//run the python code
	system("python3 ../python/rand_walk.py");

	//delete file
	system("rm rand_pts.txt");

	return 0;
}

