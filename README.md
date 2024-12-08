# ZAMA GPT Solidity Dev Helper Script

This script streamlines the process of preparing data for training a ZAMA GPT-based Solidity development helper by automating submodule management and file collection.

## GPT Link 🤖

[![Chat with ZAMA Solidity Developer](https://img.shields.io/badge/Chat%20with-ZAMA%20Solidity%20Developer-blue?style=for-the-badge&logo=openai)](https://chatgpt.com/g/g-67518aee3c708191b9f08d077a7d6fa1-zama-solidity-developer)

## Features

1. **Submodule Management**:
   - Automatically adds and updates the following submodules:
     - [`fhevm`](https://github.com/zama-ai/fhevm)
     - [`fhevm-hardhat-template`](https://github.com/zama-ai/fhevm-hardhat-template)
     - [`fhevm-contracts`](https://github.com/zama-ai/fhevm-contracts)

2. **File Collection**:
   - Collects Markdown files, Solidity files, TypeScript files, and README.md files from the submodules based on the following criteria:

   ### From `fhevm` Repository:
   - Collects all Markdown (`.md`) files from the `/docs` folder.

   ### From `fhevm-hardhat-template` Repository:
   - Collects `.ts`, `.sol`, and `README.md` files recursively from these folders:
     - `./contracts`
     - `./deploy`
     - `./tasks`
     - `./test`

   ### From `fhevm-contracts` Repository:
   - Collects `.ts`, `.sol`, and `README.md` files recursively from these folders:
     - `./contracts`
     - `./tasks`
     - `./test/confidentialERC20`
     - `./test/governance`
     - `./test/utils`

3. **Markdown to PDF Conversion**:
   - Converts the collected Markdown files into PDF format for easy reference or training purposes.

4. **Training Guide**:
   - Instructions for training the ZAMA GPT helper are available in the `TRAIN.md` file.

## Usage

### Prerequisites

Ensure you have the following installed:
- **Python 3.8+**
- **Git**
- Required Python packages (install via `pip install -r requirements.txt`)

### Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. To only update submodules:
   ```bash
   python submodules.py
   ```

### Running the Script

To execute the full process:
```bash
python main.py
```

This will:
1. Update submodules to the latest commit on their `main` branches.
2. Collect files based on the specified structure.
3. Generate PDF files from the collected Markdown documents.

### Training the GPT Model

Follow the instructions in the [`TRAIN.md`](./TRAIN.md) file for details on how to train the ZAMA GPT Solidity development helper using the prepared data.

## Repository Structure

```
├── main.py                   # Main script to execute the workflow
├── config.json               # Configuration file for paths and settings
├── collected/                # Directory where collected files are saved
│   ├── markdown/             # Collected Markdown files
│   └── pdfs/                 # Generated PDF files
├── TRAIN.md                  # Instructions for training the GPT model
├── README.md                 # This file
└── requirements.txt          # Python dependencies
```

## Contribution

Contributions are welcome! If you encounter issues or have suggestions, feel free to open a pull request or an issue.

## License

This project is licensed under the MIT License.

--- 

This version provides a clearer, more professional presentation of the script’s purpose and usage, along with a structured explanation of its features and workflow.