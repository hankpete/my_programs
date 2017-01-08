#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

int main() 
{
	//This program does some calculations to make an array to plot
	int N;
	cout << "Array size, N: ";
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

	//use heap instead of stack:
	int * A = new int[N * N];  //A points to 1D array
		
	int diverge = 1000;
	int converge = 200;

	double a;
	double b;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			a = -L + 2*i*L/N;
			b = -L + 2*j*L/N;
		
			A[i*N + j] = 0;

			double r;
			double t;

			for (int c = 0; c < converge; c++)
			{

		       		r = sqrt( pow(a, 2) + pow(b, 2) );
		       		t = atan( b / a );
				
				if (r > diverge)
				{
					A[i*N + j] = c;
					break;
				}

		       		//multiply complex number by itself
		       		//(a + bi)^2
		       		//use polar coordinates
		       		r *= r;
		       		t += t; 

				//add julia constants
		       		a = Ja + r * cos(t);
		       		b = Jb + r * sin(t);

			}	
		}
	}
	
	//write A to file
	ofstream file;
	file.open("A_julia.txt");
	file << "N = " << N << "\n";
	for (int i = 0; i < N*N; i++)
	{
		file << A[i] << "\n";
	}
	file.close();

	//release memory 
	delete[] A;

	return 0;
}
