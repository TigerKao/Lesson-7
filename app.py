from PIL import Image
import os

for file in os.listdir("original"): # 將在特定資料夾中的檔案使用 OS 模組讀取，如果將 original 換成 "."，會直接讀取跟 app.py 檔案所在的同一個資料夾
    if file.endswith((".jpg", ".jpeg")): # endswith()方法會接收一個元組作為參數，其中包含了你想要檢查的所有可能的後綴。這種方式是正確的，可以正常工作。
        image_file = Image.open(os.path.join("original", file)) # 打開原始檔案
        image_file = image_file.convert("L") # 將圖片轉換成黑白的版本
        image_file.save(os.path.join("result", file[:-4] + "_grey.png"))