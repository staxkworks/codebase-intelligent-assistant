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

if __name__ =="__main__":
    files=find_file_path("app")
    for file in files:
        print(f"{file}:{count_lines(file)} lines")
