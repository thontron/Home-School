"""
Converts regular text text to banner3D text
"""


from colorize import bold

# initalise the values for the letters
LETTERS = {
    "A": [
        "|||'###||||",
        "||'## ##|||",
        "|'##|| ##||",
        "'##|||| ##|",
        " #########|",
        " ##|||| ##|",
        " ##|||| ##|",
        "|||||||||||",
    ],
    "B": [
        "'########||",
        " ##|||| ##|",
        " ##|||| ##|",
        " ########||",
        " ##|||| ##|",
        " ##|||| ##|",
        " ########||",
        "|||||||||||",
    ],
    "C": [
        "|'######||",
        "'##||| ##|",
        " ##|||||||",
        " ##|||||||",
        " ##|||||||",
        " ##||| ##|",
        "| ######||",
        "||||||||||",
    ],
    "D": [
        "'########||",
        " ##|||| ##|",
        " ##|||| ##|",
        " ##|||| ##|",
        " ##|||| ##|",
        " ##|||| ##|",
        " ########||",
        "|||||||||||",
    ],
    "E": [
        "'########|",
        " ##|||||||",
        " ##|||||||",
        " ######|||",
        " ##|||||||",
        " ##|||||||",
        " ########|",
        "||||||||||",
    ],
    "F": [
        "'########|",
        " ##|||||||",
        " ##|||||||",
        " ######|||",
        " ##|||||||",
        " ##|||||||",
        " ##|||||||",
        "||||||||||",
    ],
    "G": [
        "|'######|||",
        "'##||| ##||",
        " ##||||||||",
        " ##||'####|",
        " ##||| ##||",
        " ##||| ##||",
        "| ######|||",
        "|||||||||||",
    ],
    "H": [
        "'##||||'##|",
        " ##|||| ##|",
        " ##|||| ##|",
        " #########|",
        " ##|||| ##|",
        " ##|||| ##|",
        " ##|||| ##|",
        "|||||||||||",
    ],
    "I": [
        "'####|",
        "| ##||",
        "| ##||",
        "| ##||",
        "| ##||",
        "| ##||",
        "'####|",
        "||||||",
    ],
    "J": [
        "||||||'##|",
        "|||||| ##|",
        "|||||| ##|",
        "|||||| ##|",
        "'##||| ##|",
        " ##||| ##|",
        "| ######||",
        "||||||||||",
    ],
    "K": [
        "'##|||'##|",
        " ##||'##||",
        " ##|'##|||",
        " #####||||",
        " ##| ##|||",
        " ##|| ##||",
        " ##||| ##|",
        "||||||||||",
    ],
    "L": [
        "'##|||||||",
        " ##|||||||",
        " ##|||||||",
        " ##|||||||",
        " ##|||||||",
        " ##|||||||",
        " ########|",
        "||||||||||",
    ],
    "M": [
        "'##||||'##|",
        " ###||'###|",
        " ####'####|",
        " ## ### ##|",
        " ##| #| ##|",
        " ##|||| ##|",
        " ##|||| ##|",
        "|||||||||||",
    ],
    "N": [
        "'##||| ##|",
        " ###|| ##|",
        " ####| ##|",
        " ## ## ##|",
        " ##| ####|",
        " ##|| ###|",
        " ##||| ##|",
        "||||||||||",
    ],
    "O": [
        "|'#######||",
        "'##|||| ##|",
        " ##|||| ##|",
        " ##|||| ##|",
        " ##|||| ##|",
        " ##|||| ##|",
        "| #######||",
        "|||||||||||",
    ],
    "P": [
        "'########||",
        " ##|||| ##|",
        " ##|||| ##|",
        " ########||",
        " ##||||||||",
        " ##||||||||",
        " ##||||||||",
        "|||||||||||",
    ],
    "Q": [
        "|'#######||",
        "'##|||| ##|",
        " ##|||| ##|",
        " ##|||| ##|",
        " ##|'## ##|",
        " ##||| ##||",
        "| ##### ##|",
        "|||||||||||",
    ],
    "R": [
        "'########||",
        " ##|||| ##|",
        " ##|||| ##|",
        " ########||",
        " ##|| ##|||",
        " ##||| ##||",
        " ##|||| ##|",
        "|||||||||||",
    ],
    "S": [
        "|'######||",
        "'##||| ##|",
        " ##|||||||",
        "| ######||",
        "|||||| ##|",
        "'##||| ##|",
        "| ######||",
        "||||||||||",
    ],
    "T": [
        "'########|",
        "||| ##||||",
        "||| ##||||",
        "||| ##||||",
        "||| ##||||",
        "||| ##||||",
        "||| ##||||",
        "||||||||||",
    ],
    "U": [
        "'##||||'##|",
        " ##|||| ##|",
        " ##|||| ##|",
        " ##|||| ##|",
        " ##|||| ##|",
        " ##|||| ##|",
        "| #######||",
        "|||||||||||",
    ],
    "V": [
        "'##||||'##|",
        " ##|||| ##|",
        " ##|||| ##|",
        " ##|||| ##|",
        "| ##|| ##||",
        "|| ## ##|||",
        "||| ###||||",
        "|||||||||||",
    ],
    "W": [
        "'##|||||'##|",
        " ##|'##| ##|",
        " ##| ##| ##|",
        " ##| ##| ##|",
        " ##| ##| ##|",
        " ##| ##| ##|",
        "| ###| ###||",
        "||||||||||||",
    ],
    "X": [
        "'##||||'##|",
        "| ##||'##||",
        "|| ##'##|||",
        "||| ###||||",
        "|| ## ##|||",
        "| ##|| ##||",
        " ##|||| ##|",
        "|||||||||||",
    ],
    "Y": [
        "'##|||'##|",
        "| ##|'##||",
        "|| ####|||",
        "||| ##||||",
        "||| ##||||",
        "||| ##||||",
        "||| ##||||",
        "||||||||||",
    ],
    "Z": [
        "'########|",
        "||||| ##||",
        "|||| ##|||",
        "||| ##||||",
        "|| ##|||||",
        "| ##||||||",
        " ########|",
        "||||||||||",
    ],
    " ": [
        "||||||||||",
        "||||||||||",
        "||||||||||",
        "||||||||||",
        "||||||||||",
        "||||||||||",
        "||||||||||",
        "||||||||||",
    ],
    ":": [
        "|||'##||||",
        "|| ####|||",
        "||| ##||||",
        "||||||||||",
        "|||'##||||",
        "|| ####|||",
        "||| ##||||",
        "||||||||||",
    ],
    ".": [
        "||||||||||",
        "||||||||||",
        "||||||||||",
        "||||||||||",
        "|||'##||||",
        "|| ####|||",
        "||| ##||||",
        "||||||||||",
    ],
    "!": [
        "|||'##||||",
        "||| ##||||",
        "||| ##||||",
        "||||||||||",
        "|||'##||||",
        "|| ####|||",
        "||| ##||||",
        "||||||||||",
    ],
    ",": [
        "||||||||||",
        "||||||||||",
        "||||||||||",
        "||||||||||",
        "|||'##||||",
        "|| ####|||",
        "||| ##||||",
        "|| #||||||",
    ],
}


def convert(text, background, foreground):
    """
        Converts regular text text to banner3D text
    """
    # only uppercase text is accepted
    text = text.upper()

    # loop through letter rows
    for row in range(8):
        # loop through the charecters on the text
        for _, letter in enumerate(text):
            # get the correct ASCII row and letter
            string = LETTERS[letter][row]
            # initalize `new_string`
            new_string = ""
            # append colored charecters to final string
            for char in string:
                if char == "#":
                    new_string += bold(foreground, char)
                else:
                    new_string += bold(background, char)
            # print each letters correct row
            print(new_string, end="")
        # newline at end of ASCII row
        print("")


# example conversion
if __name__ == "__main__":
    convert("Banner text", "red", "white")