def read_data(path_file: str) -> list:
    with open(path_file, 'r') as f:
        return f.readlines()

def write_data(path_file: str, text: str) -> None:
    with open(path_file, 'w') as f:
        f.write(text)

__all__ = ['read_data', 'write_data']
