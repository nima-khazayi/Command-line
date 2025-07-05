
# Figlet Python Script

This program script uses the 'pyfiglet' library
to render text in various ASCII art fonts.
It can be run from the command line or interactively.

## Installation 

To use this script, you need to have Python installed along with the 
'pyfiglet' library. You can install it using pip:
```bash

pip install pyfiglet
```

## Usage 

You can run the script in two ways:

1. **Interactive Mode:** Simply run the script without any arguments to input text interactively.
    ```python figlet.py```
2. **Command Line Mode:** You can specify a font using command-line arguments.
   
   ```bash
   
   python figlet.py -f <font_name>
   ```

## Example
```bash

python figlet.py -f slant
```
After running the command, input your text:
```
Input: Welcome
Output:

```
Find out!

## Error Handling

- If you provide an invalid font name, the script will exit with and error code.
- If the usage is incorrect, the script will print "Invalid usage" and exit.
