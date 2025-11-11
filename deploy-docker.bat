@echo off
echo ========================================
echo Deploying Student Report Card System to Docker
echo ========================================
echo.

echo Checking Docker...
docker --version
if %errorlevel% neq 0 (
    echo ERROR: Docker is not running or not installed
    pause
    exit /b 1
)
echo.

echo Step 1: Removing old containers and images...
docker stop student-report-card-system 2>nul
docker rm student-report-card-system 2>nul
docker rmi student-report-card-system 2>nul
echo Done.
echo.

echo Step 2: Building Docker image (this may take a few minutes)...
docker build -t student-report-card-system .
if %errorlevel% neq 0 (
    echo ERROR: Failed to build Docker image
    pause
    exit /b 1
)
echo.
echo Image built successfully!
echo.

echo Step 3: Starting container...
docker run -d -p 5000:5000 --name student-report-card-system student-report-card-system
if %errorlevel% neq 0 (
    echo ERROR: Failed to start container
    echo.
    echo Checking logs...
    docker logs student-report-card-system
    pause
    exit /b 1
)
echo.
echo Container started!
echo.

echo Step 4: Waiting for container to initialize...
timeout /t 3 /nobreak >nul

echo.
echo ========================================
echo Deployment Status
echo ========================================
echo.
echo Container Status:
docker ps --filter "name=student-report-card-system" --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}"
echo.
echo Container Logs (last 10 lines):
docker logs --tail 10 student-report-card-system
echo.
echo ========================================
echo.
echo Your application should be available at:
echo http://localhost:5000
echo.
echo To view full logs: docker logs -f student-report-card-system
echo To stop: docker stop student-report-card-system
echo.
pause

