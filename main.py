from app import app, create_tables

if __name__ == "__main__":
    create_tables()  # Create database tables first
    
    # Import routes after tables are created to avoid circular imports
    import routes  # noqa: F401
    
    app.run(host='0.0.0.0', port=5009, debug=True)
