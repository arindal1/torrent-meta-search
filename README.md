# Torrentous - A Torrent Meta-Search Script

This is a Python script that performs meta-search for torrents across multiple torrent websites. It allows users to search for torrents based on a query term and apply filters such as minimum seeders and categories.

## Features

- **Meta-Search**: The script concurrently searches multiple torrent websites for torrents based on the provided query.
- **Filtering**: Users can specify minimum seeders and filter torrents by categories such as movies, music, games, etc.
- **Asynchronous**: Asynchronous programming is used to perform concurrent HTTP requests, improving efficiency.
- **JSON Output**: Results are formatted and printed in JSON format for easy consumption.

## Prerequisites

- Python 3.x
- pip (Python package manager)
- aiohttp
- beautifulsoup4

## Installation

1. Clone or download the repository to your local machine.

```bash
git clone https://github.com/arindal1/torrentous.git
```

2. Navigate to the project directory.

```bash
cd torrentous
```

3. Install dependencies using pip.

```bash
pip install -r requirements.txt
```

## Usage

Run the script with the desired search query and optional arguments.

```bash
python torrent_meta_search.py <query> [-s SEEDER_LIMIT] [-c CATEGORIES [CATEGORIES ...]]
```

- `<query>`: The search term for torrents.
- `-s SEEDER_LIMIT, --seeder-limit SEEDER_LIMIT`: Specify the minimum number of seeders for filtering torrents (default is 0).
- `-c CATEGORIES [CATEGORIES ...], --categories CATEGORIES [CATEGORIES ...]`: Specify one or more categories to filter torrents (e.g., movies, music).

Example:

```bash
python torrent_meta_search.py "ubuntu" -s 10 -c applications games
```

## Supported Torrent Websites

- **The Pirate Bay**: [thepiratebay.org](https://thepiratebay.org)
- **1337x**: [1337x.to](https://1337x.to)
- **Torlock**: [torlock.com](https://torlock.com)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script was inspired by the need for a simple meta-search tool for torrents.
- Special thanks to the developers of the aiohttp and BeautifulSoup libraries.
