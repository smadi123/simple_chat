# simple_chat

docker save -o backend_twin2.tar backend_twin2

docker save -o frontend_twin2.tar frontend_twin2

docker load -i backend_twin2.tar


docker load -i frontend_twin2.tar

docker-compose up -d

To create and initialize a GitHub repository for your project in WSL 2 on Windows, follow these steps:

### Step 1: Create a New Project Directory

1. Open your WSL 2 terminal.
2. Navigate to the location where you want to create your project directory.
3. Create a new directory for your project:
   ```bash
   mkdir my-new-project
   cd my-new-project
   ```

### Step 2: Initialize a Local Git Repository

1. Initialize a new Git repository in your project directory:
   ```bash
   git init
   ```

### Step 3: Create a New Repository on GitHub

1. Go to [GitHub](https://github.com/) and log in to your account.
2. Click the "+" icon in the top-right corner and select "New repository."
3. Fill in the repository name, description, and other details.
4. Click "Create repository."

### Step 4: Link Your Local Repository to GitHub

1. Copy the URL of your new GitHub repository. It will look something like `https://github.com/your-username/your-repository.git`.
2. In your WSL 2 terminal, add the GitHub repository as a remote:
   ```bash
   git remote add origin https://github.com/your-username/your-repository.git
   ```

### Step 5: Push Your Local Repository to GitHub

1. Add your project files to the local repository:
   ```bash
   git add .
   ```
2. Commit the files:
   ```bash
   git commit -m "Initial commit"
   ```
3. Push the files to GitHub:
   ```bash
   git push -u origin master
   ```

### Step 6: Keep Your Repository in Sync

To keep your local repository in sync with GitHub, you can use the following commands:

- To pull the latest changes from GitHub:
  ```bash
  git pull origin master
  ```

- To push your local changes to GitHub:
  ```bash
  git add .
  git commit -m "Your commit message"
  git push origin master
  ```

By following these steps, you can create and initialize a GitHub repository for your project and keep it in sync with any modifications.