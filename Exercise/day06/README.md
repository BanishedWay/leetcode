# 生成图片验证码

1. 生成随机颜色
2. 获取指定大小的图片（Image.new）
3. 生成随机数字和字母（random.choice([random_num, random_low_alpha])）
4. 将数字和字母添加到image上（ImageDraw.Draw，Draw.text）
5. 在图片上添加噪点（Draw.line，Draw.arc）
6. 将图片转为Base64编码（BytesIO，base64.encode）


1. ランダムな色を生成する
2. 指定したサイズの画像を取得(Image.new)
3. 乱数と文字を生成します (random.choice([random_num, random_low_alpha]))
4. 画像に数字と文字を追加します (ImageDraw.Draw、Draw.text)
5. 画像にノイズを追加する (Draw.line、Draw.arc)
6. 画像を Base64 エンコード (BytesIO、base64.encode) に変換します。
