Cisco Packet Tracer login screen bypass

This script simply patches Cisco Packet Tracer executable to bypass the mandatory login requirement.
This way, you do not have to login to Cisco network, nor turn off your network connection in order to use Cisco PT.

Run with:
`python cisco_pt_patch.py <path_to_ciscopt_executable>`

If you ran cisco_pt_patch.py without arguments, the script will assume that ciscoPT.exe is in the current directory, if not found, will assume the default installation path.


Here's a simple demo:
https://github.com/user-attachments/assets/5386598c-6678-4deb-8ac5-093cf200e772


This script supports only Windows 64 version.
I may support MacOS in the future, but I hate mac.


## Technical Details
### How this script works
It is a simple jnz <-> jz swap in the binary.
1- Traced down the basic block that displays the QMessageBox (critical message box) and terminates the process.
2- Got the address of the previous conditional jump (JNZ addr)
<img width="707" height="392" alt="image" src="https://github.com/user-attachments/assets/f219def8-a812-4e42-b18b-d762329134ef" />

3- Simply swapped the JNZ to a JZ in x64dbg or HxD
<img width="313" height="87" alt="image" src="https://github.com/user-attachments/assets/d365ce33-e12d-4417-b486-c4a77ea9ac73" />

<img width="282" height="66" alt="image" src="https://github.com/user-attachments/assets/5f10754d-d429-48a8-9586-a0ddeb3b74e5" />

4- Hardcoded this process in a python script

### Warning
Cisco Packet tracer utilizes some anti-debugging procedures, but their attempts for anti-debugging is so bad:
<img width="677" height="512" alt="image" src="https://github.com/user-attachments/assets/d8f7a597-d0ca-4049-a530-b5825e5f2191" />

