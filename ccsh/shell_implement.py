import os

class Shell_Imp:
    
    def __init__(self):
        self.history = []
        self.prev_dir = os.getcwd()
        self.curr_dir = os.getcwd()
    
    def list_dir(self, cmd : str):
        '''
        Lists all files and folders in given directory.
        Supports ls, ls -la and ls <flag or no flag> <directory>
        '''
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
                print("Incorrect way")
                return
            self._list_dir(args[2], "a" in args[1], "l" in args[1])
        print()

    def _list_dir(self, dir_path : str, dot_file_flag = False, pretty_flag = False):
        full_path = ""
        if dir_path.startswith("/"):
            full_path = dir_path
        else:
            full_path = self.curr_dir + "/" + dir_path
        
        separator = "  " if not pretty_flag else "\n"
        if os.path.exists(full_path):
            if os.path.isfile(full_path):
                print(full_path, end=separator)
            else:
                for f in os.listdir(dir_path):
                    if (dot_file_flag and f.startswith(".")) or not f.startswith("."):
                        print(f, end=separator)
        else:
            print("Incorrect way", end=separator)

    def cat_file(self, cmd : str):
        pass

    def print_dir(self, cmd : str):
        '''Prints current directory path'''
        args = cmd.split(" ")
        out = ""
        if len(args) == 1:
            out = self.curr_dir.replace("//", "/")
        elif len(args) == 2:
            out = "Incorrect way for pwd"
        print(out)
        self.history.append(cmd)

    def change_dir(self, cmd : str):
        '''
        Does not handle cases like `cd ../ or cd ./`
        '''
        options = set([".", "..", "-"])
        out = ""
        args = cmd.split(" ")
        if len(args) == 1:
            out = "/Users/amankumar"
        elif len(args) == 2:
            if args[1] in options:
                cd_opt = args[1]
                if cd_opt == ".":
                    out = self.curr_dir
                elif cd_opt == "..":
                    words = self.curr_dir.split("/")[:-1]
                    out = "/"
                    for word in words:
                        out = out + word + "/"
                else:
                    out = self.prev_dir
            else:
                target_dir = args[1]
                if target_dir.startswith("/"):
                    out = target_dir
                for dir in os.listdir(self.curr_dir):
                    if dir == target_dir and os.path.isdir(self.curr_dir + "/" + dir):
                        out = self.curr_dir + "/" + target_dir
        if out:
            self.prev_dir = self.curr_dir
            self.curr_dir = out    
        else:
            print("Incorrect way") 
        self.history.append(cmd)  

    def print_history(self):
        for i, cmd in enumerate(self.history):
            print(f"{i}  {cmd}")
    