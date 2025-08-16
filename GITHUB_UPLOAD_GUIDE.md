# GitHub Upload and PyPI Publishing Guide for prompt2json

This guide will help you upload your `prompt2json` package to GitHub and publish it to PyPI so users can install it with `pip install prompt2json`.

## Step 1: Upload to GitHub

### 1.1 Create a GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Repository name: `prompt2json`
5. Description: "A Python library for converting prompts to JSON format"
6. Make it **Public** (required for PyPI)
7. **DO NOT** initialize with README (you already have one)
8. Click "Create repository"

### 1.2 Upload Your Code to GitHub

Open your terminal in the `d:\GitHub\prompt2json` directory and run these commands:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: prompt2json library v0.1.0"

# Add your GitHub repository as remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/prompt2json.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME` with your actual GitHub username!**

### 1.3 Create a Release Tag

```bash
# Create and push a version tag
git tag v0.1.0
git push origin v0.1.0
```

## Step 2: Publish to PyPI

### 2.1 Install Required Tools

```bash
pip install build twine
```

### 2.2 Create PyPI Account

1. Go to [PyPI.org](https://pypi.org)
2. Click "Register" and create an account
3. Verify your email address

### 2.3 Build Your Package

```bash
# Clean any previous builds
rmdir /s prompt2json.egg-info
rmdir /s dist
rmdir /s build

# Build the package
python -m build
```

### 2.4 Test on TestPyPI (Recommended)

1. Create account on [TestPyPI](https://test.pypi.org)
2. Upload to TestPyPI first:

```bash
python -m twine upload --repository testpypi dist/*
```

3. Test installation from TestPyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ prompt2json
```

### 2.5 Upload to PyPI

Once testing is successful:

```bash
python -m twine upload dist/*
```

Enter your PyPI username and password when prompted.

## Step 3: Verify Installation

After successful upload, anyone can install your package:

```bash
pip install prompt2json
```

## Step 4: Update Your GitHub Repository

### 4.1 Add Installation Badge to README

Add this badge to the top of your README.md:

```markdown
[![PyPI version](https://badge.fury.io/py/prompt2json.svg)](https://badge.fury.io/py/prompt2json)
[![Python versions](https://img.shields.io/pypi/pyversions/prompt2json.svg)](https://pypi.org/project/prompt2json/)
```

### 4.2 Create GitHub Release

1. Go to your GitHub repository
2. Click "Releases" → "Create a new release"
3. Tag: `v0.1.0`
4. Title: `prompt2json v0.1.0`
5. Description: Copy from your README or changelog
6. Click "Publish release"

## Step 5: Future Updates

When you want to release a new version:

1. Update version in `setup.py` and `pyproject.toml`
2. Update `__init__.py` version
3. Commit changes:
   ```bash
   git add .
   git commit -m "Release v0.1.1"
   git tag v0.1.1
   git push origin main
   git push origin v0.1.1
   ```
4. Rebuild and upload:
   ```bash
   python -m build
   python -m twine upload dist/*
   ```

## Troubleshooting

### Common Issues:

1. **Package name already exists**: Choose a different name
2. **Authentication failed**: Use API tokens instead of passwords
3. **Build fails**: Check your `setup.py` and `pyproject.toml` syntax

### API Token Setup (Recommended):

1. Go to PyPI → Account Settings → API tokens
2. Create a new token
3. Use `__token__` as username and your token as password

## Security Best Practices

1. Never commit API tokens to git
2. Use `.gitignore` for sensitive files
3. Enable 2FA on PyPI account
4. Use API tokens instead of passwords

## Resources

- [PyPI Publishing Guide](https://packaging.python.org/tutorials/packaging-projects/)
- [GitHub Documentation](https://docs.github.com/)
- [Python Packaging User Guide](https://packaging.python.org/)

---

**Your package is ready for publication! Follow these steps and users will be able to install it with `pip install prompt2json`.**