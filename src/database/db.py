import sqlite3 as sqlite
import os

class DatabaseClient:
    def __init__(self, filepath: str = "sqlite.db"):
        #TODO: Filepath validation
        self._filepath = filepath
        self._conn = self._connect()
        self._cur = self._conn.cursor()
        
        self._initialize_schema()

    def _connect(self):
        return sqlite.connect(self._filepath)
    
    def close(self):
        self._conn.close()
        
    def _initialize_schema(self):
        self._cur.executescript("""
            -- Collection Items (main table)
            CREATE TABLE IF NOT EXISTS collection_item (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL,
                image_url TEXT,
                source_url TEXT NOT NULL,
                source_id TEXT,
                brand_id INTEGER NOT NULL,
                source_site_id INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_price_check TIMESTAMP,
                FOREIGN KEY (brand_id) REFERENCES brand(id),
                FOREIGN KEY (source_site_id) REFERENCES sources(id)
            );

            -- Brands lookup table
            CREATE TABLE IF NOT EXISTS brand (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            -- Sources lookup table
            CREATE TABLE IF NOT EXISTS sources (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                base_url TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            -- Indexes for common queries
            CREATE INDEX idx_collection_brand ON collection_item(brand_id);
            CREATE INDEX idx_collection_source ON collection_item(source_site_id);
            CREATE INDEX idx_brand_name ON brand(name);
            CREATE INDEX idx_sources_name ON sources(name);

            -- Triggers to auto-update timestamps
            CREATE TRIGGER update_collection_item_timestamp 
                AFTER UPDATE ON collection_item
                BEGIN
                    UPDATE collection_item SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
                END;
        """)