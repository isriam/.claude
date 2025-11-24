#!/home/jeremy/.claude/venv/bin/python3
"""
PostgreSQL Query Executor
Executes SQL queries against PostgreSQL databases with user-provided credentials.
"""

import sys
import json
import argparse
import psycopg2
from psycopg2 import sql


def execute_query(host, database, user, password, query, port=5432):
    """
    Execute a SQL query against PostgreSQL database.
    
    Args:
        host: Database host/IP address
        database: Database name
        user: Username
        password: Password
        query: SQL query to execute
        port: Database port (default: 5432)
    
    Returns:
        dict: Query results with columns, rows, and metadata
    """
    try:
        # Establish connection
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password,
            connect_timeout=10
        )
        
        # Execute query
        with conn.cursor() as cursor:
            cursor.execute(query)
            
            # Check if query returns results (SELECT)
            if cursor.description:
                columns = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()
                
                return {
                    'success': True,
                    'columns': columns,
                    'rows': rows,
                    'row_count': len(rows)
                }
            else:
                # For INSERT/UPDATE/DELETE/etc
                conn.commit()
                return {
                    'success': True,
                    'affected_rows': cursor.rowcount,
                    'message': f'{cursor.rowcount} row(s) affected'
                }
    
    except psycopg2.Error as e:
        return {
            'success': False,
            'error': str(e),
            'error_type': type(e).__name__
        }
    except Exception as e:
        return {
            'success': False,
            'error': f'Unexpected error: {str(e)}',
            'error_type': type(e).__name__
        }
    finally:
        # Always close connection
        if 'conn' in locals():
            conn.close()


def main():
    """Parse arguments and execute query."""
    parser = argparse.ArgumentParser(
        description='Execute SQL queries against PostgreSQL databases'
    )
    parser.add_argument('--host', required=True, help='Database host/IP address')
    parser.add_argument('--port', type=int, default=5432, help='Database port (default: 5432)')
    parser.add_argument('--database', required=True, help='Database name')
    parser.add_argument('--user', required=True, help='Username')
    parser.add_argument('--password', required=True, help='Password')
    parser.add_argument('--query', required=True, help='SQL query to execute')
    
    args = parser.parse_args()
    
    # Execute query
    result = execute_query(
        host=args.host,
        port=args.port,
        database=args.database,
        user=args.user,
        password=args.password,
        query=args.query
    )
    
    # Output JSON result
    print(json.dumps(result, indent=2, default=str))
    
    # Exit with appropriate code
    sys.exit(0 if result['success'] else 1)


if __name__ == '__main__':
    main()
