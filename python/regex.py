import re

import re
def get_matching_words(regex):
 words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
 matches = []
 for word in words:
 	if re.search(regex,word):
 		matches.append(word)
 return matches


# will not work with comments. must delete comments to run. 


print get_matching_words(r'v')

print get_matching_words(r"ss")

print get_matching_words(r"e$")

print get_matching_words(r'b.b')

print get_matching_words(r'b.+b')

print get_matching_words(r'b.*b')
print get_matching_words(r"a[^aeiou]*e[^aeiou]*i[^aeiou]*o[^aeiou]*u[^aeiou]*")
print get_matching_words(r"^[regularexpression]+$")
print get_matching_words(r"(.+)\1")




All words that contain a “v”
All words that contain a double-“s”
All words that end with an “e”
All words that contain an “b”, any character, then another “b”
All words that contain an “b”, at least one character, then another “b”
All words that contain an “b”, any number of characters (including zero), then another “b”
All words that include all five vowels in order
All words that only use the letters in “regular expression” (each letter can appear any number of times)
All words that contain a double letter