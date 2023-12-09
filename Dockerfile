# Use the official PostgreSQL image from Docker Hub
FROM postgres:latest

# Set the environment variables for the PostgreSQL container
ENV POSTGRES_USER myuser
ENV POSTGRES_PASSWORD mypassword
ENV POSTGRES_DB mydb

# Expose the PostgreSQL default port (5432)
EXPOSE 5432
