# Neural Text Simplification :books: :arrow_right: :blue_book:

In our project we have addressed the **neural text simpliﬁcation task**, that aims to reduce the linguistic
complexity of text, both syntactically and semantically, in order to increase the readability and com-
prehensibility of content. We decided to address this problem by trying three diﬀerent approaches, in
order to experiment some speciﬁc techniques and make a better comparison between their performances
and peculiarities.
First of all we built a baseline in order to become familiar with the problem, then we tried to improve
our results by implementing more complex architectures. In the end we tried four diﬀerent approaches
for a total of three diverse architectures:
* **RNN with attention mechanism**
* **Transformer model trained using a supervised learning**
* **Transformer model with a self supervised approach**
* **GAN model**

For this particular task, several proposals exist in literature for what concerns the English language;
however, we decided to rely on datasets based on Italian corpora in order to experiment how neural
models can solve the text simpliﬁcation problem in a language diﬀerent from the one predominant
among existing investigations.
To obtain the Italian gold standard, we merge two available datasets composed of complex–simple
pairs of sentences, namely the **SIMPITIKI corpus** and the **PaCCSS-it corpus**. For what concerns the
self-supervised approach we have utilized also a simple Italian corpus called **PAISÀ** to enrich the training
data with unseen text lines.
The results we obtained in our experimental setup were not so satisfying based on the **SARI and
BLEU metrics**. From our point of view, this is due to several problems that we encountered, but mainly
the scarcity and not-so-high quality of the data that we used.

## Authors
* [Riccardo Fava](https://github.com/BeleRicks11)
* [Luca Bompani](https://github.com/Bomps4)
* [Davide Mercanti](https://github.com/nonci)
