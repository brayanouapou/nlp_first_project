import requests

class CorpusLoader:
    """
    Cette classe est responsable du chargement d'un corpus de texte à partir d'une URL donnée. 
    Elle utilise la bibliothèque `requests` pour récupérer le contenu du texte et gère les erreurs 
    potentielles lors du chargement.
    """

    @staticmethod
    def load_corpus(url: str) -> str:
        """
        Charge le corpus de texte à partir de l'URL spécifiée.

        Arguments:
            url (str): L'URL du corpus à charger.

        Returns:
            str: Le contenu du corpus sous forme de chaîne de caractères.

        Raises:
            Exception: Si une erreur survient lors du chargement du corpus.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Vérifie que la requête a réussi
            DEBUT = '*** START OF THE PROJECT GUTENBERG EBOOK 17989 ***'
            FIN   = '*** END OF THE PROJECT GUTENBERG EBOOK 17989 ***'
            content = response.text
            start_index = content.find(DEBUT) + len(DEBUT)
            end_index = content.find(FIN)
            roman = content[start_index:end_index].strip()
            return roman
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors du chargement du corpus : {e}")
            roman = ""

        return roman
