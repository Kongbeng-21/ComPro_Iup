# Name: Krittitee Chaisang #  Student ID: 6810545441
from pathlib import Path

input_ = input("Enter the input filename: ")
need = input("Enter the word to find: ")
replace = input("Enter the replacement word: ")
output_ = input("Enter the output filename: ")

path = Path(input_)

if path.exists():
    with open(path,"r")as f:
        word = f.read()
    new_word = word.replace(need,replace)
    
    with open(output_,"w")as f:
        f.write(new_word)
    print(f"Replacement complete. Content saved to {output_}.")        
                
else:
    print(f"Error: Input file '{input_}' not found.")