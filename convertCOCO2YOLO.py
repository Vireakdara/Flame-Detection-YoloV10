import json
import os

def convert_coco_to_yolo(coco_data):
    image_list = coco_data['images']
    annotations = coco_data['annotations']
    categories = coco_data['categories']

    yolo_data = []
    category_dict = {}  # Used to store class names and corresponding serial numbers
    for i, category in enumerate(categories):  # Construct a mapping relationship between category names and serial numbers
        category_dict[category['name']] = i

    for image in image_list:
        image_id = image['id']
        file_name = image['file_name']
        width = image['width']
        height = image['height']

        image_annotations = [ann for ann in annotations if ann['image_id'] == image_id]
        yolo_annotations = []
        for ann in image_annotations:
            category_id = ann['category_id']
            category = next((cat for cat in categories if cat['id'] == category_id), None)
            if category is None:
                continue

            bbox = ann['bbox']
            x, y, w, h = bbox
            x_center = x + w / 2
            y_center = y + h / 2
            normalized_x_center = x_center / width
            normalized_y_center = y_center / height
            normalized_width = w / width
            normalized_height = h / height

            yolo_annotations.append({
                'category': category_dict[category['name']],  # Use category number
                'x_center': normalized_x_center,
                'y_center': normalized_y_center,
                'width': normalized_width,
                'height': normalized_height
            })

        if yolo_annotations:
            yolo_annotations.sort(key=lambda x: x['category'])  # Sort by category number
            yolo_data.append({
                'file_name': file_name,
                'width': width,
                'height': height,
                'annotations': yolo_annotations
            })

    return yolo_data, category_dict

path = 'D:\\Dataset\\Flame Detection\\train'  # Modify to the directory path containing the via_export_coco.json file
file_name = '_annotations.coco.json'  # file name
save_dir = 'D:\\Dataset\\Flame Detection\\train\\labels'  # 保存目录
file_path = os.path.join(path, file_name)  # Save Directory

if os.path.isfile(file_path):  # Check if a file exists
    with open(file_path, 'r', encoding='utf-8') as load_f:
        load_dict = json.load(load_f)
        yolo_data, category_dict = convert_coco_to_yolo(load_dict)

    os.makedirs(save_dir, exist_ok=True)  # Create a save directory

    # Generate class.txt file
    class_file_path = os.path.join(save_dir, 'classes.txt')
    with open(class_file_path, 'w', encoding='utf-8') as class_f:
        for category_name, category_index in sorted(category_dict.items(), key=lambda x: x[1]):
            class_f.write(f"{category_name}\n")

    for data in yolo_data:
        file_name = os.path.basename(data['file_name'])  # Extract the file name portion
        width = data['width']
        height = data['height']
        annotations = data['annotations']

        txt_file_path = os.path.join(save_dir, os.path.splitext(file_name)[0] + '.txt')
        with open(txt_file_path, 'w', encoding='utf-8') as save_f:
            for annotation in annotations:
                category = annotation['category']
                x_center = annotation['x_center']
                y_center = annotation['y_center']
                box_width = annotation['width']
                box_height = annotation['height']

                line = f"{category} {x_center:.6f} {y_center:.6f} {box_width:.6f} {box_height:.6f}\n"
                save_f.write(line)

    print("Conversion completed, save to:", save_dir)
else:
    print("File does not exist:", file_path)
