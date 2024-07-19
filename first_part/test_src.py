import src

# Example usage for Task 1
word_list = ['milk', 'chocolate', 'chocolate', 'chocolate', 'chocolate', 'c+', 'python', 'cat','cat','cat', 'dog']
result = src.find_most_common_substring(word_list)
print(result)

# Example usage for Task 2
text = ("Additifs nutritionnels : Vitamine C-D3 : 160 UI, Fer (3b103) : 4mg, Iode (3b202) : 0,28 mg, "
        "Cuivre (3b405, 3b406) : 2,2 mg, Manganèse (3b502, 3b503, 3b504) : 1,1 mg, Zinc (3b603,3b605, 3b606) : 11 mg –"
        "Clinoptilolite d’origine sédimentaire : 2 g. Protéine : 11,0 % - Teneur en matières grasses : 4,5 % - "
        "Cendres brutes : 1,7 % - Cellulose brute : 0,5 % - Humidité : 80,0 %.")
nutrition_dict = src.config_values(text)
print(nutrition_dict)

# Example usage for Task 3
example_1 = [1, 2, [[4, 5], [4, 7]], 5, 4, [[95], [2]]]
example_2 = [5, 9, 4, [[8, 7]], 4, 7, [[5]]]

result = src.is_grandma_list(example_1)
result2 = src.is_grandma_list(example_2)

if result:
    print(example_1, 'is grandma list')
else:
    print(example_1, 'is not grandma list')

if result2:
    print(example_2, 'is grandma list')
else:
    print(example_2, 'is not grandma list')
