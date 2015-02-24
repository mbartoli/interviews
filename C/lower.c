/* Maps a given single character to lower case for the ASCII character set. */

#include <stdio.h>

int lower(int c);

main() {
  char in = getchar();
  int out = lower(in);
  printf("%d \n", out);
}

int lower(int c) {
  if (c >= 'A' && c <= 'Z')
    return c + 'a' - 'A';
  else
    return c;
}
