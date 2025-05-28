        .globl  mul3
        
        .text
mul3:
        mov     %rdi, %rax      # 將rdi放到rax裡
        imulq   %rsi, %rax      # 讓rsi乘rax回傳
        imulq   %rdx, %rax      # 讓rdx乘rax回傳
        ret     # 最後就會回傳a*b*c
