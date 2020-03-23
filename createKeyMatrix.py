class KeyMatrix:

    matrixLen = 5
    allAlphabets = ['A', 'B', 'C', 'D', 'E',
                    'F', 'G', 'H', 'I', 'K',
                    'L', 'M', 'N', 'O', 'P',
                    'Q', 'R', 'S', 'T', 'U',
                    'V', 'W', 'X', 'Y', 'Z']

    keyMatrix = list()

    def __init__(self, word):

        list_word = self.delete_repeat(word)

        for i in range(self.matrixLen):
            temp_mat = list()
            for j in range(self.matrixLen):
                if i*self.matrixLen + j < len(list_word):
                    temp_mat.append(list_word[i*self.matrixLen + j])
                else:
                    temp_mat.append(self.allAlphabets[i*self.matrixLen + j - len(list_word)])

            self.keyMatrix.append(temp_mat)

    def display_key_matrix(self):
        for line in self.keyMatrix:
            print(line)

    def find_element_2d(self, letter):
        """
        finds the position of any alphabet in the key matrix
        :param letter: Letter to be found in the key matrix
        :return: the position & if not found -1, -1
        """
        for row in range(len(self.keyMatrix)):
            for column in range(len(self.keyMatrix[row])):
                if self.keyMatrix[row][column] == letter:
                    return row, column
        else:
            return -1, -1

    def delete_repeat(self, str_word):
        """
        Replaces all j with i and any alphabet repeat in key word
        Also deletes the letter from all alphabet which are present is key word
        :param str_word: word to create key matrix with
        :return: the new word to make key matrix
        """

        str_word = str_word.replace("J", "I")

        list_word = list(str_word)
        for index in range(len(list_word)):
            if index == len(list_word):
                break
            if list_word[index] in list_word[index + 1:len(list_word)]:
                list_word.remove(list_word[index])

        for index in range(len(list_word)):
            if list_word[index] in self.allAlphabets:
                self.allAlphabets.remove(list_word[index])

        return list_word

    def x_attach(self, sentence):
        """
        add x between two repeat letter
        removers spaces
        add x if the sentence is odd number of word
        :param sentence: sentence to encode
        :return: sentence is prepared for encoding as list single word a item
        """

        # replaces space
        space_position = list()

        for index, character in enumerate(sentence):
            if character == " ":
                space_position.append(index)

        space_less_sentence = sentence.replace(" ", "")

        # replaces repeat word
        list_sentence = list(space_less_sentence)
        out_list_sentence = list()
        x_position = list()
        start = 0

        for i in range(len(list_sentence) - 1):
            out_list_sentence.append(list_sentence[i])
            start += 1
            if list_sentence[i] == list_sentence[i + 1]:
                out_list_sentence.append("X")
                x_position.append(start)
                start += 1

        out_list_sentence.append(list_sentence[-1])

        # add X at last if length in odd
        if len(out_list_sentence)%2 == 1:
            out_list_sentence.append("X")
            start += 1
            x_position.append(start)

        print(out_list_sentence)
        print(space_position)
        print(x_position)

        return out_list_sentence


in_word = "SANKHADEEP"


matrix = KeyMatrix(in_word)
matrix.display_key_matrix()
matrix.x_attach("SS DD AABBCC D DDAA")


