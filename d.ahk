; REMOVED: #NoEnv
SendMode("Input")
#MaxThreadsPerHotkey 2
$Right::
{ ; V1toV2: Added bracket
while (getkeystate("Right", "P")) {
		Send("{d down}")
        Sleep(5)
        Send("{d up}")
        Sleep(5)
}
} ; V1toV2: Added Bracket before hotkey or Hotstring

return
