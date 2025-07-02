import os
from logging import Logger

class Shell_Imp:
    
    def __init__(self):
        self.history = []
        self.prev_dir = os.getcwd()
        self.curr_dir = os.getcwd()
        self.supported_cmds = ["ls", "cat", "pwd", "cd", "history", "help"]
        
    def set_context(self, logger : Logger):
        self.logger = logger
    
    def list_dir(self, cmd : str):
        '''
        Lists all files and folders in given directory.
        Supports ls, ls -la and ls <flag or no flag> <directory>
        '''
        self.history.append(cmd)
        args = cmd.split(" ")
        options = ["-l", "-la"]
        if len(args) == 1:
            self._list_dir(self.curr_dir)
        elif len(args) == 2:
            if args[1] in options:
                self._list_dir(self.curr_dir, True, True)
            else:
                target_resource = args[1]
                self._list_dir(target_resource)
        elif len(args) == 3:
            if args[1] not in options:
                print(f"ERROR: The format is not correct for given cmd: {cmd}")
                return
            self._list_dir(args[2], "a" in args[1], "l" in args[1])
        print()

    def _list_dir(self, dir_path : str, dot_file_flag = False, pretty_flag = False):
        full_path = ""
        if dir_path.startswith("/"):
            full_path = dir_path
        else:
            full_path = self.curr_dir + "/" + dir_path
        
        self.logger.debug(full_path)
        separator = "  " if not pretty_flag else "\n"
        if os.path.exists(full_path):
            if os.path.isfile(full_path):
                print(full_path, end=separator)
            else:
                for f in os.listdir(dir_path):
                    if (dot_file_flag and f.startswith(".")) or not f.startswith("."):
                        print(f, end=separator)
        else:
            print(f"ERROR: The file path is incorrect : {full_path}", end=separator)

    def cat_file(self, cmd : str):
        '''Displays the contents a file'''
        self.history.append(cmd)
        args = self._space_separated_name_handler(cmd)
        self.logger.debug(f"Args : {args}")
        if len(args) != 2:
            print("ERROR: invalid number of args given")
            return
        
        file_name = args[1]
        if os.path.exists(file_name) and os.path.isfile(file_name):
            with open(file_name, "r") as f:
                for line in f:
                    print(line.strip())
        else:
            print("ERROR: File path is invalid")

    def print_dir(self, cmd : str):
        '''Prints current directory path'''
        args = cmd.split(" ")
        out = ""
        if len(args) == 1:
            out = self.curr_dir.replace("//", "/")
        elif len(args) == 2:
            out = f"ERROR: Incorrect cmd: {cmd} for pwd"
        print(out)
        self.history.append(cmd)

    def change_dir(self, cmd : str):
        '''
        Changes directory.
        Does not handle cases like `cd ../ or cd ./`
        '''
        self.history.append(cmd)
        options = set([".", "..", "-"])
        out = ""
        args = self._space_separated_name_handler(cmd)
        self.logger.debug(args)
        if len(args) == 1:
            out = "/Users/amankumar"
        elif len(args) == 2:
            if args[1] in options:
                cd_opt = args[1]
                if cd_opt == ".":
                    out = self.curr_dir
                elif cd_opt == "..":
                    words = list(filter(None, self.curr_dir.split("/")))
                    words.pop()
                    self.logger.debug(f"words : {words}")
                    out = "/"
                    for word in words:
                        if word:
                            out = out + word + "/"
                    out = out[:-1]
                else:
                    out = self.prev_dir
            else:
                target_dir = args[1]
                if target_dir.startswith("/"):
                    out = target_dir
                for dir in os.listdir(self.curr_dir):
                    self.logger.debug(f"Dir : {dir}")
                    if dir == target_dir and os.path.isdir(self.curr_dir + "/" + dir):
                        out = self.curr_dir + "/" + target_dir
                        
        if out and os.path.exists(out):
            self.logger.debug(f"Result : {out}")
            self.prev_dir = self.curr_dir
            self.curr_dir = out    
        else:
            self.logger.debug(f"ERROR: The command's format is invalid or file does not exist") 

    def _space_separated_name_handler(self, cmd : str):
        '''If the name of the file or directory contains 1 space separated name then it is handled here'''
        args = cmd.split(" ")
        self.logger.debug(f"Args before resolving: {args}")
        for i, arg in enumerate(args):
            if '"' in arg:
                x = arg + " "
                i += 1
                while i < len(args):
                    x = x + args[i] + " "
                    if '"' in args[i]:
                        break
                    i += 1
                args[1] = x.strip().replace('"', '')
                self.logger.debug("After resolving, args[1] : " + args[1])
                args = args[:2]
                break
        return args 

    def print_history(self):
        for i, cmd in enumerate(self.history):
            print(f"{i}  {cmd}")
    
    def help(self):
        '''Displays all supported commands in the shell'''
        print(f"Supported Commands : {self.supported_cmds}.")
        self.history.append("help")
        
    def sigint_handler(self, signum, frame ):
        print("\npress (Enter) key to release")

