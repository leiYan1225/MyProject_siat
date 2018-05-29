
import tensorflow as tf
import reader

DATA_PATH = "F:\datasets\PTB_data"
HIDDEN_SIZE = 200
NUM_LAYERS = 2
VOCAB_SIZE = 10000

LEARNING_RATE = 1.0
TRAIN_BATCH_SIZE = 20
TRAIN_NUM_STEP = 35

EVAL_BATCH_SIZE = 1
EVAL_NUM_STEP = 1
NUM_EPOCH = 2
KEEP_PROB = 0.5
MAX_GRAD_NORM = 5

# 这是一条测试语句
input_data = tf.placeholder(tf.int32, [TRAIN_BATCH_SIZE, TRAIN_NUM_STEP])
embedding = tf.get_variable("embedding", [VOCAB_SIZE, HIDDEN_SIZE])

train_data, valid_data, test_data, _ = reader.ptb_raw_data(DATA_PATH)

inputs = tf.nn.embedding_lookup(embedding, input_data)
inputs = tf.nn.dropout(inputs, KEEP_PROB)

train_queue = reader.ptb_producer(train_data, TRAIN_BATCH_SIZE, TRAIN_NUM_STEP)


with tf.Session() as session:
    init_op = tf.global_variables_initializer().run(train_queue)


