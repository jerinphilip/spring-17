#include <iostream>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
using namespace cv;
using namespace std;

bool isKeyed(Vec3b &cell){
    //int r, g, b;
    int h;
    h = cell[0];
    //bool isKeyed = ((r < 40) and (g > 180) and (b < 80));
    //cout<<"H: "<<h<<endl;
    bool result = (h > 60 and h < 100);
    return result;
}



Size get_smallest(Size s, Size t){
    return Size(
            min(s.width, t.width), 
            min(s.height, t.height));
}

Mat merge_chroma_key(Mat keyed, Mat base){   
    Size requiredSize = get_smallest(keyed.size(), base.size());
    resize(keyed, keyed, requiredSize);
    resize(base, base, requiredSize);
    cout<<"Creating result matrix...";

    Mat result(requiredSize, keyed.type());
    cout<<"Done."<<endl;
    cvtColor(keyed, keyed, CV_BGR2HSV);
    cvtColor(base, base, CV_BGR2HSV);


    // Chroma-key.
    for(int i=0; i<keyed.rows; i++){
        for(int j=0; j<keyed.cols; j++){
            Vec3b kval, bval;
            kval = keyed.at<Vec3b>(i, j);
            bval = base.at<Vec3b>(i, j);
            if(isKeyed(kval)){
                result.at<Vec3b>(i, j) = bval;
            }
            else{
                result.at<Vec3b>(i, j) = kval;
            }
        }
    }

    return result;
}


void videoMerge(
        const string &green_file,
        const string &base_file,
        const string &output_file){

    cout<<"Opening files: ";
    cout<<"{green: "<<green_file<<"},";
    cout<<"{base: "<<base_file<<"},";
    cout<<"{output: "<<output_file<<"}"<<endl;
    VideoCapture green(green_file), base(base_file); 
    VideoWriter out;
    int codec = out.fourcc('X', '2', '6', '4');
    Mat green_f, base_f;
    green >> green_f;
    base >> base_f;


    Size frameSize = get_smallest(green_f.size(), base_f.size());
    double fps = min(green.get(CV_CAP_PROP_FPS), base.get(CV_CAP_PROP_FPS));
    cout<<"Opening output stream..";
    out.open(output_file, codec, fps, frameSize, true);
    cout<<"Done."<<endl;

    while ( !green_f.empty() and !base_f.empty()){
        /*
        imshow("debug", green_f);
        waitKey(0);

        imshow("debug", base_f);
        waitKey(0);
        */
        cout<<"Merging...";
        Mat result = merge_chroma_key(green_f, base_f);
        cvtColor(result, result, CV_HSV2BGR);
        cout<<"Done."<<endl;
        //imshow("debug", result);
        //waitKey(1000/24.0);
        out<<result;
        green >> green_f;
        base >> base_f;
    }
}

int main(int argc, char *argv[]){
    namedWindow("debug", CV_WINDOW_NORMAL);
    string green_file = argv[1];
    string base_file = argv[2];
    string output_file = argv[3];
    videoMerge(green_file, base_file, output_file);
    return 0;
}
