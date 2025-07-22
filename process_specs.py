import json

# Input and Output filenames
json_filename = 'everest_story_catcher_specs.json'
output_filename = 'requirements.md'

print(f"Reading {json_filename} to create {output_filename}...")

try:
    # Open and load the JSON data
    with open(json_filename, 'r') as f:
        data = json.load(f)

    # Check if the main requirements key exists
    if 'aiSpecRequirements' in data:
        requirements_list = data['aiSpecRequirements']

        # Open the new markdown file for writing
        with open(output_filename, 'w') as f_out:
            # Write a main title for the document
            project_name = data.get('name', 'AI Project')
            f_out.write(f"# Functional Requirements for {project_name}\n\n")

            # Loop through all requirements in the list
            for req in requirements_list:
                # Safely get the data from each requirement using the correct keys
                title = req.get('title', 'No Title')
                description = req.get('description', 'No description.')
                priority = req.get('priority', 'N/A')
                req_type = req.get('type', 'N/A')

                # Write the formatted requirement to the markdown file
                f_out.write(f"## {title}\n\n")
                f_out.write(f"**Priority:** {priority}  \n")
                f_out.write(f"**Type:** {req_type}  \n\n")
                f_out.write(f"{description}\n\n")
                f_out.write("---\n\n") # Add a horizontal line for separation

        print(f"✅ Success! All {len(requirements_list)} requirements have been written to {output_filename}")

    else:
        print("❌ Could not find the key 'aiSpecRequirements' in the JSON file.")


except FileNotFoundError:
    print(f"❌ ERROR: The file '{json_filename}' was not found.")
except json.JSONDecodeError:
    print(f"❌ ERROR: The file '{json_filename}' is not a valid JSON file.")