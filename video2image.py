import cv2

def save_image(image, addr, num):
    address = addr + str(num) + '.jpg'
    cv2.imwrite(address, image)

if __name__ == '__main__':
    video_path = 'true.avi'
    out_path = './stomach_image/' 
    is_all_frame = True

    time_interval = 1

    video = cv2.VideoCapture(video_path)
    success, frame = video.read()
    print(success)

    i = 0
    j = 0
    if is_all_frame:
        time_interval = 1

    while success:
        i = i + 1
        if(i % time_interval == 0):
            j = j +1
            print('save frame:', i)
            save_image(frame, out_path, j)

        success, frame = video.read()

