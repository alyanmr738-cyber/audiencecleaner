#!/usr/bin/env python3
"""
Test script for the Audience Cleaner API
"""

import requests
import sys
from pathlib import Path

def test_api(base_url="http://localhost:5000"):
    """Test the API endpoints."""
    
    print("🧪 Testing Audience Cleaner API")
    print("=" * 50)
    
    # Test health endpoint
    print("\n1. Testing health endpoint...")
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("✅ Health check passed:", response.json())
        else:
            print("❌ Health check failed:", response.status_code)
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False
    
    # Test file upload
    test_file = Path("test2.csv")
    if not test_file.exists():
        print(f"\n⚠️  Test file {test_file} not found. Skipping upload test.")
        return True
    
    print(f"\n2. Testing file upload with {test_file}...")
    try:
        with open(test_file, 'rb') as f:
            files = {'file': (test_file.name, f, 'text/csv')}
            response = requests.post(f"{base_url}/upload", files=files, timeout=300)
        
        if response.status_code == 200:
            output_file = Path("test_api_output.csv")
            with open(output_file, 'wb') as out:
                out.write(response.content)
            print(f"✅ File processed successfully!")
            print(f"   Output saved to: {output_file}")
            print(f"   Output size: {len(response.content):,} bytes")
            return True
        else:
            print(f"❌ Upload failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Upload error: {e}")
        return False

if __name__ == '__main__':
    base_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:5000"
    success = test_api(base_url)
    sys.exit(0 if success else 1)

