#!/bin/bash

echo "========================================"
echo "Student Report Card System - Docker Deployment"
echo "========================================"
echo ""

echo "Checking Docker installation..."
if ! command -v docker &> /dev/null; then
    echo "ERROR: Docker is not installed or not in PATH"
    echo "Please install Docker from https://www.docker.com/products/docker-desktop"
    exit 1
fi

echo "Docker is installed!"
echo ""

echo "Building Docker image..."
docker build -t student-report-card-system .

if [ $? -ne 0 ]; then
    echo "ERROR: Failed to build Docker image"
    exit 1
fi

echo ""
echo "Image built successfully!"
echo ""

echo "Starting container..."
docker run -d -p 5000:5000 --name student-report-card-system student-report-card-system

if [ $? -ne 0 ]; then
    echo "Container might already be running. Stopping and removing old container..."
    docker stop student-report-card-system 2>/dev/null
    docker rm student-report-card-system 2>/dev/null
    echo "Starting new container..."
    docker run -d -p 5000:5000 --name student-report-card-system student-report-card-system
fi

echo ""
echo "========================================"
echo "Deployment Complete!"
echo "========================================"
echo ""
echo "Your application is running at:"
echo "http://localhost:5000"
echo ""
echo "To view logs: docker logs student-report-card-system"
echo "To stop: docker stop student-report-card-system"
echo "To remove: docker rm student-report-card-system"
echo ""

