import pandas as pd
import re
import contractions
import csv

def expand_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Define custom replacement patterns
    custom_replacements = {
        r"\bi[' ]?m\b": "i am",            # i'm, i m
        r"\bdon'?t\b": "do not",            # don't, dont
        r"\bur\b": "your",                 # ur -> your
        r"\byr\b": "your",                 # yr -> your
        r"\bu\b": "you",                   # u -> you
        r"\br\b": "are",                   # r -> are
        r"\bcuz\b": "because",             # cuz -> because
        r"\bwanna\b": "want to",           # wanna -> want to
        r"\bgonna\b": "going to",          # gonna -> going to
        r"\bkinda\b": "kind of",           # kinda -> kind of
        r"\bgotta\b": "got to",            # gotta -> got to
        r"\blemme\b": "let me",            # lemme -> let me
        r"\bbetcha\b": "bet you",          # betcha -> bet you
        r"\bya\b": "you",                  # ya -> you
        r"\bpls\b": "please",              # pls -> please
        r"\bplz\b": "please",              # plz -> please
        r"\bthx\b": "thanks",              # thx -> thanks
        r"\bty\b": "thank you",            # ty -> thank you
        r"\bluv\b": "love",                # luv -> love
        r"\bidk\b": "i do not know",       # idk -> i do not know
        r"\bimo\b": "in my opinion",       # imo -> in my opinion
        r"\bbrb\b": "be right back",       # brb -> be right back
        r"\bttyl\b": "talk to you later"    # ttyl -> talk to you later
    }
    
    # Apply each custom replacement using regex
    # for pattern, replacement in custom_replacements.items():
    #     text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    
    # Expand any remaining standard contractions using the contractions library
    text = contractions.fix(text)
    
    return text

# # Load your dataset (update the file path as needed)
# df = pd.read_csv("cleaned_dataset.csv")

# # Apply the expansion function to the 'text' column
# df["cleaned_text"] = df["text"].apply(expand_text)

# # Save only the 'label' and 'cleaned_text' columns to a new CSV file,
# # wrapping all values in double quotes.
# output_csv_path = "preprocessed_dataset.csv"
# df[["label", "cleaned_text"]].to_csv(
#     output_csv_path,
#     index=False,
#     quotechar='"',
#     quoting=csv.QUOTE_ALL
# )

# print("Preprocessed data saved to:", output_csv_path)