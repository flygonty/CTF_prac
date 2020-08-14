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
    7. We could see the stack and find the place which program jump
    8. paste the address to the payload then it could work
    
    `Hint: use objdump -d -M intel bof2 to find the address you want to jump`
    
```
0000000000400697 <y0u_c4n7_533_m3>:
  400697:       55                      push   rbp
  400698:       48 89 e5                mov    rbp,rsp
  40069b:       48 83 ec 10             sub    rsp,0x10
  40069f:       c7 45 fc 00 00 00 00    mov    DWORD PTR [rbp-0x4],0x0
  4006a6:       83 7d fc 00             cmp    DWORD PTR [rbp-0x4],0x0
  4006aa:       74 18                   je     4006c4 <y0u_c4n7_533_m3+0x2d>
  4006ac:       ba 00 00 00 00          mov    edx,0x0
  4006b1:       be 00 00 00 00          mov    esi,0x0
  4006b6:       48 8d 3d 1b 01 00 00    lea    rdi,[rip+0x11b]        # 4007d8 <_IO_stdin_used+0x8>
  4006bd:       e8 be fe ff ff          call   400580 <execve@plt>
  4006c2:       eb 16                   jmp    4006da <y0u_c4n7_533_m3+0x43>
  4006c4:       48 8d 3d 15 01 00 00    lea    rdi,[rip+0x115]        # 4007e0 <_IO_stdin_used+0x10>
  4006cb:       e8 80 fe ff ff          call   400550 <puts@plt>
  4006d0:       bf 00 00 00 00          mov    edi,0x0
  4006d5:       e8 c6 fe ff ff          call   4005a0 <exit@plt>
  4006da:       c9                      leave
  4006db:       c3                      ret

```

    Because x86-64 calling convention, when program call execve this syscall
    It would use rdi, rsi and rdx. In 4006ac the program has loaded /bin/sh
    and need to get rsi and rdx so the next instruction edx,0x0 is the perfect
    address we want to jump.
