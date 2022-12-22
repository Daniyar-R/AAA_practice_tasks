import math


class CountVectorizer:
    """
    A class used to convert a collection of text documents
    to a matrix of token counts.

    ...

    Attributes
    ----------
    lowercase : bool
        whether to apply lower case to words or not
        default is True
    feature_names : set
        all unique tokens in documents

    Methods
    -------
    lower()
        Return a list of lowered strings

    fit_transform(self, container):
        Assign feature names
        Return a matrix of token counts

    get_feature_names(self)
        Return all unique tokens in documents
    """

    def __init__(self, lowercase=True):
        self.lowercase_flag = lowercase
        self.feature_names = set()

    def _container_split(self, container_input):
        """
        :param container_input:
            default is True
        :return: a list of lowered strings
        """

        container = (
            [x.lower() for x in container_input]
            if self.lowercase_flag
            else container_input
        )
        container_split = [document.split() for document in container]
        return container_split

    def fit_transform(self, container):
        """
        :param container:
        :return: a matrix of token counts
        """

        container_split = self._container_split(container)

        counter_matrix = []

        for document in container_split:
            counter = dict().fromkeys(self.get_feature_names(container), 0)
            for word in document:
                counter[word] = counter[word] + 1
            counter_matrix.append([*counter.values()])

        return counter_matrix

    def get_feature_names(self, container):
        """
        :return: all unique tokens in documents
        """
        container_splitted = self._container_split(container)

        feature_names = set(
            word for document in container_splitted for word in document
        )
        return feature_names


class TfidfTransformer:
    def idf_transform(self, count_matrix):
        quantity_docs = len(count_matrix)
        word_compounds = [*zip(*count_matrix)]
        matrix = []
        for word in word_compounds:
            docs_with_word = 0
            for w in word:
                docs_with_word += int(bool(w))
            matrix.append(
                round(math.log((quantity_docs + 1) /
                               (docs_with_word + 1)) + 1, 1)
            )

        return matrix

    def fit_transform(self, count_matrix):
        tf_idf_matrix = []
        idf_matrix = self.idf_transform(count_matrix)
        for document in count_matrix:
            doc_matrix = []
            for i in range(len(document)):
                doc_matrix.append(round(document[i] /
                                        sum(document) * idf_matrix[i], 3))
            tf_idf_matrix.append(doc_matrix)
        return tf_idf_matrix


class TfidfVectorizer(CountVectorizer):
    def __init__(self, lowercase=True):
        super().__init__(lowercase=lowercase)

    def count_vectorizer(self, contain_param):
        return self.fit_transform(contain_param)

    def tf_idf_transform(self, count_matrix):
        TfidfTransformer().fit_transform(count_matrix)
        return TfidfTransformer().fit_transform(count_matrix)

    def fit_transform_2(self, contain_param):
        count_matrix = self.count_vectorizer(contain_param)
        tf_idf_matrix = self.tf_idf_transform(count_matrix)
        return tf_idf_matrix


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform_2(corpus)
    print(vectorizer.get_feature_names(corpus))
    assert vectorizer.get_feature_names(corpus) == {
        "crock",
        "pot",
        "pasta",
        "never",
        "boil",
        "again",
        "pomodoro",
        "fresh",
        "ingredients",
        "parmesan",
        "to",
        "taste",
    }
    print(tfidf_matrix)
    assert list(map(sorted, tfidf_matrix)) == list(
        map(
            sorted,
            [
                [0.2, 0.2, 0.286, 0.2, 0.2, 0.2, 0, 0, 0, 0, 0, 0],
                [0, 0, 0.143, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
            ],
        )
    )
