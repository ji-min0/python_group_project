import json

# txt -> json
def convert_to_json(input_file: str, output_file: str): 
    profanity_list = []
    
    with open(input_file, "r", encoding="utf-8") as f: 
        for line in f: 
            profanity_list.append(line.strip())
            
    with open(output_file, "w", encoding="utf-8") as json_file: 
        json.dump(profanity_list, json_file, ensure_ascii=False, indent=4)



if __name__ == "__main__": 
    convert_to_json("profanity.txt", "profanity.json")

