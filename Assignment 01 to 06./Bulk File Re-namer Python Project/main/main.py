import os

def rename_files_in_directory(directory, prefix='', suffix='', replace_str=None, start_number=1):
    try:
        # Get the list of files in the directory
        files = os.listdir(directory)
        
        # Filter out directories, keeping only files
        files = [f for f in files if os.path.isfile(os.path.join(directory, f))]

        if not files:
            print(f"No files found in the directory: {directory}")
            return
        
        # Loop through the files and rename them
        for index, file in enumerate(files, start=start_number):
            # Get the file's current name and extension
            file_name, file_extension = os.path.splitext(file)
            
            # Optionally replace a string in the file name
            if replace_str:
                file_name = file_name.replace(replace_str, '')
            
            # Construct the new name
            new_name = f"{prefix}{file_name}{suffix}{file_extension}"
            
            # Ensure the new name doesn't exist already
            new_file_path = os.path.join(directory, new_name)
            old_file_path = os.path.join(directory, file)
            
            if new_file_path != old_file_path:
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {file} -> {new_name}")
            else:
                print(f"Skipping: {file} (No change needed)")
                
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Ask the user for input
    directory = input("Enter the directory path to rename files: ").strip()
    
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return
    
    # Ask for renaming options
    prefix = input("Enter prefix to add (leave empty if none): ").strip()
    suffix = input("Enter suffix to add (leave empty if none): ").strip()
    replace_str = input("Enter a string to replace in file names (leave empty if none): ").strip() or None
    start_number = input("Enter the starting number for sequential renaming (default is 1): ").strip()
    start_number = int(start_number) if start_number else 1
    
    # Perform the renaming operation
    rename_files_in_directory(directory, prefix, suffix, replace_str, start_number)

if __name__ == "__main__":
    main()
