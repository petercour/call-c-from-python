from ctypes import *

libc = cdll.LoadLibrary("/lib/x86_64-linux-gnu/libc.so.6")
printf = libc.printf
printf(b"hello world\n")


