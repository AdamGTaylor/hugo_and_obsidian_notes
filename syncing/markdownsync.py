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
import pathlib
import re
import shutil
import os

import textwrap
import yaml
import logger

import utils.cleaning_rule_handling as crh

FILE_PATH = pathlib.Path(__file__)

def define_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Copy files from source to destination using a YAML config."
    )
    parser.add_argument(
        '--config', required=True, help='Path to the YAML config file'
    )
    return parser

# def target_path(path: str) -> pathlib.Path | None:
#     pass
    

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
                matched = set(sync_source_files).intersection(set(sync_target_files))
                only_source = set(sync_source_files).difference(matched)
                only_target = set(sync_target_files).difference(matched)
                assert len(sync_source_files), f"There are no source files to sync!"
                # Both exists -> Update target
                # -> grab original
                # -> clean it with source
                # -> compare it to target
                # --> target mathes -> no update
                # --> target mismatch -> force update
                # ---> leave header as is
                for markdown_file in matched:
                    # Grab original file
                    with open(pathlib.Path(sync_path['path']) / markdown_file, 'r', encoding='utf-8') as f:
                        markdown_text = f.read()
                        
                    if not len(markdown_text):
                        # Why would you sync an empty file?
                        continue
                        
                    # Apply rules 
                    for rule in sync_path['rules']:
                        # Cursed way of calling a func
                        markdown_text_redacted = getattr(crh, rule)(markdown_text)
                        
                    # Markdown cleaned, try to load target
                    with open(sync_target / markdown_file, 'r', encoding='utf-8') as f:
                        markdown_text_target = f.read()
                    
                    t_header_exists = markdown_text_target.startswith("---\ntitle:")
                    s_header_exists = markdown_text_redacted.startswith("---\ntitle:")
                    
                    # Compare content
                    t_content = markdown_text_target if not t_header_exists else "---\n".join(markdown_text_target.split("---\n")[2:])
                    s_content = markdown_text_redacted if not s_header_exists else "---\n".join(markdown_text_redacted.split("---\n")[2:])
                    
                    if t_content == s_content:
                        # Just leave everything as is
                        continue
                    else:
                        header = ''
                        if s_header_exists:
                            # Nothing to do here
                            pass
                        elif t_header_exists:
                            # Add it's header to source
                            header = markdown_text_target.split("---\n")[1]
                            header = "---\n" + header + "---\n"
                        else:
                            # Add default stuff
                            header = textwrap.dedent(
                                f'''
                                ---
                                title: "{markdown_file.split(".")[0]}"
                                date: 
                                draft: false
                                tags: []
                                categories: {sync_path['target'].split("/")[-1]}
                                ---
                                '''[1:]            # It leaves the first newline character in
                            )
                            
                        # Save it
                        content_to_be_saved = header + markdown_text_redacted
                        with open(sync_target / markdown_file, 'w', encoding="utf-8") as f:
                            f.write(content_to_be_saved)
                            f.close()
                
                # Only source -> Copy
                # --> target doesn't exists -> add
                for markdown_file in only_source:
                    # Grab original file
                    with open(pathlib.Path(sync_path['path']) / markdown_file, 'r', encoding='utf-8') as f:
                        markdown_text = f.read()
                        
                    markdown_text_redacted = markdown_text
                    
                    # Apply rules 
                    for rule in sync_path['rules']:
                        # Cursed way of calling a func
                        markdown_text_redacted = getattr(crh, rule)(markdown_text)
                    
                    t_header_exists = markdown_text_redacted.startswith("---\ntitle:")
                    
                    if not t_header_exists:
                        header = textwrap.dedent(
                            f'''
                            ---
                            title: "{markdown_file.split(".")[0]}"
                            date: 
                            draft: false
                            tags: []
                            categories: {sync_path['target'].split("/")[-1]}
                            ---
                            '''[1:]            # It leaves the first newline character in
                        )

                        markdown_text_redacted = header + markdown_text_redacted
                    
                    with open(sync_target / markdown_file, 'w', encoding="utf-8") as f:
                        f.write(markdown_text_redacted)
                        f.close()
                                
                # Only target exists -> Leave as is, but warm user!
                # -> add to log
                if len(only_target) > 0:
                    print("There are files that have only source file!")
                    print(f"Under: {sync_path['path']}")
                    print(f"Files are: {only_target}")
                
        except Exception as e:
            # TODO: better exception handling here
            print(f"Please look into this issue: {e}")
            pass
    
    print("Finished!")

def main():
    parser = define_argparse()
    args = parser.parse_args()
    print("Started!")
    copy_files(args.config)

if __name__ == '__main__':
    main()