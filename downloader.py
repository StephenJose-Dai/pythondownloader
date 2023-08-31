import os
import requests
import json
from tqdm import tqdm
from urllib.parse import urlparse

def download_file(url, download_number):
    filename = os.path.basename(urlparse(url).path)
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("content-length", 0))
    with tqdm(total=total_size, unit="B", unit_scale=True, unit_divisor=1024, bar_format="{desc} {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]") as progress_bar:
        for data in response.iter_content(chunk_size=8192):
            progress_bar.update(len(data))
            progress_bar.set_description(f"[ {download_number} ] {filename}", refresh=False)

    return {"Download_number": download_number, "Filename": filename, "status": "Completed"}

def main():
    download_url = input("Enter the download URL: ")
    num_downloads = int(input("Enter the number of times to download: "))

    results = []
    for download_number in range(1, num_downloads + 1):
        result = download_file(download_url, download_number)
        results.append(result)

    with open("jieguo.json", "w") as json_file:
        json.dump(results, json_file, indent=4)

if __name__ == "__main__":
    main()
