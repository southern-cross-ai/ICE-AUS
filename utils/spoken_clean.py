import os
import json

def txt_to_json(txt_file):
    with open(txt_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split sentences using newlines and punctuation symbols
    sentences = content.replace('\n', ' ').split('<$')
    json_output = []

    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            # Remove special symbols and tags within the line
            cleaned_sentence = sentence.split(">")[-1].strip()
            if cleaned_sentence:  # Check if the cleaned sentence is not empty
                json_output.append({"text": cleaned_sentence})
    
    return json_output

def process_directory(input_directory, output_directory):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    print(f"Processing directory: {input_directory}")
    
    # Use os.walk() to traverse the directory and its subdirectories
    for root, dirs, files in os.walk(input_directory):
        print(f"Current directory: {root}")
        print(f"Files found: {files}")
        
        for filename in files:
            if filename.endswith('.TXT'):
                txt_file_path = os.path.join(root, filename)
                print(f"Processing file: {txt_file_path}")
                
                try:
                    json_data = txt_to_json(txt_file_path)

                    # Create output directory structure identical to the input directory structure
                    relative_path = os.path.relpath(root, input_directory)
                    json_output_dir = os.path.join(output_directory, relative_path)
                    
                    if not os.path.exists(json_output_dir):
                        os.makedirs(json_output_dir)
                    
                    # Generate output JSON file path
                    json_filename = os.path.splitext(filename)[0] + '.json'
                    json_file_path = os.path.join(json_output_dir, json_filename)
                    
                    with open(json_file_path, 'w', encoding='utf-8') as json_file:
                        json.dump(json_data, json_file, ensure_ascii=False, indent=2)

                    print(f"Saved to {json_file_path}")
                
                except Exception as e:
                    print(f"Error processing file {txt_file_path}: {e}")

input_directory_path = "dataset/ICE Corpus/ICE Spoken/S2B"
output_directory_path = "dataset/cleaned_ICE_Corpus_JSON/ICE Spoken"

process_directory(input_directory_path, output_directory_path)