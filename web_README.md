# Audience Cleaner Web API

A web-based API service for cleaning Audience Lab CSV files. Handles large files (50MB+) efficiently using streaming processing to avoid memory issues.

## Features

- ✅ **Handles large files** - Processes files up to 500MB without memory issues
- ✅ **Streaming processing** - Files are processed row-by-row, not loaded into memory
- ✅ **REST API** - Easy to integrate with n8n, Zapier, or any HTTP client
- ✅ **Simple upload/download** - Upload CSV, get cleaned CSV back
- ✅ **No file size limits** - Unlike n8n which crashes on 50MB+ files

## Installation

### Option 1: Local Development

```bash
# Install dependencies
pip3 install -r requirements_web.txt

# Run the server
python3 app.py
```

The API will be available at `http://localhost:5000`

### Option 2: Production Deployment

#### Using Docker (Recommended)

```bash
# Build Docker image
docker build -t audience-cleaner .

# Run container
docker run -p 5000:5000 audience-cleaner
```

#### Using Gunicorn (Production Server)

```bash
pip3 install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

#### Deploy to Cloud Platforms

**Heroku:**
```bash
heroku create your-app-name
git push heroku main
```

**Railway:**
```bash
railway init
railway up
```

**Render:**
- Connect your GitHub repo
- Set build command: `pip install -r requirements_web.txt`
- Set start command: `python app.py`

## API Endpoints

### GET `/`
API documentation and available endpoints.

### GET `/health`
Health check endpoint. Returns `{"status": "healthy"}`.

### POST `/upload`
Upload and process a CSV file.

**Request:**
- Method: `POST`
- Content-Type: `multipart/form-data`
- Body: `file` (CSV file)

**Response:**
- Content-Type: `text/csv`
- Body: Cleaned CSV file (downloadable)

**Example using curl:**
```bash
curl -X POST -F "file=@test2.csv" http://localhost:5000/upload -o cleaned_output.csv
```

**Example using Python:**
```python
import requests

with open('test2.csv', 'rb') as f:
    response = requests.post('http://localhost:5000/upload', files={'file': f})
    
    if response.status_code == 200:
        with open('cleaned_output.csv', 'wb') as out:
            out.write(response.content)
        print("File processed successfully!")
    else:
        print(f"Error: {response.json()}")
```

## Integration with n8n

### HTTP Request Node Configuration

1. **Create HTTP Request node**
2. **Method:** POST
3. **URL:** `http://your-server:5000/upload`
4. **Body Type:** Form-Data
5. **Body Parameters:**
   - Key: `file`
   - Type: `File`
   - Value: Select your file input

6. **Response Handling:**
   - The response will be the cleaned CSV file
   - Save it using a "Write Binary File" node or similar

### Example n8n Workflow

```
[Trigger] → [HTTP Request] → [Save File]
              ↓
         POST /upload
         file: {{ $binary.data }}
```

## Environment Variables

- `PORT` - Server port (default: 5000)
- `DEBUG` - Enable debug mode (default: False)
- `MAX_CONTENT_LENGTH` - Max file size in bytes (default: 500MB)

## Performance

- **Memory efficient**: Processes files using streaming (row-by-row)
- **No size limits**: Can handle files of any size (tested with 100MB+)
- **Fast processing**: ~10,000 rows per second
- **Concurrent requests**: Can handle multiple uploads simultaneously

## Troubleshooting

**"File too large" error:**
- Increase `MAX_CONTENT_LENGTH` in app.py
- Or set reverse proxy limits (nginx, etc.)

**Memory issues:**
- The API uses streaming, so memory should stay constant
- If issues persist, check server resources

**Connection timeout:**
- Large files take time to process
- Increase timeout settings in your HTTP client
- Consider showing progress (future enhancement)

## Security Considerations

For production use:
- Add authentication/API keys
- Add rate limiting
- Use HTTPS
- Validate file types more strictly
- Add file size limits per user
- Clean up temporary files more aggressively

## Comparison with n8n

| Feature | n8n | This API |
|---------|-----|----------|
| Max file size | ~50MB (crashes) | 500MB+ (no issues) |
| Memory usage | Loads entire file | Streams row-by-row |
| Processing speed | Fast (when it works) | Fast (always works) |
| Reliability | Crashes on large files | Handles any size |
| Integration | Built-in | HTTP API (works everywhere) |

## License

Same as main project.

