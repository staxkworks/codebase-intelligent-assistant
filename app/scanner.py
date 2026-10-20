from pathlib import Path

def find_file_path(folder:str,ignored_dirs : set[str] | None = None)-> list[Path]: # ->is a type hint
    if ignored_dirs is None:
        ignored_dirs ={".venv","__pycache__",".git"}

    root=Path(folder)
    return[
        path for path in root.rglob("*.py")
        if not any(part in ignored_dirs for part in path.parts)
    ]

def count_lines(file_path: Path) -> int:
    """returns the number of lines that are in the given file."""
    return len(file_path.read_text(encoding="utf-8").splitlines())

def scan_files(file_path:str) -> dict[str,str | int]:
    "return a better formatted info about the file"
    return {
        "path": str(file_path),
        "line_count": count_lines(file_path),
        "file_content": file_path.read_text(encoding="utf-8")
    }

def chunk_text(content: str,chunk_size : int = 20) -> list[str]:
    lines=content.splitlines()
    return [
        "/n".join(lines[start:start + chunk_size])
        for start in range(0,len(lines),chunk_size)
    ]

if __name__ =="__main__":
    files=find_file_path("app")
    for file in files:
        info= scan_files(file)
        chunks=chunk_text(info['file_content'])
        print(f"{info['path']}:{info['line_count']} lines and {len(chunks)} chunks")
