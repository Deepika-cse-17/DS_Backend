@echo off
echo ========================================
echo Student Report Card System - Docker Deployment
echo ========================================
echo.

echo Checking Docker installation...
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Docker is not installed or not in PATH
    echo Please install Docker Desktop from https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)

echo Docker is installed!
echo.

echo Building Docker image...
docker build -t student-report-card-system .

if %errorlevel% neq 0 (
    echo ERROR: Failed to build Docker image
    pause
    exit /b 1
)

echo.
echo Image built successfully!
echo.

echo Starting container...
docker run -d -p 5000:5000 --name student-report-card-system student-report-card-system

if %errorlevel% neq 0 (
    echo Container might already be running. Stopping and removing old container...
    docker stop student-report-card-system >nul 2>&1
    docker rm student-report-card-system >nul 2>&1
    echo Starting new container...
    docker run -d -p 5000:5000 --name student-report-card-system student-report-card-system
)

echo.
echo ========================================
echo Deployment Complete!
echo ========================================
echo.
echo Your application is running at:
echo http://localhost:5000
echo.
echo To view logs: docker logs student-report-card-system
echo To stop: docker stop student-report-card-system
echo To remove: docker rm student-report-card-system
echo.
pause
