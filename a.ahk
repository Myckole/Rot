; REMOVED: #NoEnv
SendMode("Input")
#MaxThreadsPerHotkey 2
$left::
{ ; V1toV2: Added bracket
while (getkeystate("left", "P")) {
		Send("{a down}")
        Sleep(5)
        Send("{a up}")
        Sleep(5)
}
} ; V1toV2: Added Bracket before hotkey or Hotstring

return
