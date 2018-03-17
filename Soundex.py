# Two implementations of Soundex algorithm


def soundexNaive(name, len=4):
    '''A naive implementation of the soundex algorithm.
       By Deepak Kumar, 2/12/2008. dkumar@brynmawr.edu
       Expects name to be in uppercase.
    '''
    sndx = name[0]  # Keep first letter

    for i in name[1:len]:
        if i in "BFPV":
            d = "1"
        elif i in "CGJKQSXZ":
            d = "2"
        elif i in "DT":
            d = "3"
        elif i == "L":
            d = "4"
        elif i in "MN":
            d = "5"
        elif i == "R":
            d = "6"
        else:
            d = ''

        # Do not add if repeated/duplicated
        if d != sndx[-1]:
            sndx += d
    return (sndx + (len * '0'))[:len]   # first 4 letters or padd with 0 to make 4


def soundex(name, len=4):
    """ soundex module conforming to Donald Knuth's algorithm
        implementation 2000-12-24 by Gregory Jorgensen
        public domain.
		Expects name to be in uppercase.
        Modified by Deepak Kumar, 2/11/2008. dkumar@cs.brynmawr.edu
		Modified by Deepak Kumar, 3/21/2017. dkumar@cs.brynmawr.edu
    """

    # Define soundex values for each letter, 0 means omitted
    #         ABCDEFGHIJKLMNOPQRSTUVWXYZ
    digits = '01230120022455012623010202'

    # retain first letter of string
    sndx = name[0]

    # translate each successive letter in name
    for c in name[1:len]:
        d = digits[ord(c)-ord('A')]
        # If 2 or more letters with same # are adjacent then just keep one
        if d != '0' and d != sndx[-1]:
            sndx += d

    # remove all 0s from the soundex code
    sndx = sndx.replace('0','')

    # return soundex code padded to len characters
    return (sndx + (len * '0'))[:len]


def main():
    person = input("Enter your name: ")
    # print("Length ", len(person))
    print("Algorithm 1 result for", person, soundexNaive(person.upper(), len(person)))
    print("Algorithm 2 result for", person, soundex(person.upper(), len(person)))


main()