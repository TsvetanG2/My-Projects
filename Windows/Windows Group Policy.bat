Open any folder in C:/Users/Downloads for example.
Create a text file and put:

@echo off
pushd "%~dp0"

dir /b %SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientExtensions-Package3*.mum >List.txt
dir /b %SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientTools-Package3*.mum >>List.txt

for /f %%i in ('findstr /i . List.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages%%i"
pause

Save it as gpedit.bat / choose All Files
Close it,
Run it as administrator and wait until the processes are done.

Congratulations, you have the Windows Group Policy on your device

