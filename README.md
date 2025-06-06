# Vue Python Devops project

This is a learning project for better understanding of tools and best practices at my current job.

## What I plan to put in here:
- Vue/Nuxt frontend
    - Automated tests on cypress
- Python/Flask backend
    - Automated tests
- On commit push, run eslint
- Github/Gitlab pipelines with autobuild, eslint check

# Setup Instructions


## For running using Skaffold
- Download docker desktop
- Go to settings and enable kubernetes
- Run:
```bash
skaffold dev
```
- Enjoy nice dev experience

## Nuxt/Vue frontend:
```bash
    cd nuxt
    pnpm install          ## PNPM instaed of NPM
    cd ..
    pnpm run dev:nuxt
```

## Python/FastAPI backend:
- You need Python 3.9+ installed on your system
- Clone the repository
- Create and activate a virtual environment
```bash
    cd python_backend
    python -m venv venv
    source venv/Scripts/activate   # (on Windows with Git Bash or use other command for your shell)
```
- Install dependencies
```bash
    pip install -r requirements.txt
```
- Run the server
```bash
    pnpm run dev:py
```

## Once setup correctly, you can run both with Concurrently:
    ```bash
        pnpm run dev
    ```

## Extensions to install in VSCode:
- vue
- Prettier
- Eslint

- Python
- Pylance
- fastApi
- flake8
- black

## For python/fastapi:
