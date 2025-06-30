from shell_implement import Shell_Imp

def parser(cmd: str, shell: Shell_Imp):
    cmd = cmd.strip()
    supported_cmds = set(["ls", "cat", "pwd", "cd", "history"])
    main_cmd = cmd.split(" ")[0]
    if main_cmd not in supported_cmds:
        print("No such file or directory (os error 2)")
        return
    
    if main_cmd == "ls":
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
    print(f"Supported Commands : {["ls", "cat", "pwd", "cd", "history"]}")
    while True:
        cmd = input("ccsh> ")
        if "exit" in cmd:
            print("Exiting the shell...👋")
            break
        parser(cmd, shell)