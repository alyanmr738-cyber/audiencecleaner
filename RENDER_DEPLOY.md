# Deploying to Render

## Choose: **Web Services** ✅

Your Audience Cleaner API is a **Web Service** because it:
- Accepts HTTP requests (POST /upload)
- Processes files dynamically
- Returns responses (cleaned CSV files)
- Needs to run continuously

## Quick Deploy Steps

### Option 1: Connect GitHub Repository (Recommended)

1. **Push your code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/audiencecleaner.git
   git push -u origin main
   ```

2. **Go to Render Dashboard**
   - Visit https://dashboard.render.com
   - Click "New +" → "Web Service"

3. **Connect Repository**
   - Select "Build and deploy from a Git repository"
   - Connect your GitHub account
   - Select the `audiencecleaner` repository

4. **Configure Service**
   - **Name**: `audience-cleaner` (or any name you like)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements_web.txt`
   - **Start Command**: `python app.py`
   - **Plan**: Free (or paid for more resources)

5. **Environment Variables** (Optional)
   - `PORT`: `10000` (Render sets this automatically, but you can specify)
   - `DEBUG`: `false`

6. **Click "Create Web Service"**

Render will automatically:
- Build your app
- Deploy it
- Give you a URL like `https://audience-cleaner.onrender.com`

### Option 2: Manual Deploy (Without Git)

1. **Go to Render Dashboard**
   - Visit https://dashboard.render.com
   - Click "New +" → "Web Service"

2. **Manual Deploy**
   - Select "Deploy without a Git repository"
   - Upload your project files (or use Render CLI)

3. **Configure the same settings as above**

## Important Settings

### Build Command
```
pip install -r requirements_web.txt
```

### Start Command
```
python app.py
```

### Health Check Path
```
/health
```

## After Deployment

Your API will be available at:
```
https://your-app-name.onrender.com
```

### Test Your Deployment

1. **Health Check**
   ```bash
   curl https://your-app-name.onrender.com/health
   ```

2. **Upload a File**
   ```bash
   curl -X POST \
     -F "file=@test2.csv" \
     https://your-app-name.onrender.com/upload \
     -o cleaned_output.csv
   ```

3. **Access Web Interface**
   Visit: `https://your-app-name.onrender.com`
   - You'll see a web form to upload files
   - Or see API documentation

## n8n Integration

Once deployed, use your Render URL in n8n:

```
https://your-app-name.onrender.com/upload
```

See `N8N_INTEGRATION.md` for complete n8n setup instructions.

## Free Tier Limitations

Render's free tier has:
- ✅ 750 hours/month (enough for 24/7)
- ✅ 512MB RAM (sufficient for streaming processing)
- ⚠️ Spins down after 15 minutes of inactivity
- ⚠️ First request after spin-down takes ~30 seconds

**Solution for n8n**: 
- Use a health check service (like UptimeRobot) to ping `/health` every 10 minutes
- Or upgrade to paid plan for always-on service

## Troubleshooting

### "Application Error"
- Check logs in Render dashboard
- Make sure `requirements_web.txt` includes all dependencies
- Verify `app.py` is in the root directory

### "Build Failed"
- Check that `requirements_web.txt` exists
- Verify Python version (Render uses Python 3.11 by default)
- Check build logs for specific errors

### "Timeout"
- Large files take time to process
- Free tier has request timeout limits
- Consider upgrading for larger files

### "Memory Error"
- Free tier has 512MB RAM
- The app uses streaming, so should work fine
- If issues persist, upgrade plan

## Updating Your App

1. Push changes to GitHub
2. Render automatically rebuilds and redeploys
3. Or manually trigger deploy from Render dashboard

## Custom Domain (Optional)

1. Go to your service settings
2. Click "Custom Domains"
3. Add your domain
4. Update DNS records as instructed

## Monitoring

- View logs in real-time from Render dashboard
- Set up alerts for errors
- Monitor usage and performance

## Cost

- **Free**: $0/month (with limitations)
- **Starter**: $7/month (always-on, more resources)
- **Standard**: $25/month (even more resources)

For production use with n8n, consider the Starter plan to avoid spin-down delays.

