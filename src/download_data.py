import hashlib 
import urllib.request

from config import DATA_URL, EXPECTED_ROWS, RAW_DATA_FILE




def file_sha256(path):
    digest = hashlib.sha256()
    with open(path , "rb") as f:
        chunk = f.read(1024 * 1024)
        while chunk: 
            digest.update(chunk)
            chunk = f.read(1024 * 1024)
    return digest.hexdigest()


def count_data_rows(path):
    number_of_lines = 0
    with open(path, "r", encoding="utf-8") as f:
        for _line in f:
            number_of_lines += 1
    return number_of_lines - 1

def main():
    RAW_DATA_FILE.parent.mkdir(parents=True, exit_ok=True)
    if RAW_DATA_FILE.exists():
        print(f"File already exists, skipping download : {RAW_DATA_FILE}")
    else:
        print(f"Downloading {DATA_URL}")
        urllib.request.urlretrieve(DATA_URL,RAW_DATA_FILE)
        print(f"Saved to {RAW_DATA_FILE}")


rows = count_data_rows(RAW_DATA_FILE)
size = RAW_DATA_FILE.stat().st_size
print(f"size: {size:,} bytes")
print(f"Rows: {rows:,} (expected {EXPECTED_ROWS:,})")
print(f"SHA-256:{file_sha256(RAW_DATA_FILE)}")


if rows != EXPECTED_ROWS:
    raise ValueError("Row count is not what we expected . The file may be incomplete.")



if __name__ == "__main__":
    main()