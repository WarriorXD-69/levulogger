import colorama
import time
from colorama import Fore

# Credits to ReXx..!!

colorama.init()

class levu:
    def __init__(self):
        self.time_format = '%H:%M:%S'
        self.prefix = lambda: f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTWHITE_EX}{time.strftime(self.time_format, time.localtime())}{Fore.LIGHTBLACK_EX}]"
        self.suffix = f"{Fore.LIGHTBLACK_EX}"
        self.warning_color = "\x1b[38;5;214m" 

    def success(self, message):
        """Print success message with green dot"""
        print(f"{self.prefix()} [{Fore.GREEN}●{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.GREEN} SUCCESS {Fore.LIGHTWHITE_EX}» {message} {self.suffix}")

    def error(self, message):
        """Print error message with red dot"""
        print(f"{self.prefix()} [{Fore.RED}⊘{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.RED} ERROR {Fore.LIGHTWHITE_EX}» {message} {self.suffix}")

    def debug(self, message):
        """Print debug message with blue dot"""
        print(f"{self.prefix()} [{Fore.BLUE}◉{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.BLUE} DEBUG {Fore.LIGHTWHITE_EX}» {message} {self.suffix}")

    def warn(self, message):
        """Print warning message with custom orange dot"""
        print(f"{self.prefix()} [{self.warning_color}☢{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{self.warning_color} WARN {Fore.LIGHTWHITE_EX}» {message} {self.suffix}")
    
    def ratelimit(self, message):
        """Print ratelimit message with yellow dot"""
        print(f"{self.prefix()} [{Fore.YELLOW}!{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.YELLOW} RATELIMIT {Fore.LIGHTWHITE_EX}» {message} {self.suffix}")

    def info(self, message):
        """Print info with cyan colour"""
        print(f"{self.prefix()} [{Fore.LIGHTCYAN_EX}◉{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.LIGHTCYAN_EX} INFO {Fore.LIGHTWHITE_EX}» {message} {self.suffix}")
    
    def input(self, prompt):
        """Get input with magenta arrow prompt"""
        print(f"{self.prefix()} [{Fore.LIGHTRED_EX}?{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX}{Fore.LIGHTRED_EX} INPUT {Fore.LIGHTWHITE_EX}» {prompt} {self.suffix}»{Fore.RESET}", end=" ")
        return input()
    
