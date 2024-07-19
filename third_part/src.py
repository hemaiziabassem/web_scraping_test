import gzip
import json
import os

def read_gzipped_json(file_path):
    with gzip.open(file_path, 'rt', encoding='utf-8') as file:
        content = file.read()
        if not content:
            return None
        return json.loads(content)

def investigate_structure(data, max_depth=3):
    def recursive_investigate(item, depth=0):
        if depth >= max_depth:
            return "..."
        
        if isinstance(item, dict):
            return {k: recursive_investigate(v, depth + 1) for k, v in item.items()}
        elif isinstance(item, list):
            return [recursive_investigate(e, depth + 1) for e in item[:3]]  # Show first 3 elements
        else:
            return type(item).__name__

    return recursive_investigate(data)

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'third_part', 'categories.json.gz')

    try:
        data = read_gzipped_json(input_file_path)
        
        if data is None:
            print(f"The file {input_file_path} is empty.")
            return

        print("File content structure:")
        print(json.dumps(investigate_structure(data), indent=2))

    except FileNotFoundError:
        print(f"Error: The file {input_file_path} was not found.")
    except json.JSONDecodeError as e:
        print(f"Error: The file {input_file_path} contains invalid JSON. Details: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()