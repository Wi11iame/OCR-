from paddleocr import PaddleOCR, draw_ocr
import re
import cv2

class healthCardOCR:
    def __init__(self):
        self.ocr = PaddleOCR(use_angle_cls=True,lang="ch")
        self.recorder = []
    def scan(self, img_path):
        result = self.ocr.ocr(img_path, cls=True)

        ## print出每個字符框內容
        # for idx in range(len(result)):
        #     res = result[idx]
        #     for line in res:
        #         print(line)

        result = result[0]
        txts=   [line[1][0] for line in result]
        for txt in txts:
            if len(txt) == 12 and re.match(r'^0000', txt):
                self.recorder.append(txt)
                # print(txt)
            else:
                pass
        if self.recorder:
            return self.recorder
        else:
            print ("未查詢到健保卡號碼，請重新拍攝。")
            return None
        
        

if __name__ == '__main__':
    # 可直接輸入圖片路徑
    img = cv2.imread('test_noID.jpg')
    a = healthCardOCR()
    recoder = a.scan(img)
    print(recoder)
 

