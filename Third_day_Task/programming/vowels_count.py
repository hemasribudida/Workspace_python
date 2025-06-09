def get_vowels_and_count(input_str):
    vowels = 'aeiouAEIOU' 

    vowel_list = list(filter(lambda ch: ch in vowels, input_str))

    count = len(vowel_list)

    return vowel_list, count

input_string = "quintessential"

vowels_found, total_count = get_vowels_and_count(input_string)

print("Vowels:", vowels_found)
print("Count:", total_count)
