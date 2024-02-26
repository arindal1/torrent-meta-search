#!/usr/bin/env python3

import asyncio
import json
import argparse
from aiohttp import ClientSession, ClientError
from aiohttp.http_exceptions import HttpProcessingError
from urllib.parse import quote
from collections import defaultdict
from re import sub
from bs4 import BeautifulSoup

# Default dictionary to store results categorized by type
results = defaultdict(list)

# Dictionary containing URLs for torrent websites
urlList = {
    'thepiratebay': 'https://thepiratebay10.org/search/{query}/{page}/99/0',
    '1337x': 'https://1337x.to/search/{query}/{page}/',
    'torlock': 'https://www.torlock.com/all/torrents/{query}/{page}.html'
}

# Dictionary mapping category names to their respective labels
category_list = {
    'anime': 'Anime',
    'applications': 'Applications',
    'documentaries': 'Documentaries',
    'games': 'Games',
    'movies': 'Movies',
    'music': 'Music',
    'other': 'Other',
    'television': 'Television',
    'xxx': 'XXX',
    'unknown': 'Unknown'
}

# Function to create a dictionary object representing a torrent
def to_object(
    title: str = '',
    url: str = '',
    magnet_link: str = '',
    seeder: int = None,
    leecher: int = None
):
    return {
        'title': title,
        'url': url,
        'magett-link': magnet_link,
        'seeder': seeder,
        'leecher': leecher
    }

# Function to parse command-line arguments
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Meta-Search-Script for torrents.'
    )
    parser.add_argument('query', metavar='QUERY', type=str,
                        help='the search term')
    parser.add_argument('-s', '--seeder-limit', dest='seeder_limit', type=int,
                        action='store', default=0,
                        help='minimum number of seeders')
    parser.add_argument('-c', '--categories', dest='categories',
                        nargs='*', default=[],
                        help='filter by categories')

    args = parser.parse_args()

    # Convert categories to lowercase for case-insensitive comparison
    for i in range(len(args.categories)):
        args.categories[i] = args.categories[i].casefold()

    return args

# Function to send HTTP GET request and return response text
async def send_query(
    url: str,
    session: ClientSession,
    headers: dict = None
) -> str:
    response = await session.request(method='GET', url=url, headers=headers)
    response.raise_for_status()
    return await response.text(errors='ignore')

# Function to parse torrents from The Pirate Bay
async def parse_thepiratebay(
    args: argparse.Namespace,
    session: ClientSession
) -> None:
    page = 1

    while (True):
        try:
            # Send HTTP GET request to The Pirate Bay
            html = await send_query(urlList['thepiratebay'].format_map({
                'query': quote(args.query),
                'page': page}),
                session
            )
        except (ClientError, HttpProcessingError):
            break

        soup = BeautifulSoup(html, 'html.parser')

        try:
            # Find all torrent rows in the HTML response
            rows = soup.find('div', id='main-content').find_all('tr')[1:-1]
        except AttributeError:
            break

        if len(rows) == 0:
            break

        for row in rows:
            columns = row.find_all('td')
            # Extract category, title, URL, magnet link, seeders, and leechers
            category = sub(r'\W+', ' ', columns[0].find('a').text).strip()
            category = category_list.get(
                category.lower(),
                category_list.get('unknown')
            )
            title = sub(
                '[\n\t]+',
                ' ',
                columns[1].find('div', class_='detName').text
            ).strip()
            url = columns[1].find('a', href=True)['href']
            magnet_link = columns[1].find_all('a')[1]['href']
            seeder = int(columns[2].text.strip())
            leecher = int(columns[3].text.strip())

            # Apply category and seeder filters
            if len(args.categories) > 0:
                if category.casefold() not in args.categories:
                    continue

            if seeder < args.seeder_limit:
                continue

            # Add torrent object to results dictionary
            results[category].append(to_object(
                title=title,
                url=url,
                magnet_link=magnet_link,
                seeder=seeder,
                leecher=leecher
            ))

        page += 1

# Function to parse torrents from 1337x
async def parse_1337x(
    args: argparse.Namespace,
    session: ClientSession
) -> None:
    category_mappings = {
        # Mapping of 1337x category IDs to category names
    }

    page = 1

    while (True):
        try:
            # Send HTTP GET request to 1337x
            html = await send_query(urlList['1337x'].format_map({
                'query': quote(args.query),
                'page': page}),
                session
            )
        except (ClientError, HttpProcessingError):
            break

        soup = BeautifulSoup(html, 'html.parser')

        try:
            # Find all torrent rows in the HTML response
            rows = soup.find('table', class_='table-list').find_all('tr')[1:]
        except AttributeError:
            break

        if len(rows) == 0:
            break

        for row in rows:
            columns = row.find_all('td')
            # Extract category, title, URL, seeders, and leechers
            category = columns[0].find_all('a')[0]['href'].split('/')[2]
            category = category_mappings.get(
                category,
                category_list.get('unknown')
            )
            title = columns[0].find_all('a')[1].text.strip()
            url = 'https://1337x.to' + columns[0].find_all('a')[1]['href']
            seeder = int(columns[1].text.strip())
            leecher = int(columns[2].text.strip())

            # Apply category and seeder filters
            if len(args.categories) > 0:
                if category.casefold() not in args.categories:
                    continue

            if seeder < args.seeder_limit:
                continue

            # Add torrent object to results dictionary
            results[category].append(to_object(
                title=title,
                url=url,
                seeder=seeder,
                leecher=leecher
            ))

        page += 1

# Function to parse torrents from Torlock
async def parse_torlock(args, session: ClientSession) -> None:
    category_mappings = {
        # Mapping of Torlock category IDs to category names
    }

    page = 1

    while (True):
        try:
            # Send HTTP GET request to Torlock
            html = await send_query(urlList['torlock'].format_map({
                'query': quote(args.query),
                'page': page}),
                session
            )
        except (ClientError, HttpProcessingError):
            break

        soup = BeautifulSoup(html, 'html.parser')

        try:
            # Find all torrent rows in the HTML response
            rows = soup.find_all('table')[4].find_all('tr')[1:]
        except AttributeError:
            break

        if len(rows) == 0:
            break

        for row in rows:
            columns = row.find_all('td')
            # Extract category, title, URL, seeders, and leechers
            category = columns[0].find('span')['class'][0]
            category = category_mappings.get(
                category,
                category_list.get('unknown')
            )
            title = columns[0].find('a').text.strip()
            url = 'https://torlock.to' + columns[0].find('a')['href']
            seeder = int(columns[3].text.strip())
            leecher = int(columns[4].text.strip())

            # Apply category and seeder filters
            if len(args.categories) > 0:
                if category.casefold() not in args.categories:
                    continue

            if seeder < args.seeder_limit:
                continue

            # Add torrent object to results dictionary
            results[category].append(to_object(
                title=title,
                url=url,
                seeder=seeder,
                leecher=leecher
            ))

        page += 1

# Main function to run the script
async def run(args):
    task_list = [
        parse_thepiratebay,
        parse_1337x,
        parse_torlock
    ]

    async with ClientSession() as session:
        for i in range(len(task_list)):
            task_list[i] = task_list[i](args, session)
        await asyncio.gather(*task_list)

# Entry point of the script
if __name__ == "__main__":
    args = parse_args()
    asyncio.run(run(args))
    print(json.dumps(results, indent=4))
