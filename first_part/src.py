########################################################################## Task 1 #########################################################################

from collections import Counter

def find_most_common_substring(words):
    # Count the frequency of each complete word
    word_counts = Counter(words)
    
    # Find the most common complete word
    most_common_word = word_counts.most_common(1)
    
    # If a complete word is the most common, return it
    if most_common_word and most_common_word[0][1] > 1:
        return most_common_word[0][0]
    
    # Count substrings of length > 1
    substring_counts = Counter()
    for word in words:
        word_length = len(word)
        for i in range(word_length):
            for j in range(i+2, word_length+1):  # +2 to ensure substrings are at least 2 characters long
                substring = word[i:j]
                substring_counts[substring] += 1
    
    if not substring_counts:
        return ""
    
    # Return the most common substring
    return max(substring_counts, key=substring_counts.get)


########################################################################## Task 2 #########################################################################

import re

def config_values(text):
    # Clean the text by replacing non-standard delimiters with commas
    cleaned_text = text.replace('–', ',').replace(' - ', ',').replace('. ', ', ')
    
    # Regular expression to match nutritional values and their units
    pattern = re.compile(r'([A-Za-zéèûôïçâêëç\s\-\(\)0-9,]+?)\s*:\s*([\d.,]+\s*[a-zA-Z%]+)')
    
    # Find all matches in the text
    matches = pattern.findall(cleaned_text)
    
    # Build the dictionary
    nutrition_dict = {}
    for match in matches:
        key = match[0].strip().strip(',')
        value = match[1].strip()
        nutrition_dict[key] = value
    
    return nutrition_dict

# Given text containing nutritional values
text = ("Additifs nutritionnels : Vitamine C-D3 : 160 UI, Fer (3b103) : 4mg, Iode (3b202) : 0,28 mg, "
        "Cuivre (3b405, 3b406) : 2,2 mg, Manganèse (3b502, 3b503, 3b504) : 1,1 mg, Zinc (3b603,3b605, 3b606) : 11 mg –"
        "Clinoptilolite d’origine sédimentaire : 2 g. Protéine : 11,0 % - Teneur en matières grasses : 4,5 % - "
        "Cendres brutes : 1,7 % - Cellulose brute : 0,5 % - Humidité : 80,0 %.")


########################################################################## Task 3 #########################################################################

def is_grandma_list(lst):
    # Helper function to calculate the products of adjacent numbers in a list
    def calculate_products(sub_lst):
        products = set()
        for i in range(len(sub_lst) - 1):
            if isinstance(sub_lst[i], int) and isinstance(sub_lst[i + 1], int):
                product = sub_lst[i] * sub_lst[i + 1]
                products.add(product)
        return products
    
    # Helper function to collect all values in the list and its nested lists
    def collect_values(sub_lst):
        values = set()
        for item in sub_lst:
            if isinstance(item, list):
                values.update(collect_values(item))
            elif isinstance(item, int):
                values.add(item)
        return values

    # Collect all products of adjacent numbers in the nested lists
    products = set()
    def traverse(sub_lst):
        if isinstance(sub_lst, list):
            products.update(calculate_products(sub_lst))
            for item in sub_lst:
                traverse(item)
    
    traverse(lst)
    
    # Collect all values in the list
    all_values = collect_values(lst)
    
    # Check if any product is in the set of all values
    return any(product in all_values for product in products)
