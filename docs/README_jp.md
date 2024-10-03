# コミット翻訳機
このスクリプトは、韓国語や日本語で書かれたコミットメッセージを英語に翻訳し、一般的なコミット規則に従ってフォーマットします。

## 主な機能
- **言語サポート**: 韓国語や日本語で書かれたコミットメッセージを英語に翻訳します。
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

- `Poetry`をインストールしたくない場合は、`openai`と`python-dotenv`パッケージをグローバルにインストールできます。以下のコマンドを使用してパッケージをインストールします：

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

### 5. zshの設定

- シェル設定ファイルを開き、`cmtl`関数を追加します。

    ```bash
    function cmtl() {
        if [ "$#" -eq 0 ]; then
            echo "Usage: cmtl \"commit message\""
            return 1
        fi
        
        message="$*"
        
        commit_message=$(poetry run python /path/to/your/translate.py "$message")
        
        git commit -m "$commit_message"
    }
    ```

- `/path/to/your/translate.py`部分は、実際のスクリプトのパスに置き換えてください。

#### 5.1 (オプション)

- コミットが行われる前にキャンセルしたい場合は：

    ```bash
    function cmtl() {
        if [ "$#" -eq 0 ]; then
            echo "Usage: cmtl \"commit message\""
            return 1
        fi
        
        message="$*"

        commit_message=$(poetry run python /path/to/your/translate.py "$message")
        
        echo "Translated commit message: $commit_message"
        echo "Do you want to proceed with the commit? (y/n)"
        
        read -r response
        if [[ "$response" == "y" ]]; then
            git commit -m "$commit_message"
            echo "commit successful!"
        else
            echo "commit canceled."
        fi
    }
    ```
    

- 変更を保存します：
    ```bash
    source ~/.zshrc
    ```

### 6. cmtlコマンドの使用

- これで`cmtl`マンドを使用してコミットメッセージを翻訳し、コミットできます。例えば：

    ```bash
    cmtl "コンポーネント追加"
    ```

- 韓国語で入力する場合：

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

インストールしたくない場合：
```bash
python translate.py "コミットメッセージ"
```

## 例
スクリプトを使用する簡単な例です：

日本語メッセージ入力：
```bash
cmtl "バグ修正"
```

출력:
```bash
fix: fix a bug
Do you want to proceed with the commit? (y/n)
```

韓国語メッセージ入力：
```bash
cmtl "버그 수정"
```

出力：
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