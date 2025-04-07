from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import json

# Initialize Crawlbase API with your access token
crawling_api = CrawlingAPI({'token': 'YOUR_CRAWLBASE_TOKEN'})

def scrape_monster_with_pagination(url):
    options = {
        'ajax_wait': 'true',
        'scroll': 'true',  # Enables scroll pagination
        'scroll_interval': '60'  # Scroll duration set to 60 seconds
    }

    response = crawling_api.get(url, options)
    if response['headers']['pc_status'] == '200':
        soup = BeautifulSoup(response['body'], 'html.parser')
        job_cards = soup.select('div#JobCardGrid article[data-testid="svx_jobCard"]')

        all_jobs = []
        for job in job_cards:
            title = job.select_one('a[data-testid="jobTitle"]').text.strip() if job.select_one('a[data-testid="jobTitle"]') else ''
            company = job.select_one('span[data-testid="company"]').text.strip() if job.select_one('span[data-testid="company"]') else ''
            location = job.select_one('span[data-testid="jobDetailLocation"]').text.strip() if job.select_one('span[data-testid="jobDetailLocation"]') else ''
            link = job.select_one('a[data-testid="jobTitle"]')['href'] if job.select_one('a[data-testid="jobTitle"]') else ''

            all_jobs.append({
                'Job Title': title,
                'Company': company,
                'Location': location,
                'Job Link': link
            })

        return all_jobs
    else:
        print(f"Failed to fetch data. Status code: {response['headers']['pc_status']}")
        return None

def save_to_json(data, filename='monster_jobs.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    base_url = 'https://www.monster.com/jobs/search?q=Java+Developers&where=New+York&page=1&so=p.s.lh'
    jobs = scrape_monster_with_pagination(base_url)

    if jobs:
        save_to_json(jobs)