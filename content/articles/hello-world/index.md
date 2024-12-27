---
title: "Hello World"
date: 2024-12-24
draft: false
description: "This is a description."
tags: ["example", "tag"]
---

This example to get you started.

# This is a heading

# This a secondary heading

## This is a subheading

### This is a subsubheading

#### This is a subsubsubheading

This is a paragraph with **bold** and _italic_ text.
Check more at [Blowfish documentation](https://blowfish.page/)

```asm
# Write syscall using AARCH64 asm

.global _start
.section .text

_start:
        mov x8, #64        // syscall number for write
        mov x0, #1         // stdin/stdout/stderr fd index
        ldr x1, =str_hello // string address using label
        mov x2, #14        // string size
        svc 0              // make the syscall

        mov x8, #93        // syscall number for exit
        mov x0, #12        // exit code 12
        svc 0              // make the syscall

.section .data
        str_hello: .ascii "Hello, world!\n"

==
=>
```
