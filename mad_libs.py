def load_template():
    with open('templates.txt', 'r') as file:
        return file.readlines()

def mad_libs():
    templates = load_template()
    template = templates[0].strip()  # Simple: use first template
    words = []
    prompts = ['adjective', 'noun', 'verb', 'adjective', 'noun']
    
    print("Enter the following words:")
    for prompt in prompts:
        words.append(input(f"{prompt.capitalize()}: ").strip())
    
    story = template.format(*words)
    print("\nYour Mad Libs Story:\n", story)
    
    with open('output.txt', 'w') as file:
        file.write(story)

if __name__ == "__main__":
    mad_libs()
