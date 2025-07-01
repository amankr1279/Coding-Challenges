from shell_implement import Shell_Imp
import sys

sys.path.append("../")
from logger import setup_logger

def parser(cmd: str, shell: Shell_Imp):
    cmd = cmd.strip()
    supported_cmds = set(shell.supported_cmds)
    main_cmd = cmd.split(" ")[0]
    if main_cmd not in supported_cmds:
        print("No such file or directory (os error 2)")
        return
    
    if main_cmd == "help":
        print(f"Supported Commands : {shell.supported_cmds}.")
    elif main_cmd == "ls":
        shell.list_dir(cmd)
    elif main_cmd == "cat":
        shell.cat_file(cmd)
    elif main_cmd == "pwd":
        shell.print_dir(cmd)
    elif main_cmd == "cd":
        shell.change_dir(cmd)
    else:
        shell.print_history()
        

if __name__ == "__main__":
    shell = Shell_Imp()
    print(f"Supported Commands : {shell.supported_cmds}. Type `help` for seeing this again.")
    logger = setup_logger("shell_logger")
    shell.set_context(logger)
    while True:
        cmd = input("ccsh> ")
        if "exit" in cmd:
            print("Exiting the shell...👋")
            break
        logger.debug(f"Command : {cmd}")
        parser(cmd, shell)
