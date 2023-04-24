botcommands = [
    {
        "command_string": "create_task_list",
        "command_argument": "[CONTENT]",
        "command_description": "Your first command should be to create the task list. Replace '[CONTENT]' with the string content."
    },
    {
        "command_string": "no_command",
        "command_argument": "None",
        "command_description": "Used when you do not need to use a command"
    },
    {
        "command_string": "create_pdf_from_html_markup",
        "command_argument": "Filename: [FILENAME] Content: [CONTENT]",
        "command_description": "Create PDF's by sending formatted HTML as the content along with any research data."
    },
    {
        "command_string": "create_python_script",
        "command_argument": "Filename: [FILENAME] Content: [CONTENT]",
        "command_description": "Writes and saves a formatted non interactive python script that do not require API keys. Replace '[FILENAME]' with the desired filename and '[CONTENT]' with the formatted python script (using triple quotes)."
    },
    {
        "command_string": "write_new_content_to_file",
        "command_argument": "Filename: [FILENAME] Content: [CONTENT]",
        "command_description": "Write and save formatted text content to a file. Replace '[FILENAME]' with the desired filename and '[CONTENT]' with the content sent as a multiline string using triple quotes."
    },
    {
        "command_string": "append_content_to_existing_file",
        "command_argument": "Filename: [FILENAME] Content: [CONTENT]",
        "command_description": "Append formatted content or formatted code to existing files. Replace '[FILENAME]' with the desired filename and '[CONTENT]' with the file content as a multiline string (using triple quotes)."
    },
    {
        "command_string": "read_content_from_file",
        "command_argument": "Filename: [FILENAME]",
        "command_description": "Reads formatted content from existing file."
    },
    {
        "command_string": "search_google",
        "command_argument": "Query 7 Words Long|pagenumber",
        "command_description": "Creates a list of url's and snippets by passing a query and page number. Pass the arugment as query|pagenum Example: Query|2"
    },
    {
        "command_string": "scrape_website_url",
        "command_argument": "https://url",
        "command_description": "Used to scrape the contents of a URL with http or https. Replace 'url' with the single web address you want to visit. Summerize the content when analyzing and visit every URL for thorough research"
    },
    {
        "command_string": "save_research",
        "command_argument": "Title: [CONTENT] ResearchContent: [CONTENT]",
        "command_description": "Saves data gathered from the internet and through research. Format argument as Title: [CONTENT] ResearchContent: [CONTENT]"
    },
    {
        "command_string": "fetch_research",
        "command_argument": "Title: [CONTENT] ResearchContent: [CONTENT]",
        "command_description": "Fetch all research data to use in PDF report."
    },
    {
        "command_string": "run_bash_shell_command",
        "command_argument": "[BASH COMMAND]",
        "command_description": "Execute non-interactive ubuntu bash shell commands or python scripts to fully manage the system you are on. Pass the BASH command as a command_argument or python3 to run python."
    },
    {
        "command_string": "mission_accomplished",
        "command_argument": "Mission accomplishment message",
        "command_description": "Marks the goal as completed if all tasks have been completed."
    },
]


