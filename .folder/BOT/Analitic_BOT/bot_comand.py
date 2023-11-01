def get_html_content(url):
    response = requests.get(url)
    return response.text


def get_top_chars(text):
    cyrillic_chars = [char for char in text if char.isalpha() and char.isalpha() and char.islower()]
    top_chars = Counter(cyrillic_chars).most_common(10)
    return top_chars


def get_top_words(text):
    words = [word.lower() for word in text.split() if word.isalpha() and len(word) >= 5]
    top_words = Counter(words).most_common(10)
    return top_words


def get_code_stats(text):
    num_chars = len(text)
    num_spaces = text.count(' ')
    top_char = Counter(text).most_common(1)[0]
    return num_chars, num_spaces, top_char


def analyze_website(update, context):
    url = update.message.text
    html_content = get_html_content(url)