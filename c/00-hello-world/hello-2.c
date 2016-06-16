// #include <time.h>
#include <stdlib.h>
#include <unistd.h>
#include <ncurses.h>

int getDirection ();
int * movePoint (int, int);

int main ()
{
    int i = 150;
    int ch;
    int *p_coord;
    int row;
    int col;

    initscr();
    getmaxyx(stdscr, row, col);
    // row = row / 2;
    // col = col / 2;
    printw("pres any key");

    row = col = 0;

    do {
        sleep(1);
        //usleep(1000);
        p_coord = movePoint(col, row);
        // col = p_coord[0];
        // row = p_coord[1];
        ch = getch();
        //sleep(1);
        mvprintw(row, col, "# i:%d r:%d c:%d ", i, row, col);
        printw("[key code: %d]", ch);
        refresh();
        col++;
        row++;

    } while (i--);
    //} while (ch != 27);

    getch();
    endwin();

    return 0;
}

int getDirection ()
{
    return rand() % 4;
}

int * movePoint (int x, int y)
{
    switch (getDirection()) {
        case 0:
            y--;
            break;
        case 1:
            y++;
            break;
        case 2:
            x--;
            break;
        case 3:
            x++;
            break;
    }
    static int r[2];
    r[0] = x;
    r[1] = y;
    return r;
}
