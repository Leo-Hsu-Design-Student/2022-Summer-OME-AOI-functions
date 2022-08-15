import cv2
pos = []
def click_xy(event, x, y, flags, params):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'{x}, {y}')

        pos.append((x, y))

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('xy detection', img)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        print(f'{x}, {y}')
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, f'b: {str(b)}' + ',' +
                    f'g: {str(g)}' + ',' + f'r: {str(r)}',
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('xy detection', img)

if __name__ == "__main__":
    img = cv2.imread('1_21.jpg', 1)
    cv2.imshow('xy detection', img)
    cv2.setMouseCallback('xy detection', click_xy)
    
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
    left, upper, right, down = min(pos[0][0], pos[2][0]), min(pos[0][1], pos[1][1])\
        , max(pos[1][0], pos[3][0]), max(pos[2][1], pos[3][1])
    
    #cv2 is img[y, x]
    cropped = img[upper:down, left:right]
    cv2.imshow('cropped', cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(f"the position is: {left} {upper} {right} {down}")
    