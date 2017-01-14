#include <opencv2/opencv.hpp>
#include <string>
#include <vector>
using namespace cv;
using namespace std;

void images_to_video(
        const string &input_path, 
        const string &filename, 
        double fps){
    /* Assumptions: All images are of same size. One output extension */
    string folder = input_path;
    vector<String> filenames;
    glob(folder, filenames);

    VideoWriter out;
    int codec = out.fourcc('X', '2', '6', '4');
    Size frameSize = imread(filenames[0], CV_LOAD_IMAGE_COLOR).size();
    out.open(filename, codec, fps, frameSize, true);

    Mat img; 
    for(auto fn: filenames){
        img = imread(fn, CV_LOAD_IMAGE_COLOR);
        out<<img;
    }
}


int main(int argc, char *argv[]){
    string folder(argv[1]);
    string output(argv[2]);
    images_to_video(folder, output, 60.0);
    return 0;
}
