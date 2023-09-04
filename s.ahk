; REMOVED: #NoEnv
SendMode("Input")
#MaxThreadsPerHotkey 2
$down::
{ ; V1toV2: Added bracket
while (getkeystate("down", "P")) {
		Send("{s down}")
        Sleep(40)
        Send("{s up}")
        Sleep(40)
}
} ; V1toV2: Added Bracket before hotkey or Hotstring

return
