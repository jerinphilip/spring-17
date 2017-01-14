#include <opencv2/opencv.hpp>
#include <string>
using namespace cv;
using namespace std;


void video_to_images(const string &output_path, const string &filename){
    VideoCapture capture(filename);
    if(!capture.isOpened()){
        fprintf(stderr, "error opening file.\n");
        return;
    }

    Mat frame;
    string output_file_name;
    int count = 0;
    capture>>frame;

    while(!frame.empty()){
        count = count + 1;
        capture>>frame;
        output_file_name = output_path + "img" + 
                            "_frame_" + to_string(count)
                            + ".jpg";
        printf("In frame %d\n", count);
        printf("> outname = %s\n",output_file_name.c_str());
        bool write_out = imwrite(output_file_name, frame);
        cout<<"Write status: "<<write_out<<endl;
    }
}

int main(int argc, char *argv[]){
    video_to_images("sample-output/", argv[1]);
    return 0;
}
