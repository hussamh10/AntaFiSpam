from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from getFeatures import getFeatures
from getFeatures import getMessageFeatures


def getDataSet():
    X, Y = getFeatures()
    features = len(X[0])
    cases = len(X)

    DS = SupervisedDataSet(features, 1)

    i = 0
    while(i < cases):
        DS.addSample(X[i], Y[i])        
        i+=1

    return DS

def build(length):
    net = buildNetwork(length, 5, 4, 1)
    return net

def train(net, DS):
    trainer = BackpropTrainer(net, DS)
    trainer.trainOnDataset(DS, 100)

def main():

    print("Extracting Features...")
    DS = getDataSet()
    print("Features Extracted")
    print("Building Network...")
    net = build(10)
    print("Network Built")
    print("Training...")
    train(net, DS)
    return net
main()
