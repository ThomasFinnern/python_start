@ECHO OFF
REM <What it does>

CLS

Set CmdArgs=
ECHO python _emptyClass.py 

REM 
Call :AddNextArg -p "\pr004\entwickl\Schleif.nt"
                     
REM 
Call :AddNextArg -n "modules"
 
REM add command line 
REM Call :AddNextArg %*

ECHO.
ECHO ------------------------------------------------------------------------------
ECHO Start cmd:
ECHO.
ECHO python _emptyClass.py %CmdArgs% %* 
     python _emptyClass.py %CmdArgs% %* 

GOTO :EOF

REM ------------------------------------------
REM Adds given argument to the already known command arguments
:AddNextArg 
	Set NextArg=%*
	Set CmdArgs=%CmdArgs% %NextArg%
	ECHO  '%NextArg%'
GOTO :EOF
