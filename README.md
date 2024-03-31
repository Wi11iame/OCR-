# OCR辨識健保卡號(12碼)
## 說明
此為利用paddleOCR撰寫之辨識健保卡號程式
## python依賴庫
paddleocr `請依照下方說明安裝`
re
python-opencv `可裝可不裝`
## paddleOCR安裝方法
### 1.
``` 
python -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
```
### 2.
```
pip install paddleocr
```
## 使用說明
可直接在`if __name__ == '__main__':`下方自行調適

## 輸入輸出格式說明
1. `input`:可為`ndarray(cv2)`or`圖片路徑`
2. `output`:為`None`或是`recoder:內含辨識到的健保卡號 格式為list`