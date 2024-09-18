# An das Sktipt übergeneme Parameter
param([string]$fileToOpen)

# Pfad zu Notepad++
$notepadPlusPlusPath = "C:\Program Files\Notepad++\notepad++.exe"

# Starten von Notepad++ mit Datei die geöffnet werden soll
Start-Process -FilePath $notepadPlusPlusPath -ArgumentList $fileToOpen