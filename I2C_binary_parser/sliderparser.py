
"""
"""


def get_packets(fr, scl=0, sda=1):
    """

    Parameters
    ----------
    fr - opened file reader object
        ...
    scl - int (optional)
        Channel number of clock signal (really column number in output,
        not including timestamps column). Default=%default
    sda - int (optional)
        Channel number of data signal (really column number in output,
        not including timestamps column). Default=%default

    Notes
    -----
    Output taken, e.g. from the Saleae Logic device, corresponds with timestamps
    where the level in any channel has changed; i.e. only a single entry in the
    data will exist for a period where all channels are constant.
    """

    idxcl = 1 + scl
    idxda = 1 + sda

    #based on observation that typical delay between clock pulse sets is about 3.98 ms
    delaytime = 0.0030

    #Toss the header line
    fr.readline()

    # Handle potential partial packet at beginning
    # Do this by looking for a sufficiently long period during which the clock
    # channel stays logic low

    line = fr.readline().split(',')

    oldt = float(line[0])
    for line in fr:
        lineparts = [x.strip() for x in line.split(',')]

        #overly thorough treatment of values in file
        vals = [float(lineparts[0])]
        vals.extend([int(x) for x in lineparts[1:]])

        if vals[0] - oldt > delaytime:
            oldt = vals[0]
            break

        oldt = vals[0]

    # Old code using assumption that the log included data at every time
    # interval, even if nothing had changed.
    #while dt < delaytime:
    #    line = fr.readline()
    #    lineparts = [x.strip() for x in line.split(',')]

    #    #overly thorough treatment of values in file
    #    vals = [float(lineparts[0])]
    #    vals.extend([int(x) for x in lineparts[1:]])
    #    
    #    #look for a period with scl is low for longer than the delaytime.
    #    if vals[idxcl]:
    #        dt = 0.0
    #    else:
    #        dt += vals[0] - oldt
    #        oldt = vals[0]

    # these store the previous logic values of the channels
    cl = 0 #clock
    da = 0 #data

    data = list()
    times = list()

    for line in fr:
        lineparts = [x.strip() for x in line.split(',')]

        #if data and len(data[-1]) == 21: print 'hmm.. {0:20} \t{1:20}'.format( dt, vals[0])
        #if data and len(data[-1]) >82: print 'hmm..\t{0:<17}\t{1:<20.7}\t{2:<20.7}'.format( dt, vals[0], vals[0]-4.9805815)

        #overly thorough treatment of values in file
        vals = [float(lineparts[0])]
        vals.extend([int(x) for x in lineparts[1:]])
        
        # if clock went high
        if vals[idxcl] and not cl:
            # if a long pause has ended...
            #if dt > delaytime:
            if vals[0] - oldt > delaytime:
                # start a new packet
                data.append([]) #[vals[0],dt])
                #times.append([vals[0], dt])
                times.append(vals[0])

            #if len(data[-1]) == 21: print dt, vals[0]
    
            # append byte to latest packet
            if data:
                data[-1].append(vals[idxda])
            dt = 0.0

        # if clock stayed high
        elif vals[idxcl] and cl:
            # reset time tracking variable
            dt = 0.0

        # if clock stayed low
        elif not vals[idxcl] and not cl:
            # dt continues to accumulate
            pass

        # if clock went low
        elif not vals[idxcl] and cl:
            # dt continues to accumulate
            pass


        cl = vals[idxcl]
        da = vals[idxda]
        oldt = vals[0]

    return data, times


def parse_packets(packets, times=None):
    """
    """

    numbers = list()

    if not times: times = [0] * len(packets)

    for cnt, packet in enumerate(packets):
        if len(packet) != 21:
            print "incorrect packet length:", len(packet), "; packet #{0} at {1} s".format(cnt, times[cnt:cnt+2])
            continue
        sign = 1.0 if packet[0] else -1.0
        # take sets of 4 bits
        #print enumerate([packet[x:x+4] for x in xrange(1,21,4)])

        # Approach: 1 sign bit, 5x 4 bits per decimal number
        #number = sign * sum([10**(-1*d) * sum([nibble[x]<<(3-x) for x in xrange(4)]) for d, nibble in enumerate([packet[x:x+4] for x in xrange(1,21,4)]) ])
        #number = sign * sum([10**(-1*d) * sum([nibble[x]<<(3-x) for x in xrange(4)]) for d, nibble in enumerate([packet[x:x+4] for x in xrange(0,20,4)]) ])

        #Approach: 16bit # w/ incr. significance, ... sign? unit? ?? ?? ??
        number = sum([bit<<(x) for x, bit in enumerate(packet[2:2+16])])

        #Inspecting individual bits
        #number = packet[0]

        numbers.append(number)

    return numbers


if __name__ == '__main__':
    #fr = open("quick.csv", 'r')
    fr = open("SliderOutput2Mhz_001.csv", 'r')
    data, times = get_packets(fr, 1, 0)
    fr.close()
    #data = get_packets(fr)
    print len(data), "packets parsed"
    #for line in data[:10]: print line

    numbers = parse_packets(data, times)
    #for number in numbers[:10]: print number
    #print data[2]
    #print data[2][-21:]
    #print data[3]
    #print data[2][-42:-21]
    #print data[4]
    #print data[5]
    #
    #for cnt, x in enumerate(data):
    #    print "packet #{0}, len: {2:<3} at {1} s".format(cnt, times[cnt:cnt+2], len(x))
    #
    #n=0
    #for x in data:
    #    n+= len(x)
    #
    #print n

    packet = data[500]
    print  packet
    print numbers[500]
    a = [sum([nibble[x]<<(3-x) for x in xrange(4)]) for nibble in [packet[x:x+4] for x in xrange(0,21-3)]]

    print a
    for z in [a[x:x+4] for x in xrange(0,20,4)]:
        print z

    print ''


    a = [sum([nibble[x]<<(x) for x in xrange(4)]) for nibble in [packet[x:x+4] for x in xrange(0,21-3)]]
    print a
    for z in [a[x:x+4] for x in xrange(0,20,4)]:
        print z
