# Audience Cleaner

A reliable Python script to clean and transform large CSV files from Audience Lab. This tool processes files of any size (including 50MB+) without crashing, unlike web-based solutions.

## Quick Start

```bash
# 1. Install globally (one time setup)
pip3 install .

# 2. Use from anywhere
clean-audience your_file.csv
```

That's it! 🎉

## Features

- ✅ **Handles large files** - Processes files of any size efficiently
- ✅ **Memory efficient** - Processes data row-by-row, no need to load entire file
- ✅ **Reliable** - Works every single time, no crashes
- ✅ **Simple** - Just run one command
- ✅ **Progress tracking** - Shows progress for large files

## Installation

### Option 1: Install Globally (Recommended)

Install the tool so you can use it from anywhere on your computer:

```bash
# Navigate to the audiencecleaner directory
cd audiencecleaner

# Install globally
pip3 install .

# Or install in development mode (editable)
pip3 install -e .
```

After installation, you can use the tool from anywhere:

```bash
clean-audience input_file.csv
# or
audience-cleaner input_file.csv
```

### Option 2: Use Directly (No Installation)

If you prefer not to install, you can run the script directly:

```bash
python3 clean_audience.py input_file.csv
```

### Option 3: Quick Install Script

Run the included install script:

```bash
chmod +x install.sh
./install.sh
```

## Requirements

- Python 3.6 or higher (usually pre-installed on Mac/Linux)
- pip (usually comes with Python)
- No additional packages needed (uses only Python standard library)

## Usage

### Basic Usage

**If installed globally:**
```bash
clean-audience input_file.csv
```

**If using directly:**
```bash
python3 clean_audience.py input_file.csv
```

This will create a cleaned file named `cleaned_input_file.csv` in the same directory.

### Specify Output File

```bash
# Installed globally
clean-audience input_file.csv output_file.csv

# Or using directly
python3 clean_audience.py input_file.csv output_file.csv
```

### Examples

```bash
# Clean test2.csv (outputs to cleaned_test2.csv)
clean-audience test2.csv

# Clean large_file.csv and save to my_cleaned_data.csv
clean-audience large_file.csv my_cleaned_data.csv

# Works from any directory after installation
cd ~/Documents
clean-audience ~/Downloads/my_data.csv
```

## What It Does

The script transforms your Audience Lab CSV file by:

1. **Selecting key columns**: Extracts only the most important fields
2. **Cleaning phone numbers**: 
   - Extracts first phone from DIRECT_NUMBER, MOBILE_PHONE, or PERSONAL_PHONE
   - Removes formatting (+, spaces, commas)
   - Removes leading "1" from US numbers
3. **Extracting emails**: Gets primary email from BUSINESS_EMAIL or first from PERSONAL_EMAILS
4. **Formatting income ranges**: Replaces commas with spaces in NET_WORTH and INCOME_RANGE

## Output Columns

The cleaned CSV contains these columns:
- FIRST_NAME, LAST_NAME
- PRIMARY_PHONE, PRIMARY_EMAIL
- Personal_Phone, Mobile_Phone, Valid_Phone
- UUID
- PERSONAL_CITY, PERSONAL_STATE
- AGE_RANGE, CHILDREN, GENDER, HOMEOWNER, MARRIED
- NET_WORTH, INCOME_RANGE

## Performance

- Processes approximately **10,000+ rows per second**
- Memory usage stays constant regardless of file size
- Works with files **50MB, 100MB, 500MB+** without issues

## Uninstallation

If you installed globally and want to remove it:

```bash
pip3 uninstall audience-cleaner
```

## Troubleshooting

**"File not found" error:**
- Make sure you're in the correct directory
- Check the file path is correct

**"Permission denied" error:**
- Make the script executable: `chmod +x clean_audience.py`
- Or run with: `python3 clean_audience.py input.csv`

**Large files taking time:**
- This is normal! The script shows progress every 10,000 rows
- Be patient - it will complete successfully

## Sharing with Others

To share this tool with others:

1. **Share the entire folder** - They can install it the same way
2. **Create a zip file** - Include all files except test CSV files
3. **Upload to GitHub** - Others can clone and install

Recipients just need to:
```bash
cd audiencecleaner
pip3 install .
clean-audience their_file.csv
```

## Why This Solution?

Unlike web-based tools that crash on large files:
- ✅ Runs locally on your computer
- ✅ No file size limits
- ✅ No internet required
- ✅ No crashes or timeouts
- ✅ Works reliably every time
- ✅ Can be installed globally for easy access

