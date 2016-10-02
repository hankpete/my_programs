//a program to decode secret messages with Gabe

#include <iostream>
#include <string>
using namespace std;

string decode(string msg, int shift) {
		//binarize
		for (int i = 0; i<msg.length(); i++) {
				if (msg[i] == '|') {
						msg[i] = '1';
				} else if (msg[i] == '_') {
						msg[i] = '0';
				}
		}

		//decimalize
		int nums[200];
		int size = 0;
		string num = "";

		for (int i = 0; i<msg.length(); i++) {
			if (msg[i] == '-' || msg[i] == '!' || msg[i] == '.' || msg[i] == ' ' || msg[i] == ',') {
				if (num != "") {
					nums[size] = stoi(num);
					size++;
					if (msg[i] != '-') {
						nums[size] = -1;
						size++;
					}
					num = "";
				}
			} else {
				num += msg[i];
			}
		}	

		string bin_str;
		for (int i = 0; i<size; i++) {
				if (nums[i] == -1) {
						continue;
				}
				bin_str = to_string(nums[i]);
				nums[i] = stoi(bin_str,nullptr,2);
		}

		//alphabetize
		string alpha = "abcdefghijklmnopqrstuvwxyz";
		char letters[200];
		for (int i = 0; i<size; i++) {
			if (nums[i] == -1) {
					letters[i] = ' ';
					continue;
			}
			int index = nums[i]-shift;
			if (index < 0) {
					index += 26;
			}
			letters[i] = alpha[ index ];
		}	

		return letters;
}

int main() {
		
		//cout << "Enter Gabe's message here: ";

		//string code;
		//getline(cin,code);

		string code = "|__|_-||_-||__|-|__-||___-|___|, ||_-||-|__-|____-|_|||! ||| |_-||__|-|____-|| |___|-||__|-|_||| |__|_-||_-||__|-|__|_ |-|_||| ||_|_-|||-|____-|__|_-||_-|_-||__|-|_||| |_|_|-||__|-|___| |||-|__-|_-||-||-|_ |___|-|_|_|-||-|_|_-|_|_, ||__|-|__-|_ |_-||-||_|-|__||-|_-|||-|__-|_| |_|||-|__||-||__-|____ |___|-||-||_|-|____-||-|__|_ |-||-|___|-|___|-||__|-|_|-|| |_|_|-||__|-|___| ||__|-|__ ||-|__-||_|-||_-||__|-|__-|__|_-|||-|__-|_| ||-|_||-||||-||-|____-|||-||-|__-||_|-||.";

		string msg;
		for (int i = 0; i<26; i++){
			msg = decode(code,i);
			cout << "Gabe's message was: " + msg + "\n";
		}
		

		return 0;
}
