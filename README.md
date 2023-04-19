# 🚀 Custom Data Class for Torchreid

![GitHub release (latest by date)](https://img.shields.io/github/v/release/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME?style=flat-square)
![GitHub](https://img.shields.io/github/license/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME?style=flat-square)
![GitHub stars](https://img.shields.io/github/stars/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME?style=flat-square)
![GitHub forks](https://img.shields.io/github/forks/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME?style=flat-square)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

This repository contains a custom data class for torchreid, designed to work seamlessly with the [deep-person-reid](https://github.com/KaiyangZhou/deep-person-reid) framework.

![Custom Data Class Demo](path/to/demo.gif)

## 🌟 Features

- Custom data class for torchreid
- Easy integration with the deep-person-reid framework
- Automatic and manual registration methods
- Detailed instructions for usage

## 📚 Table of Contents

- [Installation](#-installation)
- [Usage](#-usage)
  - [Automatic Registration](#automatic-registration)
  - [Manual Registration](#manual-registration)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

## 🔧 Installation

A step-by-step guide on how to install and set up the custom data class project locally.
  ```sh
# Clone the repositories
git clone git@github.com:kailaspanu/p-destre.di.ubi.pt.git
git clone https://github.com/KaiyangZhou/deep-person-reid.git

# Navigate to the custom data class project folder
cd p-destre.di.ubi.pt

# Install the required dependencies
pip install -r requirements.txt

# More setup instructions as per torchreid 
```

## 🛠️ Usage

### Automatic Registration

Follow these steps to automatically register your custom data class with torchreid:

1. Place your custom data class file (e.g., `torchreid.py`) in the `torchreid/data/datasets` folder of the deep-person-reid framework.
2. Add the following code snippet to the `__init__.py` file in the `torchreid/data/datasets` folder:

```python
from .custom_data import CustomData
```
