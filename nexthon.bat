@echo off
setlocal

set "PROJECT_DIR=%~dp0"
set "PYTHONPATH=%PROJECT_DIR%src;%PYTHONPATH%"

py -m nexthon.interpreter %*

endlocal
