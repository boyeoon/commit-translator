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
    
- `.env.example` ファイルの名前を `.env` に変更し、`your_openai_api_key_here` の部分を自分の OpenAI API キーに置き換えます:

    ```bash
    OPENAI_API_KEY="your_openai_api_key_here"
    ```

### 5. ファイルのダウンロードと設定
#### 5.1. ファイルのダウンロード:

- `curl`を使用して`cmtl`ファイルをダウンロードします:

    ```bash
    curl -O https://gist.githubusercontent.com/BoYeonJang/a49de7f226f668a0cb1185fc808f42cf/raw/6638adae14589273e095cfab270db04c00793489/cmtl
    ```

#### 5.2. ファイルの修正:

- `SCRIPT_DIR`変数を修正する必要があります:

    ```bash
    vi cmtl
    ```

    ```bash
    3 # =============== Please revise this section ===============
    4 SCRIPT_DIR="/absolute/path/to/commit-translator"
    5 # ==========================================================
    ```

- ここで、`/absolute/path/to/commit-translator`をクローンしたリポジトリの絶対パスに変更します。

#### 5.3. 実行権限を付与し、システムパスに移動:

- 実行権限を付与した後、ファイルを`/usr/local/bin/`ディレクトリに移動して全体で使用できるように設定します:

    ```bash
    chmod +x cmtl && sudo mv cmtl /usr/local/bin/
    ```

#### 5.4 (オプション)

- コミットを実行するかどうかのプロンプトをスキップするには:

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