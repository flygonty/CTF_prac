##### This challenge is from ntustisc bof2c

`Here is source code`
```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void y0u_c4n7_533_m3()
{
  int allow = 0;
  if (allow) {
    execve("/bin/sh", 0, 0);
  }
  else {
    puts("Oh no~~~!");
    exit(0);
  }
}

int main()
{
  char buf[16];
  puts("This is your second bof challenge ;)");
  fflush(stdout);
  read(0, buf, 0x30);
  if (strlen(buf) >= 16) {
    puts("Bye bye~~");
    exit(0);
  }
  return 0;
}

```

    Firstly, we need to bypass strlen function(func)
    This func could be bypass by \x00 first becasue strlen would check
    It's first byte if the first byte is \x00 
    Then the result of strlen woule be 0
    Once we success bypass strlen, we need to find the offset 
    And try to return to y0u_c4n7_533_m3()
    Use gdb-peda and pwntools to find the padding
    But I'm not familiar with pwntools QQ
    So, I use brute force to try to find offset
    
    Here's my procees
    1. python solve.py // while program would be stopped by raw_input()
    2. gdb ./bof2
    3. at // attach to solve.py
    4. set breakpoint at  b*0x0000000000400738
    5. press "c" button
    6. press 'enter' button
    7. We could see the stack and find the return address
