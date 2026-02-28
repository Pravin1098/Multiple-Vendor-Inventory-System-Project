# Multiple Vendor Inventory System

This project is a **Multiple Vendor Inventory System** built with **FastAPI** and **MongoDB**. The application is containerized using **Docker** for easy deployment and scaling.

---

## Requirements

- **Docker** and **Docker Compose** installed on your system.
- **Python 3.12+** (if you're running the app outside Docker for development).
- **MongoDB** for database storage.

## Setup and Installation

**Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/Pravin1098/Multiple-Vendor-Inventory-System.git
   cd Multiple-Vendor-Inventory-System


Step 1: Build the Docker Containers
docker-compose build


Step 2: Run the Docker Containers
docker-compose up

This will:
Start the MongoDB container.
Build and run the FastAPI application container.
The application will be available at http://localhost:4000, and the MongoDB service will be accessible at mongodb://localhost:27018.


API Documentation
http://localhost:4000/docs
This is a Swagger-based interactive documentation that allows you to explore the available endpoints.