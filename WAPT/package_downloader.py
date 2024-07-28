from rich.progress import Progress
import httpx

def download_file(url: str, file_path: str = ''):
    local_filename = file_path or url.split('/')[-1]
    
    with httpx.stream("GET", url) as response:
        file_size = int(response.headers.get("Content-Length", 0))
        response.raise_for_status()
        
        progress = Progress()
        task = progress.add_task('Downloading...', total=file_size)
        
        with open(local_filename, 'wb') as f, progress:
            for chunk in response.iter_bytes(1024):
                f.write(chunk)
                progress.update(task, advance=len(chunk))
    
    return local_filename