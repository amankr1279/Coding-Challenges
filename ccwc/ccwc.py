import argparse
import io
import optparse
import sys
import time

"""
TODO:-
    - Support multiple files
    - Allow for stdin input like cat ```test.txt | python3 ccwc.py```
"""

class CCWC:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.line_cnt = 0
        self.word_cnt = 0
        self.char_cnt = 0
        self.byte_cnt = 0
        if self.file_path:
            with open(self.file_path, "rb") as f:
                self._count(f)
        
    def _count(self,f: io.BufferedReader):
        for line in f.readlines():
            self.line_cnt += 1
            self.char_cnt += len(line.decode())
            self.word_cnt += len(line.split())
            self.byte_cnt += len(line)
                        

if __name__ == "__main__":
        
    parser = optparse.OptionParser(
        description="For counting words in a file"
    )
    
    parser.add_option("-l", dest = "lines", help="Count number of lines" )
    parser.add_option("-c", dest = "bytes", help="Count number of bytes")
    parser.add_option("-m", dest = "characters", help="Count number of characters")
    parser.add_option("-w", dest = "words", help="Count number of words")
    
    (options, args) = parser.parse_args()
    
    if len(sys.argv) < 2:
        print(sys.argv)
        print("Need file name or path")
        exit(1)
       
    file_path = sys.argv[-1]
    ccwc = CCWC(file_path)
    
    # print(options,args)
    if len(sys.argv) == 2:
        print(f"    {ccwc.line_cnt}    {ccwc.word_cnt}    {ccwc.byte_cnt}    {ccwc.file_path}")
        exit(0)
    if options.lines:
        print(ccwc.line_cnt, end=" ")
    if options.words:
        print(ccwc.word_cnt, end=" ")
    if options.bytes:
        print(ccwc.byte_cnt, end=" ")
    if options.characters:
        print(ccwc.char_cnt, end=" ")


    print(file_path)