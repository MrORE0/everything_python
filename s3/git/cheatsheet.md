# Git cheat sheet

## The three areas

```
working directory  --git add-->  staging area  --git commit-->  repository (history)
   (your files)                  (next commit)                    (permanent snapshots)
```

## Everyday commands

| Command | What it does |
|---|---|
| `git init` | start a repo in the current folder |
| `git clone <url>` | copy a remote repo to your machine |
| `git status` | what changed, what is staged |
| `git add <file>` | stage a file for the next commit |
| `git commit -m "message"` | save a snapshot of everything staged |
| `git diff` | unstaged changes (`git diff --staged` for staged) |
| `git log --oneline --graph --all` | history as a compact graph |

## Branches (a branch is just a label pointing at a commit)

| Command | What it does |
|---|---|
| `git switch -c name` | create a branch and move to it |
| `git switch name` | move to an existing branch |
| `git merge name` | bring `name`'s commits into the current branch |
| `git branch -d name` | delete a merged branch |

## Remotes

| Command | What it does |
|---|---|
| `git remote -v` | show where `origin` points |
| `git push -u origin name` | upload a branch (first time) |
| `git pull` | download and merge new commits |
| `git fetch` | download only, don't merge |

## Undo toolbox

| Situation | Command |
|---|---|
| Discard edits to a file (not committed) | `git restore <file>` |
| Unstage a file | `git restore --staged <file>` |
| Fix the last commit message (not pushed) | `git commit --amend` |
| Undo a commit safely (keeps history) | `git revert <commit>` |
| Throw away commits (dangerous, local only) | `git reset --hard <commit>` |

Rule: never rewrite history (`reset`, `amend`, force-push) that other people already have.

## Merge conflicts

Git marks the file like this when both sides changed the same lines:

```
<<<<<<< HEAD
your side
=======
their side
>>>>>>> feature
```

Edit the file to what it should be (delete the three marker lines), then `git add <file>` and `git commit`.

## Habits worth having

- Commit small, commit often, one idea per commit.
- Write messages in the imperative: "Add retry decorator", not "stuff" or "fixed it".
- Run `git status` before every commit.
- Add a `.gitignore` early: `__pycache__/`, `.venv/`, data files, anything secret.
- Never commit passwords, API keys or tokens. If one slips in, treat it as leaked and rotate it.
