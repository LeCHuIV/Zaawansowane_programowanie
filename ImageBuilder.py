from Detector import DetectorAPI, run_model, visualize, cv


def image_build() -> None:
    api = DetectorAPI(
        r'C:/Users/Patryk Lech/Downloads/frozen_inference_graph.pb',
        r'C:/Users/Patryk Lech/Downloads/test.jpg')
    graph = api.read_graph()
    cols, rows, inp, img = api.read_and_preprocess_image()
    out = run_model(graph, inp)
    visualize(out, cols, rows, img)
    cv.imshow('image', img)
    cv.waitKey()
    cv.destroyAllWindows()