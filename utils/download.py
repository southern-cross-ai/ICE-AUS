import argparse
import os
import zipfile

import requests


def download(save_path=None, unzip=True):
    """Download and unzip the dataset.

    Args:
        save_path (str, optional): The root path to save the file. If the save_path is None, 
            the file will be saved in the current directory. Defaults to None.
        unzip (bool, optional): Whether to unzip downloaded files. Defaults to True.
    """
    # WARNING: DO NOT CHANGE THE FOLLOWING CODE
    url = 'https://figshare.mq.edu.au/ndownloader/files/43778337'
    file_name = r'ICE Corpus.zip'

    # Send a GET request to the URL
    response = requests.get(url)
    # Specify the local file path where you want to save the ZIP file
    if save_path:
        file_path = save_path + '/' + file_name
        # Write the content of the response to a file
        if not os.path.exists(save_path):
            os.mkdir(save_path)
    else:
        file_path = file_name
    with open(file_path, 'wb') as f:
        f.write(response.content)
    print(f"File downloaded and saved as {file_path}")
    # Unzip files if needed
    if unzip:
        with zipfile.ZipFile(file_path, 'r') as f:
            # Extract all the contents into the directory
            f.extractall(file_path.split('.')[0])
        print(f"File is unzipped and saved as {file_path.split('.')[0]}")


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(
        description="Download a file and optionally unzip it.")
    parser.add_argument(
        "--save_path", help="Path to save the downloaded file.")
    parser.add_argument("--unzip", action="store_true",
                        help="Unzip the file if it's a zip archive.")
    args = parser.parse_args()
    # Download, unzip and save under the directory dataset
    download(save_path=args.save_path, unzip=args.unzip)
