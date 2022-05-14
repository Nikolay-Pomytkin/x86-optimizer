        global _entry
        default rel
        section .text
        extern _peek_byte
        extern _read_byte
        extern _write_byte
        extern _raise_error
        global _entry
_entry:
        mov rbx, rdi
        lea rax, [rel _ret4780]
        push rax
        mov rax, 80
        push rax
        jmp _label_even?_cf135ea9e652962
_ret4780:
        cmp rax, 56
        je _if4778
        lea rax, [rel _ret4781]
        push rax
        mov rax, 1632
        push rax
        jmp _label_odd?_813193bd5bf69e1
_ret4781:
        jmp _if4779
_if4778:
        lea rax, [rel _ret4782]
        push rax
        mov rax, 1616
        push rax
        jmp _label_odd?_813193bd5bf69e1
_ret4782:
_if4779:
        ret
_label_even?_cf135ea9e652962:
        mov rax, [rsp + 0]
        mov r9, rax
        and r9, 15
        cmp r9, 0
        jne _raise_error_align
        cmp rax, 0
        mov rax, 24
        je _g4785
        mov rax, 56
_g4785:
        cmp rax, 56
        je _if4783
        mov rax, 24
        jmp _if4784
_if4783:
        lea rax, [rel _ret4786]
        push rax
        mov rax, [rsp + 8]
        mov r9, rax
        and r9, 15
        cmp r9, 0
        jne _raise_error_align
        sub rax, 16
        push rax
        jmp _label_odd?_813193bd5bf69e1
_ret4786:
_if4784:
        add rsp, 8
        ret
_label_odd?_813193bd5bf69e1:
        mov rax, [rsp + 0]
        mov r9, rax
        and r9, 15
        cmp r9, 0
        jne _raise_error_align
        cmp rax, 0
        mov rax, 24
        je _g4789
        mov rax, 56
_g4789:
        cmp rax, 56
        je _if4787
        mov rax, 56
        jmp _if4788
_if4787:
        lea rax, [rel _ret4790]
        push rax
        mov rax, [rsp + 8]
        mov r9, rax
        and r9, 15
        cmp r9, 0
        jne _raise_error_align
        sub rax, 16
        push rax
        jmp _label_even?_cf135ea9e652962
_ret4790:
_if4788:
        add rsp, 8
        ret
_raise_error_align:
        mov r15, rsp
        and r15, 8
        sub rsp, r15
        call _raise_error