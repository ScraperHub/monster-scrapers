# Monster.com Job Scrapers

## 📝 Description

This repository provides two Python-based scrapers to extract job data from Monster.com using the Crawlbase Crawling API. It supports both listing pages with scroll-based pagination and individual job detail pages.

➡️ [Read the full blog here](https://crawlbase.com/blog/how-to-scrape-monster-jobs-with-python/) to learn more.

## 🛠️ Scrapers Overview

### 1. Monster.com Job Listings Scraper (`monster_listing_scraper.py`)

Scrapes job data from Monster search result pages using scroll-based pagination handled by the Crawlbase Crawling API.

**Extracted Fields**:

- Job Title
- Company
- Location
- Job Link

**Pagination**: Scroll-based, using the scroll and scroll_interval options in the Crawling API.

The data is saved as a JSON file: monster_jobs.json.

### 2. Monster.com Job Detail Scraper (`monster_job_detail_scraper.py`)

Scrapes detailed information from a single Monster job posting page.

Extracted Fields:

- **Job Title**
- **Job Description**
- **Numbers & Facts (Key-Value Data Table)**
- **About Company**

The data is saved in `job_details.json`.

## ⚙️ Environment Setup

Ensure Python is installed:

```bash
python --version
```

Install required dependencies:

```bash
pip install crawlbase beautifulsoup4
```

## 🚀 Running the Scrapers

### 1. Set Your Crawlbase Token

Replace '`YOUR_CRAWLBASE_TOKEN`' in both scripts with your actual JS token from [Crawlbase](https://app.crawlbase.com/signup).

### 2. Run Listing Scraper

```bash
python monster_listing_scraper.py
```

### 3. Run Job Detail Scraper

```bash
python monster_job_detail_scraper.py
```

## ✅ Example Output

### Listings Output (`monster_jobs.json`)

```json
[
  {
    "Job Title": "Java Developer",
    "Company": "ABC Tech",
    "Location": "New York, NY",
    "Job Link": "https://www.monster.com/job-openings/abc123"
  },
  ...
]
```

### Job Detail Output (`job_details.json`)

```json
{
	{
  "Job Title": "Delivery Station Warehouse Associate",
  "Job Description": "Amazon Delivery Station Warehouse AssociateJob ....",
  "Numbers & Facts": {
    "Location": "Revere, MA",
    "Job Type": "Temporary, Part-time",
    "Industry": "Transport and Storage - Materials",
    "Salary": "$18.50 Per Hour",
    "Company Size": "10,000 employees or more",
    "Year Founded": "1994",
    "Website": "http://Amazon.com/militaryroles"
  },
  "About Company": "At Amazon, we don't wait for the next ..."
}
```

## 📌 To-Do List

- Add support for extracting salary, benefits, or other dynamic job attributes.
- Support multi-location filtering via CLI.
- Export output to CSV format.
- Add error handling retries using exponential backoff.

## 💡 Why Use These Scrapers?

- Uses Crawlbase Crawling API to handle JavaScript-heavy content and bot protection.
- Supports scroll-based pagination on job listings.
- Extracts both high-level listings and detailed job information.
- Saves structured data ready for analysis or storage.
