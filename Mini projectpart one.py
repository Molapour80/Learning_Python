import os
import sys
import argparse
import datetime
import json

# Tanzimat log
log_file = 'o.json'

def log_command(command, args, outcome):
    """sabta file dar log"""
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "command": command,
        "args": args,
        "outcome": outcome
    }
    try:
        with open(log_file, 'a') as log:
            json.dump(log_entry, log)
            log.write("\n")
    except Exception as e:
        print(f'Error in the coomand {e}')

def list_files(path='.'):
    """show the file"""
    try:
        files = os.listdir(path)
        for file in files:
            print(file)
        log_command('ls', [path], 'Success')
    except FileNotFoundError:
        print(f'command {path} not found')
        log_command('ls', [path], 'Error: Directory not found')

def change_directory(path):
    """change directory"""
    try:
        os.chdir(path)
        print(f'directory to {path} exchangge')
        log_command('cd', [path], 'Success')
    except FileNotFoundError:
        print(f'directory{path} not found')
        log_command('cd', [path], 'Error: Directory not found')

def create_directory(path):
    """Create new directory"""
    try:
        os.mkdir(path)
        print(f'directory{path} created!!!')
        log_command('mkdir', [path], 'Success')
    except FileExistsError:
        print(f'directory{path} before exit.')
        log_command('mkdir', [path], 'Error: Directory already exists')

def remove_directory(path):
    """Removed  directory"""
    try:
        os.rmdir(path)
        print(f'command {path} removed!!')
        log_command('rmdir', [path], 'Success')
    except FileNotFoundError:
        print(f'command {path} not found.')
        log_command('rmdir', [path], 'Error: Directory not found')
    except OSError:
        print(f'command{path} employ')
        log_command('rmdir', [path], 'Error: Directory not empty')

def remove_file(file):
    """remove """
    try:
        os.remove(file)
        print(f'file{file} removed!!')
        log_command('rm', [file], 'Success')
    except FileNotFoundError:
        print(f'file{file} not found')
        log_command('rm', [file], 'Error: File not found')
    



def copy(source, destination):
    """Copy the  file """
    try:
        if os.path.isfile(source):
            with open(source, 'rb') as src_file:
                with open(destination, 'wb') as dst_file:
                    dst_file.write(src_file.read())
            print(f'copy{source}to{destination} donnnnnn')
            log_command('cp', [source, destination], 'Success')
        else:
            print(f'file{source} find')
            log_command('cp', [source, destination], 'Error: Source file not found')
    except Exception as e:
        print(f'Error in the  {e}')
        log_command('cp', [source, destination], f'Error: {e}')

def move(source, destination):
    """move the file"""
    try:
        os.rename(source, destination)
        print(f'move{source} to {destination} don')
        log_command('mv', [source, destination], 'Success')
    except Exception as e:
        print(f'Error in the moveing. {e}')
        log_command('mv', [source, destination], f'Error: {e}')

def find(path, pattern):
    """search the file"""
    matches = []
    for root, dirs, files in os.walk(path):
        for name in files + dirs:
            if pattern in name:
                matches.append(os.path.join(root, name))
    print("founded!!!!")
    for match in matches:
        print(match)
    log_command('find', [path, pattern], 'Success')

def cat(file):
    """show in the file"""
    try:
        with open(file, 'r') as f:
            content = f.read()
            print(content)
        log_command('cat', [file], 'Success')
    except FileNotFoundError:
        print(f"file's{file} not found")
        log_command('cat', [file], 'Error: File not found')

def main():
    """main cli."""
    parser = argparse.ArgumentParser(description='CLI Tool for File and Directory Management')
    
  
    parser.add_argument('command', help='Command to execute (ls, cd, mkdir, rmdir, rm, cp, mv, find, cat)', nargs='*')
    
    
    args = parser.parse_args()

    # check your  command 
    if not args.command:
        print("please entar your command")
        parser.print_help()
        sys.exit(1)

    
    input_command = ' '.join(args.command)
    command_parts = input_command.split()

    if command_parts[0] == 'ls':
        list_files(command_parts[1] if len(command_parts) > 1 else '.')
    elif command_parts[0] == 'cd':
        change_directory(command_parts[1])
    elif command_parts[0] == 'mkdir':
        create_directory(command_parts[1])
    elif command_parts[0] == 'rmdir':
        remove_directory(command_parts[1])
    elif command_parts[0] == 'rm':
        remove_file(command_parts[1])
    elif command_parts[0] == 'cp':
        copy(command_parts[1], command_parts[2])
    elif command_parts[0] == 'mv':
        move(command_parts[1], command_parts[2])
    elif command_parts[0] == 'find':
        find(command_parts[1], command_parts[2])
    elif command_parts[0] == 'cat':
        cat(command_parts[1])
    else:
        print('Command not found')


main()