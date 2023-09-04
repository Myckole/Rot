; REMOVED: #NoEnv
SendMode("Input")
#MaxThreadsPerHotkey 2
$up::
{ ; V1toV2: Added bracket
while (getkeystate("up", "P")) {
		Send("{w down}")
        Sleep(40)
        Send("{w up}")
        Sleep(40)
}
} ; V1toV2: Added Bracket before hotkey or Hotstring

return
