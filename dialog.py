from scipy import spatial

from onmt.translate.translator import build_translator

# Three Seq2Seq's:
# s2s_s_a: seq2seq(s|a)
# s2s_a_pq: seq2seq(a|qi, pi)
# s2s_q_a: backward seq2seq(qi|a)
# All translators

# Rewards
def ease_of_answering(sentence_batch, s2s_s_a):
    s2s_s_a.sentence_batch

def information_flow(pi, pi1):
    return spatial.distance.cosine(dataSetI, dataSetII)

def semantic_coherence(sentence_batch):
    pass