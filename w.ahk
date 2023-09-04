; REMOVED: #NoEnv
SendMode("Input")
#MaxThreadsPerHotkey 2
$up::
{ ; V1toV2: Added bracket
while (getkeystate("up", "P")) {
		Send("{w down}")
        Sleep(5)
        Send("{w up}")
        Sleep(5)
}
} ; V1toV2: Added Bracket before hotkey or Hotstring

return
