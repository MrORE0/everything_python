# Live git demo

Follow along in a terminal and copy-paste each block. Use **Git Bash** on Windows, Terminal on macOS/Linux. Everything happens in a throwaway folder, so nothing touches your real projects.

Expected output is shown under each block (hashes and dates will differ).

## 0. Set up a scratch folder

```bash
mkdir git-demo
cd git-demo
```

## 1. Create a repo

```bash
git init -b main
```

```
Initialized empty Git repository in .../git-demo/.git/
```

Older git (before 2.28) doesn't know `-b`. Use `git init` followed by `git checkout -b main` instead.

Check that git knows who you are (needed once per machine). If this prints nothing, set it as shown in the pre-class checklist:

```bash
git config user.name
git config user.email
```

## 2. First commit: status, add, commit

```bash
echo 'print("Hello from main")' > greeting.py
git status --short
```

```
?? greeting.py
```

`??` means untracked: git sees the file but isn't watching it yet.

```bash
git add greeting.py
git status --short
```

```
A  greeting.py
```

The file is now **staged**: it will go into the next commit.

```bash
git commit -m "Add greeting script"
```

## 3. Change something, look at the diff, commit again

```bash
echo 'print("Welcome to Everything Python")' >> greeting.py
git diff
```

```
+print("Welcome to Everything Python")
```

`git diff` shows changes that are not staged yet. Lines starting with `+` were added.

```bash
git commit -am "Add welcome line"
git log --oneline
```

```
1f11328 Add welcome line
eb2f8e9 Add greeting script
```

`-a` stages every already-tracked file before committing. It does not pick up new files.

## 4. Branch off to work on a feature

```bash
git switch -c feature
```

```
Switched to a new branch 'feature'
```

Older git (before 2.23): `git checkout -b feature`.

Change the greeting on this branch (this rewrites the whole file with two lines):

```bash
printf 'print("Hello from the feature branch")\nprint("Welcome to Everything Python")\n' > greeting.py
git commit -am "Change greeting on feature branch"
```

## 5. Meanwhile, main moves on and edits the same line

```bash
git switch main
printf 'print("Hello, world")\nprint("Welcome to Everything Python")\n' > greeting.py
git commit -am "Change greeting on main"
git log --oneline --graph --all
```

```
* 79a3ed8 Change greeting on feature branch
| * 29b763c Change greeting on main
|/
* 1f11328 Add welcome line
* eb2f8e9 Add greeting script
```

This is the picture from the slide: history split in two, with `main` and `feature` each pointing at their own latest commit.

## 6. Merge, and hit a conflict

```bash
git merge feature
```

```
Auto-merging greeting.py
CONFLICT (content): Merge conflict in greeting.py
Automatic merge failed; fix conflicts and then commit the result.
```

Both branches changed line 1, so git can't decide. This is normal.

```bash
git status --short
cat greeting.py
```

```
UU greeting.py
<<<<<<< HEAD
print("Hello, world")
=======
print("Hello from the feature branch")
>>>>>>> feature
print("Welcome to Everything Python")
```

- Between `<<<<<<< HEAD` and `=======` is **your current branch** (`main`).
- Between `=======` and `>>>>>>> feature` is **the branch being merged**.
- Line 2 had no conflict, so it is left alone.

## 7. Resolve the conflict: edit, add, commit

Open `greeting.py` in your editor, delete the three marker lines, and decide what the file should say. To keep this copy-pasteable, this block writes the resolved version (a combination of both sides):

```bash
printf 'print("Hello, world from the feature branch")\nprint("Welcome to Everything Python")\n' > greeting.py
cat greeting.py
```

Tell git the conflict is resolved, then finish the merge:

```bash
git add greeting.py
git commit -m "Merge feature into main"
git log --oneline --graph --all
```

```
*   42839d0 Merge feature into main
|\
| * 79a3ed8 Change greeting on feature branch
* | 29b763c Change greeting on main
|/
* 1f11328 Add welcome line
* eb2f8e9 Add greeting script
```

The two lines of history join in a **merge commit**.

## 8. `.gitignore` keeps junk out

```bash
mkdir data
echo "Hamburg;12.0" > data/measurements.txt
git status --short
```

```
?? data/
```

Git wants to track the generated data. Tell it not to:

```bash
printf 'data/measurements.txt\n__pycache__/\n' > .gitignore
git status --short
```

```
?? .gitignore
```

`data/` no longer shows up. Commit the ignore file itself:

```bash
git add .gitignore
git commit -m "Ignore generated data"
```

## 9. Undo toolbox

Discard an uncommitted edit:

```bash
echo 'print("oops")' >> greeting.py
git restore greeting.py
cat greeting.py
```

The `oops` line is gone. Now undo a **commit** safely:

```bash
echo 'print("debug debug debug")' >> greeting.py
git commit -am "Add debug print"
git revert --no-edit HEAD
git log --oneline
```

```
1c9b8fc Revert "Add debug print"
6c47a08 Add debug print
4971e6a Ignore generated data
...
```

`revert` doesn't erase history. It adds a **new commit** that undoes the old one, which is safe even if other people already have your commits.

```bash
cat greeting.py
```

The file is clean again.

## Clean up

```bash
cd ..
rm -rf git-demo
```
