#!/usr/bin/env python3
"""
FolderLens - Folder Analyzer Application

Run this script to start the Flask development server.
Make sure you have activated the virtual environment first:
    source venv/bin/activate
"""

from app import create_app

if __name__ == '__main__':
    app = create_app()
    
    print("🚀 Starting FolderLens - Folder Analyzer")
    print("📁 Open your browser and navigate to: http://localhost:5000")
    print("🔧 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    # Run the Flask development server
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True,
        use_reloader=True
    )