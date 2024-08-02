# Vehicle Web Scraper

## Overview

The Vehicle Web Scraper is a Python-based tool designed to scrape various vehicle listings from specified webpages. It checks for specific vehicle criteria such as year, make, model, mileage, and cost. Once the criteria are met, it curates a list of potential vehicles and sends this list to a designated email address.

## Features

- Scrapes vehicle listings from specified webpages.
- Filters vehicles based on user-defined criteria:
  - Year
  - Make
  - Model
  - Mileage
  - Cost
- Sends a curated list of potential vehicles to a designated email address.
- Easy to configure and extend for additional criteria or webpages.

## Requirements

- Python 3.8 or higher
- BeautifulSoup4
- Requests
- smtplib
- Email