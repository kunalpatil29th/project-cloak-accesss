# Utils Module

Utility classes and functions used across the project.

## Modules

### logger.py

Custom logging setup with:
- Timestamp formatting
- Log levels (INFO, WARNING, ERROR)
- Console output
- Prevents duplicate handlers

### db_manager.py

SQLite database manager for session tracking:
- CRUD operations for sessions
- Session statistics (total, average duration)
- Safe database connections
- Auto-initialization

## Usage

```python
from utils.logger import logger
from utils.db_manager import DBManager

logger.info("Hello, World!")

db = DBManager()
db.log_session(start_time, end_time)
```
