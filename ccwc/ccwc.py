import io
import optparse
import sys


class CCWC:
    def __init__(self) -> None:
        self.line_cnt = 0
        self.word_cnt = 0
        self.char_cnt = 0
        self.byte_cnt = 0
        
    def generate_statistics(self,f: io.BufferedReader):
        for line in f.readlines():
            self.line_cnt += 1
            self.char_cnt += len(line.decode())
            self.word_cnt += len(line.split())
            self.byte_cnt += len(line)                        

if __name__ == "__main__":
        
    parser = optparse.OptionParser(
        description="For counting words in a file"
    )
    
    parser.add_option("-l", 
                      dest = "lines", 
                      action = "store_true",
                      help="Count number of lines", 
                      default = False)
    parser.add_option("-c", 
                      dest = "bytes", 
                      action = "store_true",
                      help="Count number of bytes",
                      default = False)
    parser.add_option("-m",
                      dest = "characters", 
                      action = "store_true",
                      help="Count number of characters",
                      default = False)
    parser.add_option("-w", 
                      dest = "words", 
                      action = "store_true",
                      help="Count number of words",
                      default = False)
    
    (options, args) = parser.parse_args()
    
    isFile = sys.stdin.isatty()
    if not isFile:
        contents = sys.stdin.buffer
    else:
        if len(sys.argv) < 2:
            print(sys.argv)
            print("Need file name or path")
            exit(1)
        file_path = sys.argv[-1]
        contents = open(file_path,"rb")

    ccwc = CCWC()
    ccwc.generate_statistics(contents)
    
    LIMIT = 2 if isFile else 1
    if len(sys.argv) <= LIMIT:
        print(f"    {ccwc.line_cnt}    {ccwc.word_cnt}    {ccwc.byte_cnt}")
        exit(0)
    if options.lines:
        print(ccwc.line_cnt)
    if options.words:
        print(ccwc.word_cnt)
    if options.bytes:
        print(ccwc.byte_cnt)
    if options.characters:
        print(ccwc.char_cnt)
