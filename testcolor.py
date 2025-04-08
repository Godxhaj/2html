import sys


# Initialize colorama to handle ANSI codes
print("gko:")

# Custom class to redirect output to both terminal and file
class DualStream:
    def __init__(self, file):
        self.file = file
        self.terminal = sys.stdout

    def write(self, message):
        self.terminal.write(message)  # Write to terminal
        self.file.write(message)      # Write to file

    # def flush(self):
    #     self.terminal.flush()         # Flush terminal
    #     self.file.flush()             # Flush file

# Redirect standard output to a file
with open('output_with_colors.txt', 'w') as f:
    sys.stdout = DualStream(f)
# Reset stdout to default
sys.stdout = sys.__stdout__
