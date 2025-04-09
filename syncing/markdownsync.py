"""
Summary: 
This simple script will help sync files
from different sources to given targets.

Details:
This script will go through the given config yaml
and will update the target folder with the source one.
Essentially, it will:
- Try to map source file to target.
- Force update target.
- Apply rules to hide sensitive information / give correct format.
- Copy unexisting files.

Input:
    config: yaml config containing necessary information.


Status: 
NOT TESTED!
"""

import argparse
import logger
import pathlib
import re
import shutil
import yaml
import os

FILE_PATH = pathlib.Path(__file__)

def define_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Copy files from source to destination using a YAML config."
    )
    parser.add_argument(
        '--config', required=True, help='Path to the YAML config file'
    )
    return parser

def target_path(path: str) -> pathlib.Path | None:
    pass
    

def copy_files(config_path):
    with open(config_path, 'r', encoding="utf-8") as file:
        config = yaml.safe_load(file)

    for sync_path in config['sync']:
        # Check if the path is valid
        try:
            if sync_path['type'] == "this":
                # Check if it exists
                sync_target = FILE_PATH.parent.parent / "site" / sync_path['target']
                assert sync_target.exists(), f"Your sync target doesn't exists\n{sync_target}"
                # Gather files according to filter
                sync_source_files = os.listdir(sync_path['path'])
                sync_target_files = os.listdir(sync_target)
                assert len(sync_source_files), f"There are no source files to sync!"
                # Both exists -> Update target
                # -> grab original
                # -> clean it with source
                # -> compare it to target
                # --> target mathes -> no update
                # --> target mismatch -> force update
                # ---> leave header as is
                for markdown_file in sync_source_files:
                    # Grab original file
                    with open(pathlib.Path(sync_path['path']) / markdown_file, 'r', encoding='utf-8') as f:
                        markdown_text = f.read()
                        
                    # Apply rules 
                
                # Only source -> Copy
                # --> target doesn't exists -> add
                                
                # Only target exists -> Leave as is, but warm user!
                # -> add to log

                
        except:
            pass
            

        
    # source = config.get("source")
    # destination = config.get("destination")

    # if not source or not destination:
    #     print("Invalid config: must include 'source' and 'destination'")
    #     return

    # if not os.path.exists(destination):
    #     os.makedirs(destination)

    # for filename in os.listdir(source):
    #     full_file_name = os.path.join(source, filename)
    #     if os.path.isfile(full_file_name):
    #         shutil.copy(full_file_name, destination)
    #         print(f"Copied: {filename}")
    
    pass

def main():
    parser = define_argparse()
    args = parser.parse_args()
    copy_files(args.config)

if __name__ == '__main__':
    main()