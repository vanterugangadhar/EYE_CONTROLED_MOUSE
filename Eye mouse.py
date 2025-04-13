import cv2
import mediapipe as mp
import pyautogui

## Step 1 completed by accessing camera by cv2 and camera
camera=cv2.VideoCapture(0)

## Step 2 to detect the face is present or not by mediapipe anf face_mesh
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w,screen_h=pyautogui.size()

## Step 3 to show the face and landmarks on it
while True:
    _, frame=camera.read()
    frame=cv2.flip(frame,1)
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=face_mesh.process(rgb_frame)
    landmark_points=output.multi_face_landmarks
    frame_h,frame_w,_ =frame.shape
    if landmark_points:
        landmarks=landmark_points[0].landmark
        for id,landmark in enumerate(landmarks[474:478]):
            x=int(landmark.x*frame_w)
            y=int(landmark.y*frame_h)
            cv2.circle(frame,(x,y),3,(0,255,0))
            if id==1:
                screen_x=screen_w/frame_w * x
                screen_y=screen_h/frame_h * y
                pyautogui.moveTo(screen_x,screen_y)
        left=[landmarks[145],landmarks[159]]    ## Step 5 To click is by getting the left eyes upper and lower lid
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame,(x,y),3,(0,255,255))
        if (left[0].y-left[1].y)<0.004:
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow("Eye controlled Mouse",frame)
    cv2.waitKey(1)



    ## Step 1 completed by accessing camera by cv2 and camera
    ## Step 2 to detect the face is present or not by mediapipe anf face_mesh
    ## Step 3 to show the face and landmarks on it
    ## Step 5 To click is by getting the left eyes upper and lower lid

    #### To stop the execution we can come to code and press ctrl+F2
