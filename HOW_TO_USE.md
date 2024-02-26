# How to Use the Script

1. **Clone the Repository**: First, clone or download the repository containing the script to your local machine.

   ```bash
   git clone https://github.com/arindal1/torrentous.git
   ```

2. **Navigate to the Directory**: Enter the project directory.

   ```bash
   cd torrentous
   ```

3. **Install Dependencies**: Install the required dependencies using pip.

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script**: Execute the script with the desired search query and optional arguments.

   ```bash
   python torrent_meta_search.py <query> [-s SEEDER_LIMIT] [-c CATEGORIES [CATEGORIES ...]]
   ```

   - `<query>`: The search term for torrents.
   - `-s SEEDER_LIMIT, --seeder-limit SEEDER_LIMIT`: Specify the minimum number of seeders for filtering torrents (default is 0).
   - `-c CATEGORIES [CATEGORIES ...], --categories CATEGORIES [CATEGORIES ...]`: Specify one or more categories to filter torrents (e.g., movies, music).

### Possible Commands and Examples

- **Basic Usage**: Search for torrents using a query term.

  ```bash
  python torrent_meta_search.py "ubuntu"
  ```

- **Filter by Seeders**: Specify a minimum number of seeders for filtering torrents.

  ```bash
  python torrent_meta_search.py "ubuntu" -s 10
  ```

- **Filter by Categories**: Filter torrents by one or more categories.

  ```bash
  python torrent_meta_search.py "ubuntu" -c applications games
  ```

- **Combining Filters**: Combine seeders and categories filters.

  ```bash
  python torrent_meta_search.py "ubuntu" -s 10 -c applications games
  ```

- **Example Output**: The script outputs the results in JSON format.

  ```json
  {
      "Movies": [
          {
              "title": "Ubuntu - 20.04.3 LTS - 64bit 2021-08-16",
              "url": "https://thepiratebay.org/torrent/49781529/Ubuntu_-_20.04.3_LTS_-_64bit_2021-08-16",
              "magnet-link": "magnet:?xt=urn:btih:9C3ECB780CD8E0B4F70C98DFEA6D7EFD2862FB0E&dn=Ubuntu+-+20.04.3+LTS+-+64bit+2021-08-16&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A1337%2Fannounce",
              "seeder": 304,
              "leecher": 94
          }
      ],
      "Applications": [
          {
              "title": "ubuntu-20 04 4-desktop-amd64",
              "url": "https://1337x.to/torrent/5157212/ubuntu-20-04-4-desktop-amd64/",
              "seeder": 256,
              "leecher": 87
          }
      ]
  }
  ```

### Additional Notes

- Ensure that you have a stable internet connection to perform the torrent search.
- Depending on the number of seeders and the size of the torrent database, the search may take some time to complete.
- Make sure to comply with the terms of service of the torrent websites and any legal regulations regarding torrent usage in your region.

By following these steps and examples, you can effectively use the torrent meta-search script to find torrents based on your preferences and requirements.
