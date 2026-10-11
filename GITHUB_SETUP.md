# Publish this project to GitHub

Follow these steps on your machine. Do **not** commit `.env` files (they are gitignored).

## Before you push

1. Copy environment templates:
   - `backend/restaurant-reservation-system/.env.example` → `.env`
   - `frontend/Gen AI FE/Gen AI FE/.env.example` → `.env`
2. Confirm `.env` is **not** tracked: `git status` should not list `.env`.
3. **Monorepo vs existing backend repo:** The backend folder contains a nested git history pointing to `nima-karimi-capgemini/restaurant-reservation-system`. For **one** portfolio repo with frontend + backend, remove the nested repo metadata once (only if you want a single repo):

   ```powershell
   Remove-Item -Recurse -Force "backend\restaurant-reservation-system\.git"
   ```

   Skip this step if you prefer to keep pushing only the backend to the existing GitHub repository.

## Option A — New monorepo on your GitHub account

From the folder that contains this `README.md` (`Digital_Hackers_Team_Source_Code`):

```powershell
git init
git add .
git status
git commit -m "Add AI restaurant reservation hackathon project (frontend + backend)"
```

Create an empty repository on GitHub (no README), then:

```powershell
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

## Option B — Update the existing backend remote

If you only publish the backend and your team owns the repo:

```powershell
cd backend\restaurant-reservation-system
git add .
git status
git commit -m "Document API, fix agent import, add CORS and run script"
git push origin main
```

Add the frontend in a second repo or migrate to a monorepo later.

## GitHub profile tips

- Add topics: `aws`, `amazon-bedrock`, `generative-ai`, `fastapi`, `react`, `dynamodb`, `hackathon`
- Pin the repository on your profile
- Add 2–3 screenshots (home page, reservation form, staff dashboard) in the README if you have time

## Authentication

If `git push` asks for credentials, use a [GitHub personal access token](https://github.com/settings/tokens) or GitHub CLI:

```powershell
gh auth login
gh repo create YOUR_REPO_NAME --public --source=. --remote=origin --push
```
