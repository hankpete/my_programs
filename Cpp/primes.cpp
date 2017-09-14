#include <iostream>
#include <fstream>

int main() {

	//Sieve
	static int n = 1000000;
	int *A = new int[n];                  //binary array - 0 if index value is prime
	int j = 2;                            //index of last known prime
	A[0] = 1; A[1] = 1;                   //0, 1 not prime
	
	while ( j*j <= n ) {	

		//delete numbers that have j in their PF
		for ( int i = j + j; i < n; i += j ) {
			if ( A[i] == 0 ) {
				A[i] = 1;
			}
		}

		//next prime	
		j++;	
		while (	A[j] == 1 ) {
			j++;
		}

	}
	
	//print primes
	std::ofstream file;
	file.open("primes.txt");
	static int x = 1000;
	int i = 0;
	while ( i < n ) {
		for ( j = 0; j < x; j++ ) {
			if ( A[i + j] == 0 ) {
				file << "1 ";
			} else {
				file << "0 ";
			}
		}
		i += x;
		file << "\n";
	}
	file.close();
	delete[] A;

	system("gnuplot -e \"set view map; splot 'primes.txt' matrix with image\"");    	

    return 0;

}
