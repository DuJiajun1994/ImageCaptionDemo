import json


def add_predictions(images, name):
    with open('data/sample/{}.txt'.format(name)) as fid:
        for line in fid:
            image_id = line.split()[0]
            caption = line[len(image_id):].strip()
            images[image_id][name] = caption

if __name__ == '__main__':
    with open('data/dataset_coco.json') as fid:
        data = json.load(fid)
    images = {}
    for image in data['images']:
        if image['split'] != 'test':
            continue
        labels = []
        for sentence in image['sentences']:
            labels.append(sentence['raw'])
        images[str(image['cocoid'])] = {
            'filename': image['filename'],
            'labels': labels
        }
    add_predictions(images, 'xe')
    add_predictions(images, 'rl')
    add_predictions(images, 'im2txt')
    add_predictions(images, 'txt2txt')
    add_predictions(images, 'txt2txt_only_lstm')
    with open('data/images.json', 'w') as fid:
        json.dump(list(images.values()), fid)
