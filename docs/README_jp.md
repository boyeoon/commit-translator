# コミット翻訳機
このスクリプトは、韓国語や日本語で書かれたコミットメッセージを英語に翻訳し、一般的なコミット規則に従ってフォーマットします。

## 主な機能
- **言語サポート**: 日本語や韓国語で書かれたコミットメッセージを英語に翻訳します。
- コミットタイプの自動検出**: 入力されたメッセージに基づいてコミットタイプ（feat、fix、choreなど）を自動的に決定します。
- **確認プロンプト**: 翻訳されたメッセージを確認した後、ユーザーはコミットを進めるかどうかを選択できます。

## 使い方
### 1. Poetryのインストール

- `Poetry`がインストールされていない場合は、以下のコマンドを使用してインストールします。
   
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

- シェル設定ファイルにPATHを追加します（例: ~/.bash_profile, ~/.zshrc）

    ```bash
    export PATH="$HOME/.poetry/bin:$PATH"
    ```

    Poetryの詳細については、[公式ドキュメント](https://python-poetry.org/docs/)を参照してください！

#### 1.1. Poetryを使用しない場合

- `Poetry`をインストールしたくない場合は、`openai`と`python-dotenv`パッケージをグローバルにインストールできます。以下のコマンドを使用してパッケージをインストールします:

    ```bash
    pip install openai python-dotenv
    ```

### 2. リポジトリのクローン
    
- `GitHub`からこのリポジトリをクローンします。
   
    ```bash
    git clone https://github.com/BoYeonJang/commit-translator.git
    cd commit-translator
    ```

### 3. 仮想環境の設定

- `Poetry`を使用して必要なパッケージをインストールします。

    ```bash
    poetry install
    ```

### 4. OpenAI　APIキーの設定
    
- プロジェクトのルートディレクトリに`.env`ファイルを作成し、APIキーを追加します。

    ```bash
    echo 'OPENAI_API_KEY="your_openai_api_key_here"' > .env
    ```

### 5. グローバルコマンド設定
#### 5.1 スクリプトファイルの作成

- `/usr/local/bin/` パスに `cmtl` という名前のファイルを作成し、以下の内容を追加します:

    ```bash
    SCRIPT_DIR="/path/to/commit-translator"

    WHITE="\033[1;37m"
    CYAN="\033[1;36m"
    RESET="\033[0m"

    if [ "$#" -eq 0 ]; then
        echo "Usage: cmtl \"commit message\""
        exit 1
    fi

    message="$*"

    commit_message=$(poetry run python "$SCRIPT_DIR/translate.py" "$message")

    echo "Translated commit message: ${CYAN}$commit_message${RESET}"
    echo -n "${WHITE}Do you want to proceed with the commit?${RESET} > ${CYAN}(y/n)${RESET} "

    read -r response
    if [[ "$response" == "y" ]]; then
        git commit -m "$commit_message"
        echo "commit successful!"
    else
        echo "commit canceled."
    fi
    ```

- ここで、`/path/to/commit-translator` はクローンしたリポジトリの絶対パスに変更してください。

#### 5.2 (オプション)

- コミットを実行するかどうかのプロンプトをスキップするには:

    ```bash
    SCRIPT_DIR="/path/to/commit-translator"

    CYAN="\033[1;36m"
    RESET="\033[0m"

    if [ "$#" -eq 0 ]; then
        echo "Usage: cmtl \"commit message\""
        exit 1
    fi

    message="$*"

    commit_message=$(poetry run python "$SCRIPT_DIR/translate.py" "$message")

    echo "Translated commit message: ${CYAN}$commit_message${RESET}"

    # 커밋을 즉시 실행
    git commit -m "$commit_message"
    echo "commit successful!"
    ```

#### 5.3 実行権限の付与

- スクリプトに実行権限を付与します:

    ```bash
    sudo chmod +x /usr/local/bin/cmtl
    ```

### 6. cmtlコマンドの使用

- これで`cmtl`マンドを使用してコミットメッセージを翻訳し、コミットできます。例えば:

    ```bash
    cmtl "コンポーネント追加"
    ```

- 韓国語で入力する場合:

    ```bash
    cmtl "컴포넌트 추가"
    ```

## インストール方法
このスクリプトをグローバルに使用できるように設定するには、以下のコマンドを使用して`cmtl`コマンドを`/usr/local/bin`にコピーします。

```bash
sudo cp translate.py /usr/local/bin/cmtl
```
これでターミナルから直接`cmtl`コマンドを使用できます。

#### (オプション)

インストールしたくない場合:
```bash
python translate.py "コミットメッセージ"
```

## 例
スクリプトを使用する簡単な例です:

日本語メッセージ入力:
```bash
cmtl "バグ修正"
```

出力:
```bash
fix: fix a bug
Do you want to proceed with the commit? (y/n)
```

韓国語メッセージ入力:
```bash
cmtl "버그 수정"
```

出力:
```bash
fix: fix a bug
Do you want to proceed with the commit? (y/n)
```

## 貢献方法
貢献を希望される場合は、このリポジトリをフォークし、修正を適用してプルリクエストを送信してください。すべての貢献を歓迎します！

## ライセンス
このプロジェクトは[MITライセンス](https://mit-license.org/)に従います。

## お問い合わせ
質問や問題が発生した場合は、イシューを通じてお問い合わせください。