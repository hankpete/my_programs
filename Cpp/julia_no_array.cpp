#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

int main() 
{
	//This program does some calculations to make an array to plot
	int N;
	cout << "Grid size, N: ";
	cin >> N;
	double L;
       	cout << "Size of bounding box, L: ";
	cin >> L;	
	double Ja;
	cout << "Real part of complex constant, Ja: ";
	cin >> Ja;
	double Jb;
	cout << "Imaginary part of complex constant, Jb: ";
	cin >> Jb;

	//begin file
	ofstream file;
	file.open("A_julia.txt");
	file << "N = " << N << "\n";

	int diverge = 1000;
	int converge = 200;

	double a;
	double b;
	double r;
	double t;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			a = -L + 2*i*L/N;
			b = -L + 2*j*L/N;
		

			for (int c = 0; c < converge; c++)
			{

				//get polars
		       		r = sqrt( pow(a, 2) + pow(b, 2) );
		       		t = atan( b / a );
				
		       		//multiply complex number by itself
		       		//(a + bi)^2
		       		//use polar coordinates
		       		r *= r;
		       		t += t; 

				//add julia constants
		       		a = Ja + r * cos(t);
		       		b = Jb + r * sin(t);

				if (r > diverge)
				{
					file << c << "\n";
					break;
				}
				if (c == converge-1) 
				{
					file << 0 << "\n";
					break;
				}
			}	
		}
	}
	
	file.close();

	//run python code
	system("python3 ../python/julia.py");

	//delete file
	system("rm A_julia.txt");

	return 0;
}
