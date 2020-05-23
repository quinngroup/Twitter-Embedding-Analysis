import numpy as np 
from collections import defaultdict

settings = {
	'window_size': 2,	# context window +- center word
	'n': 10,		# dimensions of word embeddings, also refer to size of hidden layer
	'epochs': 50,		# number of training epochs
	'learning_rate': 0.01	# learning rate
}

class word2vec():
    def __init__(self):
        self.n = settings['n']
        self.lr = settings['learning_rate']
        self.epochs = settings['epochs']
        self.window = settings['window_size']

    def generate_training_data(self, settings, corpus):
        word_counts = defaultdict(int)
        for row in corpus:
            for word in row:
                word_counts[word]+=1
        
        self.v_count = len(word_counts.keys())
        self.words_list = list(word_counts.keys())
        self.word_to_index = dict((word, i) for i, word in enumerate(self.words_list))
        self.index_to_word = dict((i, word) for i, word in enumerate(self.words_list))

        training_data = []
        for sentence in corpus:
            sent_len = len(sentence)

            for i, word in enumerate(sentence):
                w_target = self.word2onehot(sentence[i])

                w_context = []
                for j in range(i - self.window, i+self.window+1):
                    if j != i and j <= sent_len-1 and j>= 0:
                        w_context.append(self.word2onehot(sentence[j]))
                training_data.append([w_target, w_context])
        return np.array(training_data)

    def word2onehot(self, word):
        word_vec = [0 for i in range(0, self.v_count)]
        word_index = self.word_to_index[word]
        word_vec[word_index] = 1
        return word_vec

    def train(self, training_data):
        self.w1 = np.random.uniform(-1, 1, (self.v_count, self.n))
        self.w2 = np.random.uniform(-1, 1, (self.n, self.v_count))

        for i in range(self.epochs):
            self.loss = 0

            for w_t, w_c in training_data:
                y_pred, h, u = self.forward_pass(w_t)

                EI = np.sum([np.subtract(y_pred, word) for word in w_c], axis=0)

                self.backprop(EI, h, w_t)

                self.loss += -np.sum([u[word.index(1)] for word in w_c]) + len(w_c) * np.log(np.sum(np.exp(u)))

    def backprop(self, e, h, x):
        d1_dw2 = np.outer(h,e)
        d1_dw1 = np.outer(x, np.dot(self.w2, e.T))

        self.w1 = self.w1 - (self.lr * d1_dw1)
        self.w2 = self.w2 - (self.lr * d1_dw2)

    def forward_pass(self, x):
        h = np.dot(self.w1.T, x)
        u = np.dot(self.w2.T, h)
        y_c = self.softmax(u)
        return y_c, h, u

    def softmax(self, x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum(axis=0)

    def word_vec(self, word):
        w_index = self.word_to_index[word]
        v_w = self.w1[w_index]
        return v_w