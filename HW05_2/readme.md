### 作業五

C程式碼使用老師作業中的 mul3test.c。
1、用 gcc 產生組合語言.s (參數 -S)
```
 gcc -S mul3test.c -o mul3test.s
```
2、用 gcc 編譯為目的檔.o (參數 -c)
```
 gcc mul3test.c -c
```
3、用 objdump 將目的檔進行反組譯 (參數 -d)
```
 objdump -d mul3test.o
```
```
mul3test.o:     file format elf64-x86-64


Disassembly of section .text:

0000000000000000 <mul3>:
   0:   f3 0f 1e fa             endbr64
   4:   55                      push   %rbp
   5:   48 89 e5                mov    %rsp,%rbp
   8:   89 7d fc                mov    %edi,-0x4(%rbp)
   b:   89 75 f8                mov    %esi,-0x8(%rbp)
   e:   89 55 f4                mov    %edx,-0xc(%rbp)
  11:   8b 45 fc                mov    -0x4(%rbp),%eax
  14:   0f af 45 f8             imul   -0x8(%rbp),%eax
  18:   0f af 45 f4             imul   -0xc(%rbp),%eax
  1c:   5d                      pop    %rbp
  1d:   c3                      ret

000000000000001e <main>:
  1e:   f3 0f 1e fa             endbr64
  22:   55                      push   %rbp
  23:   48 89 e5                mov    %rsp,%rbp
  26:   ba 05 00 00 00          mov    $0x5,%edx
  2b:   be 02 00 00 00          mov    $0x2,%esi
  30:   bf 03 00 00 00          mov    $0x3,%edi
  35:   e8 00 00 00 00          call   3a <main+0x1c>
  3a:   89 c6                   mov    %eax,%esi
  3c:   48 8d 05 00 00 00 00    lea    0x0(%rip),%rax        # 43 <main+0x25>
  43:   48 89 c7                mov    %rax,%rdi
  46:   b8 00 00 00 00          mov    $0x0,%eax
  4b:   e8 00 00 00 00          call   50 <main+0x32>
  50:   b8 00 00 00 00          mov    $0x0,%eax
  55:   5d                      pop    %rbp
  56:   c3                      ret
```
4、用 objdump 將該目的檔的表頭印出來 (參數 -h)
```
 objdump -h mul3test.o
```
```
mul3test.o:     file format elf64-x86-64

Sections:
Idx Name          Size      VMA               LMA               File off  Algn
  0 .text         00000057  0000000000000000  0000000000000000  00000040  2**0
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
  1 .data         00000000  0000000000000000  0000000000000000  00000097  2**0
                  CONTENTS, ALLOC, LOAD, DATA
  2 .bss          00000000  0000000000000000  0000000000000000  00000097  2**0
                  ALLOC
  3 .rodata       00000010  0000000000000000  0000000000000000  00000097  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  4 .comment      0000002c  0000000000000000  0000000000000000  000000a7  2**0
                  CONTENTS, READONLY
  5 .note.GNU-stack 00000000  0000000000000000  0000000000000000  000000d3  2**0
                  CONTENTS, READONLY
  6 .note.gnu.property 00000020  0000000000000000  0000000000000000  000000d8  2**3
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  7 .eh_frame     00000058  0000000000000000  0000000000000000  000000f8  2**3
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, DATA
```
有參考 林彥廷 的readme