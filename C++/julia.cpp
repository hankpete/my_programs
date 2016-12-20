#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

int main() 
{


	int Nx = 500;
	int Ny = 1000;
	double Lx = 2.0;
	double Ly = 1.0;
	int A[Ny][Nx]; //transpose
		
	int diverge = 10000;
	int converge = 100;

	double a;
	double b;
	for (int i = 0; i < Nx; i++)
	{
		a = -Lx + 2*i*Lx/Nx;
		for (int j = 0; j < Ny; j++)
		{
			b = -Ly + 2*j*Ly/Ny;

			double r = 0;
			double t = 0; 
			int c = 0;
		
			A[i][j] = 0;

			double new_a = 0;
			double new_b = 0;
			while (r < diverge)
			{
		       		new_a = a + r * cos(t);
		       		new_b = b + r * sin(t);

				if (c > converge)
				{
					A[j][i] = 1; 
					break;
				} else
				{
					c++;
				}
 
		       		//multiply complex number by itself
		       		//(a + bi)^2
		       		//use polar coordinates
		       		
		       		r = sqrt( pow(new_a, 2) + pow(new_b, 2) );
		       		t = atan( new_b / new_a );

		       		r *= r;
		       		t += t; 
			}	
		}
	}
	
	//write A to file
	ofstream file;
	file.open("A_julia.txt");
	for (int i = 0; i < Nx; i++)
	{
		for (int j = 0; j < Ny; j++) 
		{
			file << A[i][j] << " ";
		}
		file << "\n";
	}
	file.close();

	return 0;
}
