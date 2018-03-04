# Deep Word -rnn-Tensorflow

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)
[![Build Status](https://travis-ci.org/hunkim/word-rnn-tensorflow.svg?branch=master)](https://travis-ci.org/hunkim/word-rnn-tensorflow)


# word-rnn-tensorflow
[![Build Status](https://travis-ci.org/hunkim/word-rnn-tensorflow.svg?branch=master)](https://travis-ci.org/hunkim/word-rnn-tensorflow)

Multi-layer Recurrent Neural Networks (LSTM, RNN) for word-level language models in Python using TensorFlow.
LSTM Long short-term memory [LSTM](https://en.wikipedia.org/wiki/Long_short-term_memory) units (or blocks) are a building unit for layers of a recurrent neural network [RNN](https://en.wikipedia.org/wiki/Recurrent_neural_network)

Mostly reused code from [GIT](https://github.com/hunkim/word-rnn-tensorflow)

# Tools Used
[![Tensorflow](https://upload.wikimedia.org/wikipedia/commons/1/11/TensorFlowLogo.svg)](http://www.tensorflow.org)
[![Anaconda](https://conda.io/docs/_images/conda_logo.svg)](https://anaconda.org/)
[![Python2.7](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)](https://www.python.org/)

Before you start ,setup Tensorflow environemnt in your system. i used CPU's installations using [Conda]



# Basic Usage
To train with default parameters on the input folder, run:
```bash
python train.py
```

To sample from a trained model
```bash
python sample.py
```

To pick using beam search, use the `--pick` parameter. Beam search can be
further customized using the `--width` parameter, which sets the number of beams , `-n` set the number of words 
to search with. For example:
```bash
python sample.py --pick 2 --width 4 -n 100
```



# Deepword-rnn-tensorflow
