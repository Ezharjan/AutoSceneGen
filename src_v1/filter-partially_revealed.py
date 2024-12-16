import re

def load_configuration(config_file):
    """
    Load configuration file and extract compatible elements/words.
    Assumes each element/word is listed on a separate line.
    """
    compatible_words = set()
    with open(config_file, 'r') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line)
            compatible_words.update(words)
    return compatible_words

def filter_text(input_text, compatible_words):
    """
    Filter out incompatible elements/words from the input text.
    """
    # Convert input text to lowercase
    input_text_lower = input_text.lower()
    # Tokenize input text into words
    words = re.findall(r'\b\w+\b', input_text_lower)
    # Convert compatible words to lowercase
    compatible_words_lower = {word.lower() for word in compatible_words}
    # Separate incompatible and compatible words
    incompatible_words = [word for word in words if word not in compatible_words_lower]
    filtered_words = [word for word in words if word in compatible_words_lower]
    # Save incompatible words to file
    with open("incompatible_words.txt", "w") as incompatible_file:
        for word in incompatible_words:
            incompatible_file.write(word + "\n")
    # Form filtered text
    filtered_text = ' '.join(filtered_words)
    return filtered_text, incompatible_words

def count_incompatible_words(incompatible_words):
    """
    Count the number of filtered incompatible words.
    """
    return len(incompatible_words)

def main():
    # Load configuration (This is only a demonstration.)
    config_file = "../CarlaPy/template.py" # TODO: Change this to your own configuration file!
    compatible_words = load_configuration(config_file)
    # Example of arbitrary input text
    input_text = "import something; that is valuable to you from utils! Try not to configure all the configs! Written by: Anonymous."
    # Filter text
    filtered_text, incompatible_words = filter_text(input_text, compatible_words)
    print("Filtered text:", filtered_text) # Output the compatible words
    print("Number of incompatible words:", count_incompatible_words(incompatible_words))

if __name__ == "__main__":
    main()
