#include <ncurses.h>

int main ()
{
    int ch;
    initscr();
    printw("Hello, world");
    refresh();
    ch = getch();
    printf("[ %d ]", ch);
    endwin();

    return 0;
}

