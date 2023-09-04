; REMOVED: #NoEnv
SendMode("Input")
#MaxThreadsPerHotkey 2
$left::
{ ; V1toV2: Added bracket
while (getkeystate("left", "P")) {
		Send("{a down}")
        Sleep(40)
        Send("{a up}")
        Sleep(40)
}
} ; V1toV2: Added Bracket before hotkey or Hotstring
+`::ExitApp()
return