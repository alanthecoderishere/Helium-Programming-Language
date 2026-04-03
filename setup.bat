@echo off
REM Helium (.ium) Setup Instructions for Windows

set "PROJECT_DIR=%cd%"
set "LAUNCHER_PATH=%PROJECT_DIR%\ium.bat"

echo ========================================================
echo Helium (.ium) Setup for Windows
echo ========================================================
echo.
echo To run Helium globally, you can add this folder to your PATH:
echo.
echo 1. Open 'Edit the system environment variables' from Start.
echo 2. Click 'Environment Variables...'.
echo 3. Under 'System variables', find 'Path' and click 'Edit...'.
echo 4. Click 'New' and paste this path:
echo    %PROJECT_DIR%
echo 5. Click OK on all windows.
echo.
echo After restarting your CMD/PowerShell, you can run:
echo ium <filename>.ium
echo.
echo ========================================================
pause
