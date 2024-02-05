import hashlib
import qrcode

def create_hash_qr_code(username, password):
    # ユーザー名とパスワードを結合してハッシュ値を生成
    combined = f"{username}{password}".encode()
    hash_val = hashlib.sha256(combined).hexdigest()
    
    # ハッシュ値を含むQRコードを生成
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(hash_val)
    qr.make(fit=True)
    
    # QRコードを画像として保存
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{username}.png")
    
    print(f"QR code for {username} has been saved as {username}.png")

# 例: ユーザー名とパスワードを使ってQRコードを生成
create_hash_qr_code('username', 'password123')
