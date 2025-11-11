@echo off
echo ========================================
echo Student Report Card System - Docker Compose Deployment
echo ========================================
echo.

echo Building and starting containers...
docker-compose up --build -d

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Docker Compose deployment failed!
    echo This might be due to network issues.
    echo Please check your internet connection and try again.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Deployment Successful!
echo ========================================
echo.
echo Your application is now running at:
echo http://localhost:5000
echo.
echo To view logs: docker-compose logs -f
echo To stop: docker-compose down
echo.
pause

