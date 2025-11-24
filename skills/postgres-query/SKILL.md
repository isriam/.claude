# PostgreSQL Query Skill

Execute SQL queries against PostgreSQL databases with user-provided credentials.

## Description

This skill allows you to connect to any PostgreSQL database and execute SQL queries. The user provides connection credentials in natural language, and you extract the details and execute queries as needed.

## When to Use

Use this skill when the user:
- Mentions connecting to PostgreSQL, Postgres, or a specific database
- Asks questions about data in a database
- Wants to query, select, insert, update, or analyze database data
- Provides database connection details (host, database name, username, password)

## Usage Pattern

1. **User provides connection details** in natural language like:
   - "Connect to postgres on 192.0.2.14 database finances with user finances password finances"
   - "Query the inventory database on db.example.com as admin password secret123"

2. **Extract connection parameters:**
   - Host/IP address
   - Port (default: 5432)
   - Database name
   - Username
   - Password

3. **User asks questions** about the data:
   - "Tell me about my expenses this month"
   - "Show me all customers in California"
   - "What's the total revenue for Q4?"

4. **Generate appropriate SQL queries** based on user questions

5. **Execute queries** using this skill with the connection parameters

## Security Notes

- Credentials are NEVER stored - only passed as parameters for immediate use
- Each query creates a fresh connection and closes it immediately
- No persistent database connections
- Connection details remain in conversation context only

## Examples

**User:** "Connect to postgres on 192.0.2.14 database finances with user finances password finances and tell me about my expenses this month"

**You should:**
1. Extract: host=192.0.2.14, database=finances, user=finances, password=finances
2. Generate SQL: `SELECT * FROM expenses WHERE date >= date_trunc('month', CURRENT_DATE)`
3. Execute using this skill
4. Present results to user

**User:** "What were my top 5 expenses last month?"

**You should:**
1. Use same connection details from earlier in conversation
2. Generate SQL: `SELECT * FROM expenses WHERE date >= date_trunc('month', CURRENT_DATE - interval '1 month') AND date < date_trunc('month', CURRENT_DATE) ORDER BY amount DESC LIMIT 5`
3. Execute using this skill
4. Present results

## Command

`~/.claude/skills/postgres-query/query.py --host HOST --database DATABASE --user USER --password PASSWORD --query "SQL_QUERY" [--port PORT]`

## Parameters

- `--host`: Database host/IP address (required)
- `--database`: Database name (required)
- `--user`: Username (required)
- `--password`: Password (required)
- `--query`: SQL query to execute (required)
- `--port`: Database port (optional, default: 5432)

## Output

Returns JSON with:
- `columns`: List of column names
- `rows`: List of row data
- `row_count`: Number of rows returned
- `success`: Boolean indicating success/failure
- `error`: Error message if query failed
