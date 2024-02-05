import cv2
from pyzbar.pyzbar import decode
import hashlib

def verify_password_with_qr_code(qr_code_image_path, username):
    # QRコードを読み取る
    img = cv2.imread(qr_code_image_path)
    decoded_objects = decode(img)
    if not decoded_objects:
        print("QRコードを読み取れませんでした。")
        return
    
    # 読み取ったデータ（ハッシュ値）を取得
    hash_from_qr = decoded_objects[0].data.decode('utf-8')
    print(f"読み取ったハッシュ値: {hash_from_qr}")
    
    # ユーザーにパスワードを入力させる
    input_password = input("パスワードを入力してください: ")
    
    # 入力されたパスワードのハッシュ値を計算
    combined = f"{username}{input_password}".encode()
    input_hash = hashlib.sha256(combined).hexdigest()
    
    # ハッシュ値を検証
    if input_hash == hash_from_qr:
        print("認証成功: パスワードが正しいです。")
    else:
        print("認証失敗: パスワードが間違っています。")

# QRコード画像のパスとユーザー名を指定して関数を実行
verify_password_with_qr_code('username.png', 'username')
