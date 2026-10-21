import sys, os

if len(sys.argv) == 2: cisco_pt_path = sys.argv[1]
elif len(sys.argv) > 2: 
    print('usage: python cisco_pt_patch.py <path_to_cisco_pt_executable_file>   #this is not the shortcut path')
    exit()
else: cisco_pt_path = './PacketTracer.exe'

if(not cisco_pt_path):
    print("You didn't pass the absolute path for Cisco PT. Therefore I will consider you are using the current directory\n")

if (not os.path.exists(cisco_pt_path)):
    print("some warning, you did not pass the correct absolute path for Cisco PT.\nAnd you didn't even put this script in the directory of Cisco PT. Therefore I will consider the default installation path of Cisco PT which is in: ", end=None)
    print(r"C:\Program Files\Cisco Packet Tracer 8.2.2\bin\PacketTracer.exe", '\n')

    cisco_pt_path = r"C:\Program Files\Cisco Packet Tracer 8.2.2\bin\PacketTracer.exe"

offset = b"\xE3\xBD\xF6\x02" # 02F6BDE3 (the address of the target JNZ which i will patch converting it to JZ)

old_instructions = b"\x0F\x85\x18\x06\x00\x00" #(JNZ dword $0000061E) will change 85 to 84
new_instructions = b"\x0F\x84\x18\x06\x00\x00" #(JZ dword $0000061E)

try:
    f = open (cisco_pt_path, 'rb')
    f.seek(int.from_bytes(offset, byteorder='little'), 0)
    binary_content = f.read(6)
    f.close()
    
except:
    print("Couldn't open Cisco PT binary file, perhaps you want to run this script as administrator, or perhaps you want to close Cisco PT if it is already open\n")
    f.close()
    exit()

if (binary_content == old_instructions):
    print('Checks OK, patching now\n')
    try:
        f = open (cisco_pt_path, 'r+b')
        f.seek(int.from_bytes(offset, byteorder='little'), 0)
        f.write(new_instructions)
        f.close()
    except:
        print("couldn't overwrite bytes bcs cisco PT is in a privileged folder, please run this script as administrator\n")
        f.close()
        exit()

    print('Patching OK, Final checking\n')

    try:
        f = open (cisco_pt_path, 'r+b')
        f.seek(int.from_bytes(offset, byteorder='little'), 0)
        binary_content = f.read(6)
        if(binary_content == new_instructions):
            print('Cisco PT is now patched, feel free to open it while leaving internet connection open. Just close the login screen and continue your work.\n')
        else:
            print("Smth wrong, please run this script as administrator")
        f.close()
    except:
        print("Smth wrong, please run this script as administrator")
        f.close()
        exit()

elif (binary_content == new_instructions):
    print('Already patched :D')

else:
    print("Some error that I don't know, maybe you are running on a MAC, or running on a 32-bit system (either way, please throw your computer)")
    exit()