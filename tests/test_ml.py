from useless.ml import best_dl_framework


def test_best_dl_framework():
    # Test if the function returns a string
    assert isinstance(best_dl_framework(), str)

    # Test if the function returns a valid framework name
    frameworks = [
        "PyTorch",
        "TensorFlow",
        "JAX",
        "MXNet",
        "Chainer",
        "Theano",
        "Fastai",
        "Keras",
        "Caffe",
        "Caffe2",
        "CNTK",
        "PaddlePaddle",
        "Deeplearning4j",
        "Sonnet",
        "MindSpore",
        "OpenVINO",
        "ONNX",
    ]
    assert best_dl_framework() in frameworks
