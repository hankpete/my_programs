//an example of using classes
#include <iostream>
using namespace std;

class Calculator {
	private:
		double answer;
		double a; double b;
	public:
		void get_a_b() 
		{
			cout << "a: "; cin >> a;
			cout << "b: "; cin >> b;
		}
		void get_operation() 
		{
			int choice;
			cout << "Would you like to: \n\t1)Add \n\t2)Subtract \n\t3)Multiply \n\t4)Divide\nChoice: ";
			cin >> choice;
			switch (choice)
			{
				case 1:
					add(a, b);
					break;
				case 2:
					subtract(a, b);
					break;
				case 3:
					multiply(a, b);
					break;
				case 4:
					divide(a, b);
					break;
				default:
					cout << "Invalid input.\n";
			}

		}
		void add(double x, double y) 
		{ 
			answer = x + y;
			cout << "a + b = " << answer << "\n"; 
		}
		void subtract(double x, double y) 
		{ 
			answer = x - y;
			cout << "a - b = " << answer << "\n"; 
		}
		void multiply(double x, double y) 
		{ 
			answer = x * y;
			cout << "a * b = " << answer << "\n"; 
		}
		void divide(double x, double y) 
		{ 
			answer = x / y;
			cout << "a / b = " << answer << "\n"; 
		}
		double get_answer() { return answer; }
};

int main()
{
	Calculator calc;

	char response = 'y';
	char new_a_b;
	while (response == 'y')
	{
		cout << "Define a and b (y or n)? ";
		cin >> new_a_b;
		if (new_a_b == 'y') 
		{
			calc.get_a_b();
		}
		calc.get_operation();
		
		cout << "Again (y or n)? ";
		cin >> response;
	}

	return 0;
}
