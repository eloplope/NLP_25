import re

ITU_USERNAME = "elhe"  # ← Replace with your ITU username

old_school_emojis = [
    r':\)', r':D', r'D:', r':P', r':\(', r';\)', r':\|', r':\^D', r':O', r':/', r'<3+',
    r':3', r':\*', r':-D', r':-\)', r':-\(', r':-P', r';-\)', r';-\(', r':-/', 
    r':<', r':>', r'B\)', r';P', r'=\)', r'X\)', r'XD', r':c', r'=\(',r'\¯\\_\(ツ\)_\/\¯',r'\+_O ',r':\\',r'\(:',r'\[:',r':\]',r'•\(><\)•',r';3',r'; 3',r':S',r'\(;',r'x\)',r';o',r':d',r';L',r';D',r'=]', r';L' 
]

# Function to split contractions
def split_contractions(text):
    contractions = [
        (r" im ", r" i m "),
        #(r" ur ", r" u r "),
        (r" Ur ", r" U r "),
         (r"n't", r" n't"),
        (r"can't", r"ca n't"),
        (r"can't", r"ca n't"),
        (r"cant", r"ca nt"),
        (r"didn't", r"did n't"),
        (r"didnt ", r"did nt"),
        (r"don't", r"do n't"),
        (r"dont", r"do nt"),
        (r"gotta", r"got ta"), 
        (r"gonna", r"gon na"), 
        (r"hafta", r"haf ta"),
        (r"hes", r"he s"),
        (r"i'm", r"i 'm"),
        (r"i've", r"i 've"),
        (r"it's", r"it 's"),
        (r"its", r"it s"),
        (r"oesnt", r"oes nt"),
        (r"wanna", r"wan na"),
        (r"weren't", r"were n't"),
        (r"wasn't", r"was n't"),
        (r"wasnt", r"was nt"),
        (r"won't", r"wo 'nt"),
        (r"ntgo", r"nt go"),
        (r"Im ", r"I m "),
        (r"Ur", r"U r"),
        (r"Ur", r"U r"),
        (r"N't", r"N 't"),
        (r"N'T", r"N 'T"),
        (r"Can't", r"Ca 'nt"),
        (r"Can't", r"Ca 'nt"),
        (r"Cant", r"Ca nt"),
        (r"Didn't", r"Did 'nt"),
        (r"Didnt", r"Did nt"),
        (r"Don't", r"Do 'nt"),
        (r"Gotta", r"Got ta"),
        (r"Gonna", r"Gon na"),
        (r"Hafta", r"Haf ta"),
        (r"Hes", r"He s"),
        (r"I'm", r"I 'm"),
        (r"I've", r"I 've"),
        (r"It's", r"It 's"),
        (r"Its", r"It s"),
        (r"Oesnt", r"Oes nt"),
        (r"Wanna", r"Wan na"),
        (r"Weren't", r"Were 'nt"),
        (r"Won't", r"Wo 'nt"),
        (r"WON'T", r"WO N'T"),
        (r"Ntgo", r"Nt go"),
        (r"YALL", r"Y ALL"),
        (r"Yall", r"Y all"),
        (r"y ll", r"y ll"),
        (r"Yll", r"Y ll"),
        (r"yall", r"y all"),
        (r"aint", r"ai nt"),
        (r"tryna", r"try na"),
        (r"kinda", r"kind a"),
        (r"'ll", r" 'll"),
        (r" ive ", r" i ve "),
        (r"^im\b", r"i m")
     
        #(r"' u r ", r" ur "),

    ]
    
    # Apply regex replacements for each contraction
    for contraction, replacement in contractions:
        text = re.sub(contraction, replacement, text)
    
    return text

# Create a regex pattern that includes old-school emojis
emoji_pattern = '|'.join(old_school_emojis)

# Define the regex pattern for words and other tokens
token_pattern = r'\d+[ndNDthTH]+|http\S+|(?:\$)?\d[\$:\d,./-]*|n\'t|N\'T|(?:[@~#])?\w+|[\w\'\`]+|[?\.><_\-,!(&)\']+|[^a-zA-Z\s]'

# Final pattern: Combine emoji matching first, followed by other tokens
final_pattern = f'({emoji_pattern}|{token_pattern})'

# Process the input file and write the output
with open("tok.test.txt", "r", encoding="utf-8", errors="ignore") as f_in, \
     open(f"{ITU_USERNAME}.txt", "w", encoding="utf-8") as f_out:
    
    for line in f_in:
        # Extract the text and split contractions
        text = line.split("\t")[0].strip()
        text = split_contractions(text)  # Split contractions
        
        # Apply regex to find all tokens and emojis
        tokens = re.findall(final_pattern, text)
        
        # Write the tokens to the output file
        f_out.write(" ".join(tokens) + "\n")



