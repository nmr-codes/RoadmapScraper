from bs4 import BeautifulSoup
import requests as rq
import pandas as pd

# Getting cards' levels on HTML page
def project_level_extractor(soup: BeautifulSoup):
    level_container_class = 'flex justify-between gap-1.5'
    all_levels = soup.find_all(class_=level_container_class)
    output = []
    for level in all_levels:
        output.append(level.find('span').string)
    return output

# Getting projects' type (CLI, Web and etc.)
def project_type_extractor(soup: BeautifulSoup):
    type_container_class = 'flex justify-between gap-1.5'
    all_project_types = soup.find_all(class_=type_container_class)
    output = []
    for project_type in all_project_types:
        output.append(project_type.find('span').find_next_sibling('span').string)
    return output

# Getting projects main title
def project_name_extractor(soup: BeautifulSoup):
    name_container_class = 'my-3 flex min-h-[100px] flex-col'
    all_project_names = soup.find_all(class_=name_container_class)
    output = []
    for project_name in all_project_names:
        output.append(project_name.find('span').string)
    return output

# Getting short description of project
def short_description_extractor(soup: BeautifulSoup):
    description_container_class = 'my-3 flex min-h-[100px] flex-col'
    all_short_descriptions = soup.find_all(class_=description_container_class)
    output = []
    for short_description in all_short_descriptions:
        output.append(short_description.find('span').find_next_sibling('span').string)
    return output

# Getting Project Details Page urls
def pdp_url_extractor(prefix_url: str, soup: BeautifulSoup):
    card_container_class = 'flex flex-col rounded-md border bg-white p-3 transition-colors hover:border-gray-300 hover:bg-gray-50'
    all_pdp_urls = soup.find_all(class_=card_container_class)
    output = []
    for pdp_url in all_pdp_urls:
        output.append(f"{prefix_url}{pdp_url['href']}")
    return output

# Main function
def roadmap_scraper(url: str = None, file_name: str = 'projects.csv'):
    html_page = rq.get(f'{url}').text
    soup = BeautifulSoup(html_page, 'html.parser')
    # all_cards = soup.find_all(class_='flex flex-col rounded-md border bg-white p-3 transition-colors hover:border-gray-300 hover:bg-gray-50')
    level = project_level_extractor(soup=soup)
    project_type = project_type_extractor(soup=soup)
    project_name = project_name_extractor(soup=soup)
    short_description = short_description_extractor(soup=soup)
    pdp_url = pdp_url_extractor(prefix_url=url, soup=soup)
    df = pd.DataFrame({
        'level': level,
        'project_type': project_type,
        'project_name': project_name,
        'short_description': short_description,
        'pdp_url': pdp_url
    })
    df.to_csv(file_name)


if __name__ == '__main__':
    url = 'https://roadmap.sh/python/projects'
    roadmap_scraper(url=url)
    print("Projects data successfully scraped.")