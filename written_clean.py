import os
import json
import re

# Function to clean the text by removing special characters and numbered lists
def clean_text(text):
    # Remove HTML-like tags (e.g., <#\>, <h>, etc.)
    cleaned_text = re.sub(r'<[^>]+>', '', text)
    
    # Remove numbered lists (e.g., "1.", "2.", etc.)
    cleaned_text = re.sub(r'\d+\.\s?', '', cleaned_text)  # Removes "1.", "2.", etc.
    
    # Remove any remaining non-alphanumeric characters except for spaces, periods, and commas
    cleaned_text = re.sub(r'[^A-Za-z0-9\s.,]', '', cleaned_text)
    
    # Normalize whitespace to a single space and strip leading/trailing spaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text

# Function to process text files in a folder and output cleaned JSON files to another folder
def process_folder(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".txt"):  # Only process text files, case-insensitive
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename.lower().replace('.txt', '.json'))
            
            try:
                # Read the content of the text file
                with open(input_file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Clean the text content
                cleaned_content = clean_text(content)
                
                # Create a dictionary with a single column 'text'
                data = {"text": cleaned_content}
                
                # Write the dictionary to a JSON file
                with open(output_file_path, 'w', encoding='utf-8') as json_file:
                    json.dump(data, json_file, ensure_ascii=False, indent=4)
                
                print(f"Processed {filename} and saved to {output_file_path}")
            
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Specify the input and output folder paths
input_folder = 'dataset/ICE Corpus/ICE Written/W1A'  # Replace with your input folder path
output_folder = 'dataset/cleaned_ICE_Corpus_JSON/ICE Written'  # Replace with your output folder path

# Process the folder
process_folder(input_folder, output_folder)

print(f"All text files have been processed and saved to {output_folder}")