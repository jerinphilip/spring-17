#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>
#include <string>
using namespace cv;
using namespace std;

int main(int argc, char *argv[]){
    string savepath = argv[1];
    VideoCapture capture(0);
    namedWindow("display", CV_WINDOW_NORMAL);
    cout<<"FPS: "<<CAP_PROP_FPS<<endl;
    Mat frame;
    for(int frame_number=1; ;frame_number++){
        capture>>frame;
        string filename = savepath + to_string(frame_number) + ".jpg";
        imwrite(filename, frame);
        imshow("display", frame);
        waitKey(1000/30.0);
    }
    return 0;
}
