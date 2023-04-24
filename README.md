# LordGPT
Autonomous AI Assistant fully capable of performing tasks on its own.
JOIN US ON DISCORD: https://discord.com/channels/1099871467426025602/1099871467426025605

WELCOME LordGPT is an automated AI Assistant that can accomplish a wide range of tasks.
- Browse Internet and Research
- Read and Write local files.
- Generate Python Scripts, and even write its own commands to further is capabilities.
- Search Google
- Generate formatted PDF Reports
- Use more than one API at a time. Options to flip between Azure and OpenAI for each call, reducing timeouts, and helping Azure and OpenAI out by spreading out requests.

LordGPT is different from other AI agents. I designed it not with code, but with prompt engineering. The code is simple as you can tell. The prompts are formatted to perform the tasks, not code. Hundreds of hours were spent on these prompts, and the slightest change will throw him off, keep that in mind. Also, I choose not to use the OpenAI module, and build from scratch to increase speed, even if its a few ms. Other than that, I hope you enjoy it as much as I did creating it.

COMING SOON:
Releasing a binary shortly to run LordGPT directly on windows without any of the steps below. Check back.

KNOWN ISSUES:
1. My python code is not optimized, no need to tell me. Join and help or post an issue.
2. Hallucinates and pretends to do things when the goal is too vague. I'm mostly fixed this but it happens randomly. Decrease the temp and top_p helps.
3. API Timeouts, nothing I can do. Apply for Azure GPT-4 and use the new ALTERNATE feature. Works great..
4. The prompts were built with my thinking mind, with that said you might prompt it to do things I didnt think of.


REQUIREMENTS:
- Google Search API for searching.
- Deep pockets for tokens.

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
11. mv /usr/bin/google-chrome-stable /usr/bin/google-chrome
12. Verify chrome google-chrome --version && which google-chrome


