import ID3, parse, random
import matplotlib.pyplot as plt


def plotter(inFile):
    pruneAverages = []
    nopruneAverages = []
    trainingSizes = []
    for x in range(1, 3):
        mytuple = plot(inFile, x*10)
        trainingSizes.append(x*10)
        pruneAverages.append(mytuple[0])
        nopruneAverages.append(mytuple[1])
    plt.plot(trainingSizes, pruneAverages, "g^-")
    plt.plot(trainingSizes, nopruneAverages, "bs-")
    plt.ylabel("Accuracy")
    plt.xlabel("Data Size")
    plt.show()


def plot(inFile, training_size):
    withPruning = []
    withoutPruning = []
    testsize = 435 - training_size
    data = parse.parse(inFile)
    for i in range(3):
        random.shuffle(data)
        train = data[:7*len(data)/10]
        valid = data[7*len(data)/10:testsize]
        test = data[testsize:]

        tree = ID3.ID3(train, 'democrat')
        acc = ID3.test(tree, train)
        # print "training accuracy: ",acc
        acc = ID3.test(tree, valid)
        # print "validation accuracy: ",acc
        acc = ID3.test(tree, test)
        print "test accuracy: ",acc

        ID3.prune(tree, valid)
        acc = ID3.test(tree, train)
        # print "pruned tree train accuracy: ",acc
        acc = ID3.test(tree, valid)
        # print "pruned tree validation accuracy: ",acc
        acc = ID3.test(tree, test)
        # print "pruned tree test accuracy: ",acc
        withPruning.append(acc)
        tree = ID3.ID3(train+valid, 'democrat')
        acc = ID3.test(tree, test)
        # print "no pruning test accuracy: ",acc
        withoutPruning.append(acc)
    # plot(train)
    # print withPruning
    # print withoutPruning
    # print "average with pruning",sum(withPruning)/len(withPruning)," without: ",sum(withoutPruning)/len(withoutPruning)
    pruneAvg = sum(withPruning)/len(withPruning)
    nopruneAvg = sum(withoutPruning)/len(withoutPruning)
    return (pruneAvg, nopruneAvg)


if __name__ == "__main__":
    plotter("house_votes_84.data")
