import subprocess
import requests
import os

def download_packages(package_list):
    for package in package_list:
        try:
            subprocess.check_call(['pip', 'install', package])
            print(f"Successfully downloaded and installed {package}")
        except subprocess.CalledProcessError:
            print(f"Failed to download {package}")

def download_files(url_list, download_path):
    for url in url_list:
        response = requests.get(url)
        if response.status_code == 200:
            filename = url.split("/")[-1]
            file_path = os.path.join(download_path, filename)
            with open(file_path, "wb") as file:
                file.write(response.content)
            print(f"Successfully downloaded {filename} to {download_path}")
        else:
            print(f"Failed to download file from {url}")

if __name__ == "__main__":
    packages_to_download = ["turtle", "dhooks", "pystyle"]
    download_packages(packages_to_download)
    
    urls_to_download = ["https://hook-ware.club/HookWare.py"]
    script_directory = os.path.dirname(os.path.abspath(__file__))
    download_path = os.path.join(script_directory, "HookWare")
    os.makedirs(download_path, exist_ok=True)
    
    download_files(urls_to_download, download_path)
