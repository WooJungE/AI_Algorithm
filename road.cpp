//차선검출...
#include <opencv2/opencv.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace cv;

int main()
{
    // 비디오를 로드합니다.
    VideoCapture cap("road.mp4");
    if (!cap.isOpened()) {
        std::cout << "Video file cannot be opened" << std::endl;
        return -1;
    }

    Mat frame, hsvImage, maskWhite, maskYellow, mask, grayImage, blurImage, edgesImage;
    std::vector<Vec4i> lines;

    while (true) {
        // 프레임을 읽습니다.
        cap >> frame;
        if (frame.empty()) {
            break;
        }

        // HSV 색공간으로 변환합니다.
        cvtColor(frame, hsvImage, COLOR_BGR2HSV);

        // 흰색 마스크를 생성합니다.
        inRange(hsvImage, Scalar(0, 0, 200), Scalar(180, 25, 255), maskWhite);

        // 노란색 마스크를 생성합니다.
        inRange(hsvImage, Scalar(20, 100, 100), Scalar(30, 255, 255), maskYellow);

        // 흰색 및 노란색 마스크를 결합합니다.
        mask = maskWhite | maskYellow;

        // 그레이스케일로 변환합니다.
        cvtColor(frame, grayImage, COLOR_BGR2GRAY);

        // 마스크를 적용합니다.
        grayImage &= mask;

        // 가우스 블러를 적용하여 노이즈를 제거합니다.
        GaussianBlur(grayImage, blurImage, Size(5, 5), 0, 0);

        // Canny edge detection을 적용합니다.
        Canny(blurImage, edgesImage, 50, 150);

        // Hough Transform을 적용하여 직선을 검출합니다.
        HoughLinesP(edgesImage, lines, 1, CV_PI / 180, 50, 50, 10);

        // 검출한 직선을 그립니다.
        for (size_t i = 0; i < lines.size(); i++) {
            Vec4i l = lines[i];
            line(frame, Point(l[0], l[1]), Point(l[2], l[3]), Scalar(0, 0, 255), 3, LINE_AA);
        }

        // 결과를 출력합니다.
        imshow("Lane Detection", frame);

        // 'q' 키를 누르면 종료합니다.
        if (waitKey(1) == 'q')
            break;
    }

    return 0;
}
