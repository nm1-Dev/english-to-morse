# Define a dictionary mapping each English letter to its Morse code
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '
}

def text_to_morse(text):
    # Convert each character in the input text to Morse code
    morse_code = [morse_code_dict[char.upper()] for char in text]
    # Join the Morse code representations and return the result
    return ' '.join(morse_code)

# Example usage:
input_text = input("Enter English Words: ")
morse_result = text_to_morse(input_text)
print(f"Morse Code: {morse_result}")
