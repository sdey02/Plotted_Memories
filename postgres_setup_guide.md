# PostgreSQL Setup Guide for Plotted Memories

This guide will help you set up PostgreSQL for the Plotted Memories application.

## Prerequisites

- PostgreSQL installed on your system
- Python dependencies installed: `psycopg2-binary` and `python-dotenv`

## Installation Steps

### 1. Install PostgreSQL

**macOS:**
```bash
brew install postgresql
brew services start postgresql
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

### 2. Create Database and User

```bash
# Login to PostgreSQL as postgres user
sudo -u postgres psql

# Inside PostgreSQL CLI, create a user and database
CREATE USER username WITH PASSWORD 'password';
CREATE DATABASE plotted_memories;
GRANT ALL PRIVILEGES ON DATABASE plotted_memories TO username;

# Exit PostgreSQL CLI
\q
```

### 3. Update Environment Variables

Edit the `.env` file to use your PostgreSQL credentials:

```
DATABASE_URL=postgresql://username:password@localhost:5432/plotted_memories
```

Replace `username` and `password` with the values you created in step 2.

### 4. Run the Application

The application will automatically create the necessary tables when it first runs with the PostgreSQL database.

## Troubleshooting

- **Connection Issues**: Make sure PostgreSQL service is running
- **Authentication Errors**: Verify the username and password in `.env`
- **Permission Errors**: Ensure your user has proper permissions to the database

## Data Migration (if needed)

If you need to migrate existing data from SQLite to PostgreSQL:

1. Install pgloader: `brew install pgloader` (macOS) or `sudo apt install pgloader` (Ubuntu/Debian)
2. Run the migration:
   ```bash
   pgloader users.sqlite3 postgresql://username:password@localhost:5432/plotted_memories
   ```

## Verifying Connection

To verify that your application is using PostgreSQL instead of SQLite, check the console logs when starting the application. You should see connection information for PostgreSQL instead of SQLite. 