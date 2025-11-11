@echo off
cls
echo ========================================
echo QUICK DEPLOY TO DOCKER DESKTOP
echo ========================================
echo.

REM Stop and remove existing container
echo [1/4] Cleaning up old containers...
docker stop student-report-card-system 2>nul
docker rm student-report-card-system 2>nul
echo Done.
echo.

REM Build the image
echo [2/4] Building Docker image...
docker build -t student-report-card-system .
if %errorlevel% neq 0 (
    echo.
    echo ERROR: Build failed!
    pause
    exit /b 1
)
echo Done.
echo.

REM Run the container
echo [3/4] Starting container...
docker run -d -p 5000:5000 --name student-report-card-system student-report-card-system
if %errorlevel% neq 0 (
    echo.
    echo ERROR: Failed to start container!
    echo Checking logs...
    docker logs student-report-card-system
    pause
    exit /b 1
)
echo Done.
echo.

REM Wait a moment
echo [4/4] Waiting for application to start...
timeout /t 5 /nobreak >nul

REM Show status
echo.
echo ========================================
echo DEPLOYMENT COMPLETE!
echo ========================================
echo.
docker ps --filter "name=student-report-card-system"
echo.
echo Application URL: http://localhost:5000
echo.
echo To view logs: docker logs -f student-report-card-system
echo To stop: docker stop student-report-card-system
echo.
pause

