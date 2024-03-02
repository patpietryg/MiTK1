def load_english_words():
    with open("words.txt", "r") as file:
        english_words = file.read().splitlines()
    return english_words

def find_english_words(text, english_words):
    text = text.lower()
    found_words = []

    def recursive_search(start_index):
        for end_index in range(len(text), start_index, -1):
            word = text[start_index:end_index]
            if word in english_words:
                found_words.append(word)
                if end_index < len(text):
                    recursive_search(end_index)
                return

    recursive_search(0)
    return found_words

def merge_words(words):
    current_text=''
    for word in words:
        current_text = current_text + word + " "
    return current_text

def string_to_ascii_array(input_string):
    ascii_array = []
    for char in input_string:
        if 'A' <= char <= 'Z':
            ascii_array.append(ord(char))
    return ascii_array

def ascii_array_to_string(ascii_array):
    output_string = ""
    for ascii_value in ascii_array:
        output_string += chr(ascii_value)
    return output_string

def caesar_cipher_encrypt(plaintext, shift):
    arr = string_to_ascii_array(plaintext.upper())

    for i in range(len(arr)):
        if 'A' <= chr(arr[i]) <= 'Z':
            arr[i] = (arr[i] + shift - ord('A')) % 26 + ord('A')

    return ascii_array_to_string(arr)
def caesar_cipher_decrypt(ciphertext, shift):
    arr = string_to_ascii_array(ciphertext.upper())

    for i in range(len(arr)):
        arr[i] = (arr[i] - shift) % 26 + ord('A') if 'A' <= chr(arr[i]) <= 'Z' else arr[i]

    return ascii_array_to_string(arr)

def caesar_cipher_break(ciphertext):
    decrypted_texts = []

    for shift in range(26):
        decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
        decrypted_texts.append(decrypted_text)

    return decrypted_texts


english_words = load_english_words() #pobranie słów angielskich z pliku
text = "that is my success"
ciphertext = caesar_cipher_encrypt(text,8)
decrypted_texts = caesar_cipher_break(ciphertext)
print("Ciphertext:", ciphertext)
final = ""
final_len = 0
for decrypted_text in decrypted_texts:
    words = find_english_words(decrypted_text, english_words)
    words_len = sum(len(word) for word in words)
    if len(decrypted_text) >= words_len > final_len:
        final_len = words_len
        final = merge_words(words)

print(final)

