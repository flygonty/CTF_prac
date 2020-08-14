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
    it's first byte if the first byte is \x00 then the result of strlen woule be 0
    
    Once we success bypass strlen, we need to find the offset and try to return to          y0u_c4n7_533_m3()
   
