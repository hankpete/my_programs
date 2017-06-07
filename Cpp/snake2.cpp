//The classic game of snake, terminal style
#include <ncurses.h>
#include <string>
#include <unistd.h>  //sleep
#include <time.h>
#include <fstream>
using namespace std;

class Board {
    private:
        static const int n = 20;     //n x n board
                        //using 0 and n-1 as walls
        int tail = 0;   //length of tail
        int mx = rand() % (n-2) + 1;     //mouse x
        int my = rand() % (n-2) + 1;     //mouse y
        char dir = 'p'; //direction of snake movement (paused)
        int sx[(n-2)*(n-2)] = {-1};    //snake segments coords
        int sy[(n-2)*(n-2)] = {-1};
        char speed;
        int start = 1;  //has the game just started
    public:
        int cont = 1;   //continue game
        Board() {
            //start curses mode
            initscr();
            //use colors
            start_color();
            init_pair(1, COLOR_GREEN, COLOR_BLACK); //snake
            init_pair(2, COLOR_RED, COLOR_BLACK); //mouse
            //input
            cbreak();   //no need to press enter
            noecho();   //don't show keys typed
            keypad(stdscr, TRUE);  //special keys

            //start head of snake somewhere
            sx[0] = rand() % (n-2) + 1;
            if (sx[0] == mx) {
                sy[0] = (my + 1) % (n-2) + 1;
            } else {
                sy[0] = rand() % (n-2) + 1;
            }

            get_speed();
        }
        void get_speed() {
            clear();
            echo();
            printw("\nWELCOME TO SNEK GAME\n");
            printw("\nHow fast?");
            printw("\n    1 - snail\n    2 - snek\n    3 - heckin fast snek\nEnter Choice: ");
            char c = getch();
            while (c != '1' && c != '2' && c != '3') {
                c = getch();
            }
            getch();
            speed = c;
            noecho();
        }
        int is_snake(int x, int y) {
            //quick utility for checking if a square has tail
            for (int i = 0; i < tail + 1; i++) {
                if (sx[i] == x && sy[i] == y) {
                    return 1;
                }
            }
            return 0;
        }
        void show() {
            clear();    //remove old board
            //loop through x and y. (0,0) is top left
            string text = "SCORE: " + to_string(tail) + "\n\n"; 
            printw( text.c_str() );
            for (int y = 0; y < n; y++) {
                for (int x = 0; x < n; x++) {
                    if (x == mx && y == my) {
                        attron(COLOR_PAIR(2));
                        printw("x");
                        attroff(COLOR_PAIR(2));
                    } else if (is_snake(x,y)) {
                        attron(COLOR_PAIR(1));
                        if (x == sx[0] && y == sy[0]) {
                            printw("x");
                        } else{
                            printw("x");
                        }
                        attroff(COLOR_PAIR(1));
                    } else if (x == 0 || x == n - 1 || y == 0 || y == n - 1) {
                        printw("X");
                    } else {
                        printw(" ");
                    }
                    //add some space to make it a square board
                    printw(" ");
                }
                printw("\n");
                curs_set(0); // hide cursor
            }
            //instructions
            if (start == 1) {
                printw("\nUse arrow keys to move.");
            }
        }
        void ask_dir() {
            int dt;
            if (speed == '1') {
                dt = 200;
            } else if (speed == '2') {
                dt = 150;
            } else if (speed == '3') {
                dt = 50;
            }
            timeout(dt);  //it moves!
            int new_dir = getch();
            if (new_dir == KEY_UP && dir != 's') {
                dir = 'n';
                start = 0;
            } else if (new_dir == KEY_DOWN && dir != 'n') {
                dir = 's';
                start = 0;
            } else if (new_dir == KEY_LEFT && dir != 'e') {
                dir = 'w';
                start = 0;
            } else if (new_dir == KEY_RIGHT && dir != 'w') {
                dir = 'e';
                start = 0;
            }
        }
        void move() {
            int dx,dy;
            if (dir == 'n') {
                dx = 0; dy = -1;
            } else if (dir == 'w') {
                dx = -1; dy = 0;
            } else if (dir == 's') {
                dx = 0; dy = 1;
            } else if (dir == 'e') {
                dx = 1; dy = 0;
            } else {
                //paused at beginning
                return;
            }
            //change all but head of snake to one ahead
            for (int i = tail + 1; i > 0; i--) {
                sx[i] = sx[i - 1]; 
                sy[i] = sy[i - 1]; 
            }
            //move head
            sx[0] += dx;
            sy[0] += dy;
            //end if on wall or self
            if (sx[0] >= n-1 || sx[0] <= 0 || sy[0] >= n-1 || sy[0] <= 0) {
               end_game();
            } 
            for (int i = 1; i < tail + 1; i++) {
                if (sx[0] == sx[i] && sy[0] == sy[i]) {
                    end_game();
                }
            }
            //add to tail if on mouse, make new mouse out of what's left
            if (sx[0] == mx && sy[0] == my) {
                tail++;
                if (tail + 1 == n * n) {
                    end_game();
                } else {
                    int r = rand() % ((n-2)*(n-2) - tail - 1);  //a number between 0 and the spaces left
                    int count = 0;
                    mx = 0; my = 1;
                    while (count <= r) {
                        if (mx < n - 2) {
                            mx++;
                        } else {
                            mx = 1;
                            my++;
                        }    
                        if (! is_snake(mx,my)) {
                            count++;
                        }
                    }
                }
            }
        }
        void end_game() {
            attron(COLOR_PAIR(2));
            printw("\nGAME OVER");
            attroff(COLOR_PAIR(2));
            cont = 0; //end game
            high_score();
        }
        void high_score() {
            timeout(-1);  //indef

            echo();
            printw("\n\nSave Score");
            printw("\nName: ");
            char name[80];
            getstr(name);

            clear();

            ifstream file;
            file.open("snake_scores.dat");
            string line, newfile;
            while (getline(file, line)) {
                newfile += line + "\n";
                if (line.substr(0, 5) == "Speed" && line[6] == speed) {
                    int recorded = 0;
                    while (recorded < 3) {
                        getline(file, line);
                        //get what the score was
                        int i = 0;
                        string s;
                        while (line[i] != ' ') {
                            i++;
                        }
                        i++;
                        while (isdigit(line[i])) {
                            s += line[i];
                            i++;
                        }
                        //add if new score is higher
                        if (tail > stoi(s)) {
                            newfile += string(name) + " ";
                            newfile += to_string(tail);
                            newfile += "\n";
                            recorded++;
                            break;
                        } else {
                            newfile += line + "\n";
                            recorded++;
                        }
                    }
                }
            }
            file.close();
            ofstream file2;
            file2.open("snake_scores.dat");
            file2 << newfile;
            file2.close();

            clear();
            printw(newfile.c_str());
            getch();

            endwin();  //end ncurses session
        }
};

int main() {
    srand( time(NULL) );
    
    Board brd;
    while (brd.cont == 1) {
        brd.show(); 
        brd.ask_dir();
        brd.move();
    }
    
   
    return 0;
}
                    
