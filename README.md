# 🚀 P-DESTRE Custom Data Class for Torchreid

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

This repository contains a custom [P-DESTRE](http://p-destre.di.ubi.pt/) data class for torchreid, designed to work seamlessly with the [deep-person-reid](https://github.com/KaiyangZhou/deep-person-reid) framework.
Also conatains a custom data class for tensorflow.

![Custom Data Class Demo](path/to/demo.gif)

## 🌟 Features

- Custom data class for torchreid
- Easy integration with the deep-person-reid framework
- Automatic and manual registration methods
- Detailed instructions for usage

## 📚 Table of Contents

- [Installation](#-installation)
- [Usage](#-usage)
  - [Manual Registration](#manual-registration)
- [Acknowledgements](#-acknowledgements)

## 🔧 Installation

A step-by-step guide on how to install and set up the custom torchreid.data_class.py data class project locally.
  ```sh
# Clone the repositories
git clone git@github.com:kailaspanu/p-destre.di.ubi.pt.git
git clone https://github.com/KaiyangZhou/deep-person-reid.git


# More setup instructions as per torchreid 
```

## 🛠️ Usage

### Manual Registration

Follow these steps to register your custom torchreid.data_class.py data class with torchreid:

1. Place your custom data class file (e.g., `torchreid.data_class.py`) in the `torchreid/data/datasets` folder of the deep-person-reid framework.
2. Add the following code snippet to the `__init__.py` file in the `torchreid/data/datasets` folder:

```python
from .torchreid.data_class import Pdestre
```

## 🙏 Acknowledgements


- Project Inspiration: [deep-person-reid](https://github.com/KaiyangZhou/deep-person-reid)
- Code Inspiration: [SymbolicTemporalPooling](https://github.com/aru05c/SymbolicTemporalPooling)

Thank you!

