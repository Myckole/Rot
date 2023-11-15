; REMOVED: #NoEnv
SendMode("Input")
#MaxThreadsPerHotkey 2
$down::
{ ; V1toV2: Added bracket
while (getkeystate("down", "P")) {
		Send("{s down}")
        Sleep(5)
        Send("{s up}")
        Sleep(5)
}
} ; V1toV2: Added Bracket before hotkey or Hotstring

return
