@echo off
echo ========================================
echo Deploying to Docker Desktop...
echo ========================================
echo.

echo Step 1: Stopping and removing old container (if exists)...
docker stop student-report-card-system 2>nul
docker rm student-report-card-system 2>nul
echo Done.
echo.

echo Step 2: Building Docker image...
docker build -t student-report-card-system .
if %errorlevel% neq 0 (
    echo ERROR: Failed to build Docker image
    pause
    exit /b 1
)
echo Done.
echo.

echo Step 3: Starting container...
docker run -d -p 5000:5000 --name student-report-card-system student-report-card-system
if %errorlevel% neq 0 (
    echo ERROR: Failed to start container
    pause
    exit /b 1
)
echo Done.
echo.

echo ========================================
echo Deployment Complete!
echo ========================================
echo.
echo Your application is running at:
echo http://localhost:5000
echo.
echo Container Status:
docker ps | findstr student-report-card
echo.
echo To view logs: docker logs student-report-card-system
echo To stop: docker stop student-report-card-system
echo.
pause

