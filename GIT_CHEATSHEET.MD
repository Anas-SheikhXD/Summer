First time setting up a NEW project folder (one-time only, per folder)
bash
cd /d/TOOLS/your-folder-name
git init
git add .
git commit -m "Initial commit"

Then, create an empty repo on GitHub.com first (name it whatever, don't add README/gitignore), then:

bash
git remote add origin https://github.com/Anas-SheikhXD/your-repo-name.git
git branch -M main
git push -u origin main
Every time after that (daily — pushing new changes)
bash
git add .
git commit -m "describe what changed"
git push
Quick reminders
cd /d/TOOLS/... — always navigate into the correct folder first (check with pwd if unsure)
Windows D:\TOOLS\folder becomes /d/TOOLS/folder in Git Bash
git status anytime to check what's staged/unstaged/untracked
If you get "remote origin already exists" error → use git remote set-url origin <correct-url> instead of git remote add