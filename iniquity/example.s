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
        mov rax, 16
        push rax
        mov rax, 32
        push rax
        mov rax, [rsp + 8]
        push rax
        mov rax, [rsp + 8]
        pop r8
        mov r9, r8
        and r9, 15
        cmp r9, 0
        jne _raise_error_align
        mov r9, rax
        and r9, 15
        cmp r9, 0
        jne _raise_error_align
        add rax, r8
        push rax
        lea rax, [rel _ret4778]
        push rax
        mov rax, [rsp + 8]
        push rax
        jmp _label_double_6334fa372629b92
_ret4778:
        add rsp, 24
        ret
_label_double_6334fa372629b92:
        mov rax, [rsp + 0]
        push rax
        mov rax, [rsp + 8]
        pop r8
        mov r9, r8
        and r9, 15
        cmp r9, 0
        jne _raise_error_align
        mov r9, rax
        and r9, 15
        cmp r9, 0
        jne _raise_error_align
        add rax, r8
        add rsp, 8
        ret
_raise_error_align:
        mov r15, rsp
        and r15, 8
        sub rsp, r15
        call _raise_error