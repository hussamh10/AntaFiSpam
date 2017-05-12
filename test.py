from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from getFeatures import getFeatures
from getFeatures import getMessageFeatures
from pybrain.utilities import percentError

import network

def test(net, data, trainer):
    result = percentError(trainer.testOnClassData(dataset = data), data['target'])
    print(result)


def main():
    print("Extracting Features...")
    Training_DS, Testing_DS = network.getDataSet()
    print("Features Extracted")
    print("Building Network...")

    net = network.build(10)

    print("Network Built")
    print("Training...")

    trainer = network.train(net, Training_DS, epoch = 300)
    print("Trained")
    print("Testing..")
    test(net, Testing_DS, trainer)

    return net

if __name__ == "__main__":
    main()
