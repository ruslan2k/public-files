/**
 * The game
 */

#include <stdlib.h>
#include <unistd.h>
#include <ncurses.h>

#define DEF_UP 1
#define DEF_DOWN 2
#define DEF_RIGHT 3
#define DEF_LEFT 4
#define DEF_SPACE 32
#define MAX_SHOTS 10

struct Shot {
    int col;
    int row;
    int next_index;
};

struct Shot shots[MAX_SHOTS];
int shots_count = 0;

int getDirection ();
int * movePoint (int, int);

int addShot (int shots_count, struct Shot shots[])
{
    printw("shots_count:%d\n", shots_count);
    if (shots_count == 0) {
        shots[0].col = shots_count;
        shots[0].row = 1000 + shots_count;
    } else {
        shots[shots_count].col = shots_count;
        shots[shots_count].row = 1000 + shots_count;
    }
    return ++ shots_count;
}

void printShots (int shots_count, struct Shot shots[])
{
    for (int i = 0; i < shots_count; i++) {
        printw("col:%d row:%d next:%d ", shots[i].col, shots[i].row, shots[i].next_index);
    }
    printw("\n");
}

int main ()
{
    int i = 150;
    int ch;
    int* p_coord;
    int row;
    int col;
    int player_x;
    int player_y;

    initscr();
    getmaxyx(stdscr, row, col);
    // row = row / 2;
    // col = col / 2;
    col = row = 0;
    mvprintw(0, col, "pres cursor key");
    mvprintw(row, col, "@");
    noecho();

    do {
        int ch = getch();

        shots_count = addShot(shots_count, shots);
        printShots(shots_count, shots);

        // int * p_new_coord = movePoint(col, row);

        // mvprintw(row, col, " ");
        // col = p_new_coord[0];
        // row = p_new_coord[1];
        // mvprintw(0, 0, "r:%d c:%d  ", row, col);
        // mvprintw(row, col, "@");

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
    if (getch() == DEF_SPACE) {
        return DEF_SPACE;
    }
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
