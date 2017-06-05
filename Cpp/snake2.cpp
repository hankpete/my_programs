//The classic game of snake, terminal style
#include <iostream>
#include <string>
#include <ncurses.h>
using namespace std;

class Board {
    private:
        int n = 10;     //n x n board
        int tail = 0;   //length of tail
        int mx = rand() % n;     //mouse x
        int my = rand() % n;     //mouse y
        char dir = 'w'; //direction of snake movement (WASD)
        int sx[100] = {-1};    //snake segments coords
        int sy[100] = {-1};
        int dt = 300;
    public:
        int cont = 1;   //continue game
        Board() {
            //start curses mode
            initscr();
            cbreak();   //no need to press enter
            noecho();   //don't show keys typed
            //start head of snake somewhere
            sx[0] = rand() % n;
            if (sx[0] == mx) {
                sy[0] = (my + 1) % n;
            } else {
                sy[0] = rand() % n;
            }
        }
        int is_snake(int x, int y) {
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
            string line;
            for (int y = 0; y < n; y++) {
                line = "";
                for (int x = 0; x < n; x++) {
                    if (x == mx && y == my) {
                        line += "x";
                    } else if (is_snake(x,y)) {
                        if (x == sx[0] && y == sy[0]) {
                            line += "O";
                        } else{
                            line += "o";
                        }
                    } else {
                        line += ".";
                    }
                    //add some space to make it a square board
                    line += " ";
                }
                line += "\n";
                printw(line.c_str() );
            }
            //print it to the real screen
            refresh();
        }
        void ask_dir() {
            timeout(dt);  //it moves!
            char new_dir = getch();
            if (new_dir == 'w' || new_dir == 'a' || new_dir == 's' || new_dir == 'd') {
                dir = new_dir;
            }
        }
        void move() {
            int dx,dy;
            if (dir == 'w') {
                dx = 0; dy = -1;
            } else if (dir == 'd') {
                dx = 1; dy = 0;
            } else if (dir == 's') {
                dx = 0; dy = 1;
            } else {
                dx = -1; dy = 0;
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
            if (sx[0] >= n || sx[0] < 0 || sy[0] >= n || sy[0] < 0) {
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
                    win_game();
                } else {
                    int r = rand() % (n*n - tail - 1);  //a number between 0 and the spaces left
                    int count = 0;
                    mx = -1 ; my = 0;
                    while (count <= r) {
                        if (mx < n - 1) {
                            mx++;
                        } else {
                            mx = 0;
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
            printw("\nGAME OVER\n");
            refresh();
            timeout(-1);  //indef
            getch();
            //end curses mode 
            endwin();	
            cont = 0;
        }
        void win_game() {
            printw("\nYOU WIN\n");
            refresh();
            timeout(-1); //indef
            getch();
            //end curses mode 
            endwin();	
            cont = 0;
        }
};

int main() {
    
    
    Board brd;
    while (brd.cont == 1) {
        brd.show(); 
        brd.ask_dir();
        brd.move();
    }
   
    return 0;
}
                    
