#include <stdlib.h>
#include <ncurses.h>

int main ()
{
    int ch;
    int row, col;
    initscr();

    do {
        getmaxyx(stdscr, row, col);
        printw("Hello, world! row: %d, col: %d\n", row, col);
        ch = getch();
        printw("[ %d ]", ch);
        refresh();

    } while (ch != 27);
    endwin();

    return 0;
}

int getDirection ()
{
    return rand();
}

