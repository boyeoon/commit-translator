# Commit Translator

- [ko](docs/README_ko.md)
- [jp](docs/README_jp.md)

This script translates commit messages written in Korean and Japanese into English and formats them according to common commit rules.

## Features
- **Language Support**: Translates commit messages written in Korean and Japanese into English.
- **Automatic Commit Type Detection**: Automatically determines the commit type (feat, fix, chore, etc.) based on the input message.
- **Confirmation Prompt**: After translating the message, users can choose whether to proceed with the commit.

## Usage
### 1. Install Poetry

- If `Poetry` is not installed, install it using the command below:

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

- Add PATH to your shell configuration file (e.g., ~/.bash_profile, ~/.zshrc)

    ```bash
    export PATH="$HOME/.poetry/bin:$PATH"
    ```

    For more details about Poetry, refer to the [official documentation](https://python-poetry.org/docs/)!

#### 1.1. If you don’t want to use Poetry

- If you prefer not to install `Poetry`, you can install the `openai` and `python-dotenv` packages globally. Use the command below to install the packages:

    ```bash
    pip install openai python-dotenv
    ```

### 2. Clone the Repository

- Clone this repository from `GitHub`.

    ```bash
    git clone https://github.com/BoYeonJang/commit-translator.git
    cd commit-translator
    ```

### 3. Set Up Virtual Environment

- Install the required packages using `Poetry`.

    ```bash
    poetry install
    ```

### 4. Set Up OpenAI API Key

- Change the name of the `.env.example` file to `.env` and replace the `your_openai_api_key_here` part with your own OpenAI API key:

    ```bash
    OPENAI_API_KEY="your_openai_api_key_here"
    ```

### 5. File Download and Setup
#### 5.1. File Download:

- Download the `cmtl` file using `curl`:

    ```bash
    curl -O https://gist.githubusercontent.com/BoYeonJang/a49de7f226f668a0cb1185fc808f42cf/raw/6638adae14589273e095cfab270db04c00793489/cmtl
    ```

#### 5.2. File Modification:

- You need to modify the `SCRIPT_DIR` variable:

    ```bash
    vi cmtl
    ```

    ```bash
    3 # =============== Please revise this section ===============
    4 SCRIPT_DIR="/absolute/path/to/commit-translator"
    5 # ==========================================================
    ```

- Here, replace `/absolute/path/to/commit-translator` with the absolute path to your cloned repository.

#### 5.3. Grant Execution Permission and Move to System Path:

- After granting execution permission, move the file to the `/usr/local/bin/` directory for global accessibility:

    ```bash
    chmod +x cmtl && sudo mv cmtl /usr/local/bin/
    ```

#### 5.4 (Optional)

- To skip the prompt asking whether to execute the commit:

    ```bash
    curl -O https://gist.githubusercontent.com/BoYeonJang/93a2d63ba8651a992f3e05e5475e91de/raw/a081a14d87981d9d3b46c667a27f5c565d628c9f/cmtl
    ```

    ```bash
    vi cmtl
    ```

    ```bash
    3 # =============== Please revise this section ===============
    4 SCRIPT_DIR="/absolute/path/to/commit-translator"
    5 # ==========================================================
    ```

    ```bash
    chmod +x cmtl && sudo mv cmtl /usr/local/bin/
    ```

### 6. Using the cmtl Command

- You can now use the `cmtl` command to translate commit messages and commit. For example:

    ```bash
    cmtl "컴포넌트 추가"
    ```

- If you enter in Japanese:

    ```bash
    cmtl "コンポーネント追加"
    ```

## Example
Here’s a simple example of using the script:

Input a Korean message:
```bash
cmtl "버그 수정"
```

Output:
```bash
fix: fix a bug
Do you want to proceed with the commit? (y/n)
```

Input a Japanese message:
```bash
cmtl "バグ修正"
```
Output:
```bash
fix: fix a bug
Do you want to proceed with the commit? (y/n)
```

## Contributing
If you would like to contribute, please fork this repository, apply your modifications, and submit a pull request. All contributions are welcome!

## License
This project follows the [MIT License](https://mit-license.org/).

## Contact
If you have any questions or encounter issues, please reach out via issues.