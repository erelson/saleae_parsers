
import sliderparser

import matplotlib as plt

from matplotlib import pyplot



if __name__ == '__main__':
    #fr = open("quick.csv", 'r')
    #fr = open("SliderOutput2Mhz_001.csv", 'r')
    #data, times = sliderparser.get_packets(fr, 1, 0)
    #fr = open("SliderOutput_in_negToPos_25Msamp_8MHz.csv", 'r')
    fr = open("SliderOutput_mm_negToPos_25Msamp_8MHz_002.csv", 'r')
    data, times = sliderparser.get_packets(fr)
    fr.close()
    #data = get_packets(fr)
    print len(data), "packets parsed"
    #for line in data[:10]: print line

    numbers = sliderparser.parse_packets(data, times)
    #for number in numbers[:10]: print number

    #fig = plt.plot(times, numbers)

    #plt.show()

    zeroOffset = 4000

    pyplot.subplot(3,1,1)
    pyplot.plot(times, numbers)
    pyplot.subplot(3,1,2)
    pyplot.plot(times, [-1*(number-zeroOffset)*6.374/8160 for number in numbers])
    pyplot.subplot(3,1,3)
    pyplot.plot(times, [-1*(number-zeroOffset)*161.91/8160 for number in numbers])
    pyplot.show()

    print min(numbers)
    print max(numbers)
    print max(numbers) - min(numbers)


    #times = [times[x] for x in xrange(len(data)) if len(data[x]) == 21]
    #data = [data[x] for x in xrange(len(data)) if len(data[x]) == 21]
    #print len(data), "packets parsed"

    #x = 0#12 

    #pyplot.subplot(6,4,1)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][0+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,2)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][1+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,3)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][2+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,4)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][3+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,5)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][4+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,6)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][5+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,7)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][6+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,8)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][7+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,9)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][8+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,10)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][9+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,11)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][10+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,12)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][11+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,13)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][12+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,14)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][13+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,15)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][14+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,16)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][15+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,17)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][16+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,18)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][17+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,19)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][18+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,20)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][19+x] for i in xrange(len(data))])
    #pyplot.subplot(6,4,21)
    #pyplot.ylim(-.1,1.1)
    #pyplot.plot(times, [data[i][20+x] for i in xrange(len(data))])

    #pyplot.show()
