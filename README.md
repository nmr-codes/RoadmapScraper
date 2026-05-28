# Roadmap.sh Python Projects Scraper

A simple web scraper built with Python that extracts Python project information from the [roadmap.sh](https://roadmap.sh) projects page and saves the data into a CSV file.

## Features

* Extracts project difficulty levels
* Extracts project types (CLI, Web, etc.)
* Extracts project names
* Extracts short project descriptions
* Extracts project detail page URLs
* Saves scraped data into a CSV file using Pandas

---

## Technologies Used

* Python 3
* BeautifulSoup4
* Requests
* Pandas

---

## Installation

Clone the repository:

```bash
git clone https://github.com/nmr-codes/RoadmapScraper.git
cd RoadmapScraper
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script:

```bash
python scraper.py
```

After execution, a CSV file named `projects.csv` will be created in the project directory.

---

## Example Output

| level    | project_type | project_name | short_description         | pdp_url                |
| -------- | ------------ | ------------ | ------------------------- | ---------------------- |
| Beginner | CLI          | Task Tracker | Track tasks from terminal | https://roadmap.sh/... |

---

## Project Structure

```text
.
├── scraper.py
├── requirements.txt
└── README.md
```

---

## Code Overview

### Extractor Functions

The scraper contains separate extractor functions for:

* `project_level_extractor()`
* `project_type_extractor()`
* `project_name_extractor()`
* `short_description_extractor()`
* `pdp_url_extractor()`

Each function parses a specific part of the HTML page using BeautifulSoup.

### Main Function

```python
roadmap_scraper(url, file_name='projects.csv')
```

This function:

1. Sends an HTTP request to the target page
2. Parses HTML content
3. Extracts project data
4. Creates a Pandas DataFrame
5. Exports the data to CSV

---

## Default Target URL

```python
https://roadmap.sh/python/projects
```

You can modify the URL to scrape projects from other roadmap.sh paths.

Example:

```python
url = 'https://roadmap.sh/frontend/projects'
```

---

## Notes

* The scraper depends on the current HTML structure of roadmap.sh.
* If the website changes its CSS classes or layout, the scraper may stop working.
* Always respect the website’s Terms of Service and robots.txt policies before scraping.

---

## Future Improvements

* Add error handling
* Add logging
* Support pagination
* Export to JSON/Excel
* Add command-line arguments
* Add async requests for faster scraping

---

## Author
* Name: Abdurasul Nematxonov
* Telegram: https://t.me/lazydasturchi
* Instagram: https://instagram.com/nematxonovv

---

## License

This project is licensed under the MIT License.

---
