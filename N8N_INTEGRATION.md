# n8n Integration Guide

This guide shows you how to integrate the Audience Cleaner API with n8n to process large CSV files without memory issues.

## Problem with n8n

n8n's built-in CSV processing loads entire files into memory, causing crashes on files over 50MB. This API solves that by using streaming processing.

## Setup

### 1. Deploy the API

First, deploy the Audience Cleaner API to a server. Options:
- **Heroku**: Free tier available
- **Railway**: Easy deployment
- **Render**: Free tier available
- **Your own server**: VPS, AWS, etc.

See `web_README.md` for deployment instructions.

### 2. Get Your API URL

After deployment, you'll have a URL like:
- `https://your-app.herokuapp.com`
- `https://your-app.railway.app`
- `http://your-server.com:5000`

## n8n Workflow Setup

### Step 1: Create HTTP Request Node

1. Add an **HTTP Request** node to your workflow
2. Configure it as follows:

**Settings:**
- **Method**: `POST`
- **URL**: `https://your-api-url/upload`
- **Authentication**: None (or add API key if you set one up)
- **Send Headers**: Optional
- **Send Body**: Yes
- **Body Content Type**: `Form-Data`
- **Specify Body**: Yes

**Body Parameters:**
- **Name**: `file`
- **Type**: `File`
- **Value**: Select your file input (e.g., `{{ $binary.data }}` or from previous node)

### Step 2: Handle Response

The API returns the cleaned CSV file directly. In n8n:

1. Add a **Set** node after the HTTP Request
2. Map the response to save the file:
   - **Name**: `cleaned_file`
   - **Value**: `{{ $binary.data }}`

3. Or use **Write Binary File** node to save it:
   - **File Name**: `cleaned_output.csv`
   - **Data**: `{{ $binary.data }}`

### Step 3: Error Handling

Add an **IF** node to check for errors:

```
{{ $json.error }}
```

If error exists, send notification or log error.

## Example n8n Workflow

```
[Webhook Trigger]
    ↓
[HTTP Request Node]
    Method: POST
    URL: https://your-api-url/upload
    Body: Form-Data
    file: {{ $binary.data }}
    ↓
[IF Node]
    Condition: {{ $json.error }}
    ↓ (if error)
[Send Error Notification]
    ↓ (if success)
[Write Binary File]
    File: cleaned_output.csv
    Data: {{ $binary.data }}
```

## Complete n8n Node Configuration

### HTTP Request Node JSON

```json
{
  "parameters": {
    "method": "POST",
    "url": "https://your-api-url/upload",
    "sendBody": true,
    "bodyContentType": "multipart-form-data",
    "specifyBody": true,
    "bodyParameters": {
      "parameters": [
        {
          "name": "file",
          "type": "file",
          "value": "={{ $binary.data }}"
        }
      ]
    },
    "options": {
      "timeout": 600000
    }
  }
}
```

### Important Settings

- **Timeout**: Set to 600000 (10 minutes) for large files
- **Response Format**: Binary (for file download)
- **Error Handling**: Enable "Continue on Fail" if you want to handle errors manually

## Testing in n8n

1. Create a test workflow
2. Use a **Manual Trigger** node
3. Add **Read Binary File** node to load a test CSV
4. Connect to HTTP Request node
5. Execute and check results

## Troubleshooting

### "Request Entity Too Large"
- Increase timeout in n8n HTTP Request node
- Check API server file size limits

### "Connection Timeout"
- Large files take time to process
- Increase timeout to 600000ms (10 minutes)
- Check API server is running

### "Memory Error" (still happening)
- Make sure you're using the API, not n8n's built-in CSV processing
- The API uses streaming, so memory should stay constant

## Benefits Over n8n's Built-in Processing

| Feature | n8n Built-in | This API |
|---------|-------------|----------|
| Max File Size | ~50MB (crashes) | 500MB+ |
| Memory Usage | High (loads all) | Low (streaming) |
| Reliability | Crashes on large files | Always works |
| Processing Speed | Fast (when works) | Fast (always) |

## Advanced: Add Authentication

If you want to secure your API, add API key authentication:

1. Modify `app.py` to check for API key header
2. In n8n HTTP Request node, add header:
   - **Name**: `X-API-Key`
   - **Value**: `your-api-key`

## Support

For issues or questions:
- Check API health: `GET /health`
- Check API docs: `GET /`
- Review server logs

