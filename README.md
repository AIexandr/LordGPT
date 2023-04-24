# LordGPT
Autonomous AI Assistant fully capable of performing tasks on its own.
JOIN US ON DISCORD: https://discord.com/channels/1099871467426025602/1099871467426025605

UPDATE: 4/24/2023 1:19PM EST
- Made a ton of changes to support GPT-3.5-turbo.

UPDATE: 4/24/203 6AM EST- IMPORTANT
ENV TEMPLATE UPDATE: Use the new env template for new functions.
- Set your API Type in env. AZURE, OPENAI, ALTERNATE. ALTERNATE will flip between the two API's allowing throttle to be reduced.
- Tweeked prompt to make AI think it said the user goal. Example: Find my location will now make the AI assume ITS location rather than trying to ask you.
- Tweeked python prompt to ensure the AI doesnt try and generate code for itself that requires an API key.
- Added default iteration
- Added working_directory when issuing commands.


KNOWN ISSUES:
1. Hallucinates and pretends to do things when the goal is too vague.
2. API Timeouts, nothing I can do. Apply for Azure GPT-4 and use the new ALTERNATE feature. Works great..


REQUIREMENTS:
Google Search API for searching.

INSTALLATION WINDOWS:
1. Enable WSL dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
2. Install WSL by running the following command: wsl --install
3. Follow the on-screen instructions to install your desired Linux distribution from the Microsoft Store.
4. Launch the Linux terminal by searching for your distribution or type WSL in the cmd prompt.

RUN THESE BASH COMMANDS, COPY AND PASTE
1. ls /home/USERNAME you choose during installation to see the files in your home directory.
2. Type sudo apt update && sudo apt upgrade && sudo apt install pip && sudo apt install wkhtmltopdf
3. type git clone GITURL
4. cd LordGPT
5. pip install -r requirements.txt - Sorry for the long requirements, its my dev machine.
6. cd /tmp/
7. wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
8. unzip chromedriver_linux64.zip
9. sudo mv chromedriver /usr/bin/chromedriver
10. wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
11. sudo dpkg -i google-chrome-stable_current_amd64.deb
12. sudo apt-get install -f
13. sudo dpkg -i google-chrome-stable_current_amd64.deb
11. mv /usr/bin/google-chrome-stable /usr/bin/google-chrome
12. Verify chrome google-chrome --version && which google-chrome

Please post issues in the GIT Issues section.

LINUX INSTALLATION
1. ls /home/USERNAME you choose during installation to see the files in your home directory.
2. Type sudo apt update && sudo apt upgrade && sudo apt install pip && sudo apt install wkhtmltopdf
3. type git clone GITURL
4. cd LordGPT
5. pip install -r requirements.txt - Sorry for the long requirements, its my dev machine.
6. cd /tmp/
7. wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
8. unzip chromedriver_linux64.zip
9. sudo mv chromedriver /usr/bin/chromedriver
10. wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
11. sudo dpkg -i google-chrome-stable_current_amd64.deb
12. sudo apt-get install -f
13. sudo dpkg -i google-chrome-stable_current_amd64.deb
11. mv /usr/bin/google-chrome-stable /usr/bin/google-chrome
12. Verify chrome google-chrome --version && which google-chrome


