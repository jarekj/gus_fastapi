# RegonAPI + FastAPI

1. Add .env with GUS_API_KEY variable, use your own key
```text
GUS_API_KEY=abcde12345abcde12345 
```

2. Run:
```bash 
fastapi dev main.py
```
---
**Docker**
```bash
docker build -t gus_fastapi:latest .
docker run --name gusfastapi -p 8000:8000 --env-file ./.env -d gus_fastapi:latest
```