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
python torrentous.py <query> [-s SEEDER_LIMIT] [-c CATEGORIES [CATEGORIES ...]]
```

- `<query>`: The search term for torrents.
- `-s SEEDER_LIMIT, --seeder-limit SEEDER_LIMIT`: Specify the minimum number of seeders for filtering torrents (default is 0).
- `-c CATEGORIES [CATEGORIES ...], --categories CATEGORIES [CATEGORIES ...]`: Specify one or more categories to filter torrents (e.g., movies, music).

Example:

```bash
python torrentous.py "ubuntu" -s 10 -c applications games
```

Read [HOW_TO_USE](HOW_TO_USE.md) for a detailed commands and examples.

## Supported Torrent Websites

- **The Pirate Bay**: [thepiratebay.org](https://thepiratebay.org)
- **1337x**: [1337x.to](https://1337x.to)
- **Torlock**: [torlock.com](https://torlock.com)
- **RARBG**: [rarbg.to](https://rarbg.to/)
- **YTS**: [yts.mx](https://yts.mx/)
- **Torrentz2**: [torrentz2.eu](https://torrentz2.eu/)
- **EZTV**: [eztv.io](https://eztv.io/)

## Note

If the script returns an empty JSON object `{}` and then stops without any further output, it indicates that the script didn't find any torrents matching the provided query or filters or the sites that the script uses are down or inaccessible. Here are a few steps to troubleshoot and potentially resolve the issue:

1. **Verify Internet Connection**: Ensure that your internet connection is stable and functioning properly. The script relies on internet access to fetch search results from torrent websites.
2. **Check Query Term**: Double-check the query term you provided when running the script. Make sure it's correctly spelled and represents what you intend to search for.
3. **Test Torrent Websites**: Manually visit the torrent websites (The Pirate Bay, 1337x, Torlock) in your web browser to verify that they are accessible and operational. Sometimes, websites may be down or experiencing issues, which can affect the script's ability to fetch results.

Additionally, keep in mind that accessing and using torrent sites may be subject to **legal regulations** in your region, so make sure to comply with any applicable laws.

## Contact

If you have any questions or suggestions related to this project, you can reach out to me at:

- GitHub: [arindal1](https://github.com/arindal1)
- LinkedIn: [arindalchar](https://www.linkedin.com/arindalchar/)
- Twitter: [arindal_17](https://twitter.com/arindal_17)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script was inspired by the need for a simple meta-search tool for torrents.
- Special thanks to the developers of the aiohttp and BeautifulSoup libraries.
