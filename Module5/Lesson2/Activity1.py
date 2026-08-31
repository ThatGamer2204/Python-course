class IOString:
    def __init__(self):
        self.str1=""
    def get_String(self):
        self.str1=input("Enter a string :")
    def print_String(self):
        self.str1=self.str1.upper()
        print(self.str1)

blue=IOString()
blue.get_String()
blue.print_String()
