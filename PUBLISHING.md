# Publishing Guide for prompt2json

This guide explains how to publish the `prompt2json` package to PyPI so users can install it with `pip install prompt2json`.

## Prerequisites

1. **PyPI Account**: Create accounts on both [PyPI](https://pypi.org/account/register/) and [TestPyPI](https://test.pypi.org/account/register/)
2. **API Tokens**: Generate API tokens for both PyPI and TestPyPI
3. **Required Tools**: Install publishing tools

```bash
pip install build twine
```

## Step-by-Step Publishing Process

### 1. Prepare the Package

Ensure all files are ready:
- [ ] Update version in `setup.py`, `pyproject.toml`, and `__init__.py`
- [ ] Update `CHANGELOG.md` with new features
- [ ] Ensure `README.md` is complete and accurate
- [ ] Run tests to ensure everything works

```bash
# Run tests
pytest tests/

# Check code quality
black prompt2json/
flake8 prompt2json/
```

### 2. Build the Package

```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info/

# Build the package
python -m build
```

This creates:
- `dist/prompt2json-0.1.0.tar.gz` (source distribution)
- `dist/prompt2json-0.1.0-py3-none-any.whl` (wheel distribution)

### 3. Test on TestPyPI (Recommended)

First, test your package on TestPyPI:

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*
```

You'll be prompted for:
- Username: `__token__`
- Password: Your TestPyPI API token

Test installation from TestPyPI:

```bash
# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ prompt2json

# Test the installation
python -c "from prompt2json import convert_prompt_to_json; print('Success!')"
```

### 4. Publish to PyPI

Once testing is successful, publish to the real PyPI:

```bash
# Upload to PyPI
twine upload dist/*
```

You'll be prompted for:
- Username: `__token__`
- Password: Your PyPI API token

### 5. Verify Installation

Test that users can install your package:

```bash
# Install from PyPI
pip install prompt2json

# Test CLI
prompt2json "Test prompt"

# Test Python API
python -c "from prompt2json import convert_prompt_to_json; print(convert_prompt_to_json('test'))"
```

## Configuration Files

### `.pypirc` Configuration

Create `~/.pypirc` to store repository configurations:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = <your-pypi-api-token>

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = <your-testpypi-api-token>
```

### GitHub Actions (Optional)

Create `.github/workflows/publish.yml` for automated publishing:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    - name: Build package
      run: python -m build
    - name: Publish to PyPI
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
      run: twine upload dist/*
```

## Version Management

### Semantic Versioning

Follow [semantic versioning](https://semver.org/):
- `MAJOR.MINOR.PATCH` (e.g., `1.2.3`)
- `MAJOR`: Breaking changes
- `MINOR`: New features (backward compatible)
- `PATCH`: Bug fixes (backward compatible)

### Update Version Numbers

Update version in these files:
1. `setup.py`: `version="0.1.0"`
2. `pyproject.toml`: `version = "0.1.0"`
3. `prompt2json/__init__.py`: `__version__ = "0.1.0"`
4. `prompt2json/cli.py`: `version="%(prog)s 0.1.0"`

## Troubleshooting

### Common Issues

1. **Package name already exists**:
   - Choose a different name
   - Check availability: `pip search prompt2json`

2. **Upload fails with 403 error**:
   - Check API token permissions
   - Ensure you're the package owner

3. **Import errors after installation**:
   - Check `__init__.py` imports
   - Verify package structure

4. **Missing files in distribution**:
   - Update `MANIFEST.in`
   - Check `pyproject.toml` includes

### Validation Commands

```bash
# Check package metadata
twine check dist/*

# Validate setup.py
python setup.py check

# Test local installation
pip install -e .
```

## Post-Publication

1. **Tag the release** in Git:
   ```bash
   git tag v0.1.0
   git push origin v0.1.0
   ```

2. **Create GitHub release** with changelog

3. **Update documentation** if needed

4. **Announce** on relevant platforms

## Security Best Practices

1. **Use API tokens** instead of passwords
2. **Store tokens securely** (environment variables, GitHub secrets)
3. **Enable 2FA** on PyPI account
4. **Review permissions** regularly
5. **Use trusted publishers** when possible

## Resources

- [PyPI Publishing Guide](https://packaging.python.org/tutorials/packaging-projects/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Python Packaging User Guide](https://packaging.python.org/)
- [Semantic Versioning](https://semver.org/)

---

**Remember**: Always test on TestPyPI first before publishing to the main PyPI!