## Performance on a Flame dataset YOLOv10
[Flame Dataset](https://drive.google.com/file/d/13GZaa0A62msXdcS6z9_9k1aLfSh41d-F/view?usp=drive_link)
Train: 3500 pics
Val: 500 pics
- Validate Flame dataset (input size: 640x640)
  
| Model       | Test Size   | Parameters  | FLOPs       | mAP50       |   mAP50-95 | Best Epoch |
| ----------- | ----------- | ----------- | ----------- | ----------- |----------- |----------- |
| [YOLOv10-N](https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov10n.pt)   |      640    |      2.6M   |      8.2G   |    0.472    |        0.22 |       68 |
| [YOLOv10-S](https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov10s.pt)   |      640    |    4.2 M     |   24.8G      |    0.601  |  0.439      |    200   |
| [YOLOv10-M](https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov10m.pt)   |      640    |         |         |        |         |        |
| [YOLOv10-L](https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov10l.pt)   |      640    |         |         |        |         |        |

## Installation
`conda` virtual environment is recommended. 
```
conda create -n yolov10 python=3.9
conda activate yolov10
pip install -r requirements.txt
pip install -e .
```

## Training 
```
yolo detect train data=coco.yaml model=yolov10n/s/m/l.yaml epochs=100 batch=256 imgsz=640 device=0
```
Or
```python
from ultralytics import YOLOv10

model = YOLOv10.from_pretrained('jameslahm/yolov10{n/s/m/l}')
# or
# wget https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10{n/s/m/l}.pt
model = YOLOv10('yolov10{n/s/m/l}.pt')

model.val(data='coco.yaml', batch=16)
```


## Validation
[`yolov10n`](https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov10n.pt)  [`yolov10s`](https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov10s.pt)  [`yolov10m`](https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov10m.pt)  [`yolov10l`](https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov10l.pt)   
```
yolo val model=jameslahm/yolov10{n/s/m/l} data=coco.yaml batch=16
```

Or
```python
from ultralytics import YOLOv10

model = YOLOv10.from_pretrained('jameslahm/yolov10{n/s/m/l}')
# or
# wget https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10{n/s/m/l}.pt
model = YOLOv10('yolov10{n/s/m/l}.pt')

model.val(data='coco.yaml', batch=16)
```

## Prediction 
```
yolo mode=predict model=runs\detect\train10\weights\best.pt source=testing\1.jpg       
```
![1](https://github.com/user-attachments/assets/1f60c445-3837-4fb9-b789-98b10368b121)

Result 

![1](https://github.com/user-attachments/assets/fb46d6c2-7df4-46c1-a144-bbf7b93b8c38)

Live Web Cam
```
yolo mode=predict model=runs\detect\train10\weights\best.pt source=0 show=true conf=0.1       
```
[LINK](https://youtu.be/nynWAYpcQDQ)

Video

```
yolo mode=predict model=runs\detect\train10\weights\best.pt source=testing\v1.mp4 conf=0.1    
```
[LINK](https://youtu.be/gJME_dpIncw)


