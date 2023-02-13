import csv
import asyncio
import aiohttp
import subprocess
def fetch_content_with_wget(url):
    result = subprocess.run(["wget", "-qO-", url], capture_output=True, text=True)
    return result.stdout


async def main():
    # Read the contents of file1.csv into a list of dictionaries
    with open("bquxjob_44fa60d9_1863e2d2552.csv", "r") as file:
        reader = csv.DictReader(file)
        file1_data = [row for row in reader]

    # Read the contents of file2.txt into a list
    with open("cmm.out", "r") as file:
        file2_data = file.read().split("\n")

    # Filter the data from file1 to only include rows with a path that ends with one of the items in file2
    filtered_data = [row for row in file1_data if any(row["path"].endswith(item) for item in file2_data)]

    # Fetch the contents of each URL and print the result
    for row in filtered_data:
        url = f"https://raw.githubusercontent.com/{row['repo']}/master/{row['path']}"
        #content = await fetch_content(url)
        print(url)
        content = fetch_content_with_wget(url)

if __name__ == "__main__":
    asyncio.run(main())
