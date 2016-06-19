// #include <time.h>
#include <stdlib.h>
#include <unistd.h>
#include <ncurses.h>

#define DEF_UP 1
#define DEF_DOWN 2
#define DEF_RIGHT 3
#define DEF_LEFT 4

struct Shot {
    int col;
    int row;
    int next_index;
};

struct Shot shots[100];

int getDirection ();
int * movePoint (int, int);

int main ()
{
    int i = 150;
    int ch;
    int *p_coord;
    int row;
    int col;
    int player_x;
    int player_y;

    initscr();
    getmaxyx(stdscr, row, col);
    row = row / 2;
    col = col / 2;
    mvprintw(0, col, "pres cursor key");
    mvprintw(row, col, "@");
    noecho();

    do {
        //sleep(1);
        //usleep(1000);

        int * p_new_coord = movePoint(col, row);

        mvprintw(row, col, " ");
        col = p_new_coord[0];
        row = p_new_coord[1];
        mvprintw(0, 0, "r:%d c:%d  ", row, col);
        mvprintw(row, col, "@");

        refresh();

    } while (i--);
    //} while (ch != 27);

    getch();
    endwin();

    return 0;
}

int getDirection0 ()
{
    return rand() % 4;
}

int getCommand ()
{
    //if (getch() == )
    return 0;
}

int getDirection ()
{
    if (getch() != 27) {
        return 0;
    }
    if (getch() != 91) {
        return 0;
    }
    int ret_val;
    switch (getch()) {
        case 65:
            ret_val = DEF_UP;
            break;
        case 66:
            ret_val = DEF_DOWN;
            break;
        case 67:
            ret_val = DEF_RIGHT;
            break;
        case 68:
            ret_val = DEF_LEFT;
            break;
        default:
            ret_val = 0;
            break;
    }
    return ret_val;
}

int * movePoint (int x, int y)
{
    switch (getDirection()) {
        case DEF_UP:
            y--;
            break;
        case DEF_DOWN:
            y++;
            break;
        case DEF_LEFT:
            x--;
            break;
        case DEF_RIGHT:
            x++;
            break;
    }
    static int r[2];
    r[0] = x;
    r[1] = y;
    return r;
}
