import random


def best_dl_framework() -> str:
    """Return the best deep learning framework for you.

    Returns:
        str: The best deep learning framework.
    """
    # This is a subjective opinion, but I would say PyTorch is the best.
    return random.choice(
        [
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
    )
