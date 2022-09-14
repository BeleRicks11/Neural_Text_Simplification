import pandas as pd

def build_vocabulary(train_df, test_df, tokenizer):
    """
    Given train corpus and test corpus, builds the corresponding word vocabulary.

    --------------
    Return: 
      - word vocabulary: vocabulary index to word
      - inverse word vocabulary: word to vocabulary index
      - word listing: set of unique terms that build up the vocabulary
    """

    corpus = list(pd.concat([
        train_df['sentence_1'],
        train_df['sentence_2'],
        test_df['sentence_1'],
        test_df['sentence_2']
    ]))
    word_to_idx = dict()  
    idx_to_word = dict()
    word_listing = set()

    # Get all unique words in corpus 
    for sentence in corpus:
        word_listing |= set(tokenizer(sentence))
        
   # Cast to list
    word_listing = list(word_listing)

    # Build vocabulary index to word <idx : word>
    idx_to_word = dict(enumerate(word_listing, start=1))

    # Build word_to_idx <word : idx>
    word_to_idx = dict({_:k for k,_ in idx_to_word.items()})

    return idx_to_word, word_to_idx, word_listing
