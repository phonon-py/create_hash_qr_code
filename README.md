# QRコード認証システム
このプロジェクトでは、ユーザー名とパスワードをハッシュ化し、そのハッシュ値を含むQRコードを生成します。さらに、生成されたQRコードを読み取り、ユーザーによるパスワードの入力を通じて認証を行うプログラムを提供します。

## 機能
QRコード発行: ユーザー名とパスワードを組み合わせてハッシュ化し、そのハッシュ値からQRコードを生成します。
QRコード認証: QRコードをスキャンしてハッシュ値を取得し、ユーザーにパスワード入力を求めることで認証を行います。
## 前提条件
このプログラムを実行する前に、以下のライブラリがシステムにインストールされている必要があります。

- Python 3.x
- Pillow
- qrcode
- opencv-python-headless（QRコード読み取り用）
- pyzbar（QRコード読み取り用）
- （macOSの場合）zbar
- （Linuxの場合）libzbar0
## インストール方法
1. 必要なPythonライブラリをインストールします。


`pip install Pillow qrcode opencv-python-headless pyzbar`

2. OSに応じて、必要な追加のインストールを行ってください。

- macOSの場合:

`brew install zbar`
- Linuxの場合:

```sql
sudo apt-get update
sudo apt-get install libzbar0
```
# 使用方法
## QRコードの生成
1.create_hash_qr_code.py スクリプトを実行し、ユーザー名とパスワードを引数に渡します。

```Copy code
python create_hash_qr_code.py username password123
```
2. 実行すると、ユーザー名をファイル名としたQRコードが生成されます。

## QRコードによる認証
1. verify_password_with_qr_code.py スクリプトを実行し、QRコードの画像パスとユーザー名を引数に渡します。

```Copy code
python verify_password_with_qr_code.py username.png username
```
2スクリプトはQRコードを読み取り、コンソール上でパスワードの入力を求めます。入力されたパスワードが初期に設定したものと一致する場合、認証成功のメッセージが表示されます。

## ライセンス
このプロジェクトはMITライセンスの下で公開されています。

## 貢献
プロジェクトへの貢献に興味がある場合は、プルリクエストを送ってください。また、問題が発生した場合は、問題を報告するセクションから報告してください。

