import unittest
import sys
class CeaserCipher(unittest.TestCase):
    def setUp(self):
        self.operation = sys.argv[1]
        self.word = sys.argv[2]
        self.cipher=sys.argv[3]
    def runTest(self):
        if(self.operation=="encrypt"):
            output=""
            for i in range(len(self.word)):
                if ord(self.word[i])>=ord('a') and ord(self.word[i])<=ord('z'):
                    temp=ord(self.word[i])-int(self.cipher)
                    if temp>ord('z'):
                        temp=temp-26
                    output+=chr(temp)
                if ord(self.word[i])>=ord('A') and ord(self.word[i])<=ord('Z'):
                    temp=ord(self.word[i])-int(self.cipher)
                    if temp>ord('Z'):
                        temp=temp-26
                    output+=chr(temp)
            self.assertEqual(output,"cdef") 
                  

unittest.TextTestRunner().run(CeaserCipher())