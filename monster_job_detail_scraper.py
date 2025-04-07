from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import json

# Initialize Crawlbase API with your access token
crawling_api = CrawlingAPI({'token': 'YOUR_CRAWLBASE_TOKEN'})

def scrape_job_page(url):
    options = {
        'ajax_wait': 'true',
        'page_wait': '5000'  # Wait for the page to fully load
    }

    response = crawling_api.get(url, options)
    if response['headers']['pc_status'] == '200':
        soup = BeautifulSoup(response['body'].decode('utf-8'), 'html.parser')

        job_title = soup.select_one('h2[data-testid="jobTitle"]').text.strip() if soup.select_one('h2[data-testid="jobTitle"]') else ''
        job_description = soup.select_one('div[data-testid="svx-description-container-inner"]').text.strip() if soup.select_one('div[data-testid="svx-description-container-inner"]') else ''
        numbersAndfacts = [{tr.select_one('td:first-child').text.strip() : tr.select_one('td:last-child').text.strip()} for tr in soup.select('table[data-testid="svx-jobview-details-table"] tr')] if soup.select('table[data-testid="svx-jobview-details-table"] tr') else []
        about_company = soup.select_one('div[class*="about-styles__AboutCompanyContainerInner"]').text.strip() if soup.select_one('div[class*="about-styles__AboutCompanyContainerInner"]') else ''

        job_details = {
            'Job Title': job_title,
            'Job Description': job_description,
            'Numbers & Facts': numbersAndfacts,
            'About Company': about_company
        }

        return job_details
    else:
        print(f"Failed to fetch data. Status code: {response['headers']['pc_status']}")
        return None

def save_job_details_to_json(data, filename='job_details.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    job_url = 'https://www.monster.com/job-openings/d94729d8-929e-4c61-8f26-fd480c31e931'
    job_details = scrape_job_page(job_url)

    if job_details:
        save_job_details_to_json(job_details)