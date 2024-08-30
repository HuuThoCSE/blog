import os
import re
import json

def find_markdown_files(directory):
    """Find all markdown files in a directory."""
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def extract_links(file_path):
    """Extract markdown links from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        links = re.findall(r'\[.+?\]\((.+?)\)', content)
        return links

def create_graph_data(directory):
    """Create graph data from markdown files."""
    graph_data = {'nodes': [], 'edges': []}
    files = find_markdown_files(directory)
    for file in files:
        node_id = os.path.basename(file)
        graph_data['nodes'].append({'id': node_id, 'label': node_id})
        links = extract_links(file)
        for link in links:
            target = os.path.basename(link)
            if target.endswith('.md'):
                graph_data['edges'].append({'from': node_id, 'to': target})
    return graph_data

# Specify the directory of your Markdown files
markdown_directory = 'docs'
graph_data = create_graph_data(markdown_directory)

# Save the graph data to a JSON file
with open('docs/graph_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(graph_data, json_file, ensure_ascii=False, indent=4)

print("Graph data generated and saved to 'docs/graph_data.json'")
