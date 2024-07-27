from rich.progress import Progress
import requests

def download_file(url: str, file_path=''):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        file_size = int(r.headers.get("Content-Length", 0))
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            progress = Progress()
            task = progress.add_task('Downloading...', total=file_size)
            with progress:
                for chunk in r.iter_content(4096):
                    f.write(chunk)
                    progress.update(task, advance=len(chunk))
    return local_filename
