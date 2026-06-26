import re
# from unidecode import unidecode

class TextCleaner:

    """
    Cette classe fournit des méthodes pour nettoyer un texte en français, en supprimant la ponctuation, les chiffres isolés, et en normalisant les caractères. 
    Elle est conçue pour préparer le texte pour une analyse NLP.
    """

    @staticmethod
    def clean_text_V3(
        text: str, 
        preserve_compound_words: bool = False, 
        remove_isolated_numbers: bool = True
    ) -> str:
        """
        Nettoie un texte pour une analyse NLP en français.
        
        Le nettoyage de base (minuscules, suppression des marqueurs d'italiques Gutenberg,
        sauts de ligne, ponctuation et espaces multiples) est toujours actif.

        Parameters:
        -----------
        text : str
            La chaîne de caractères brute à nettoyer.
        preserve_compound_words : bool, optional
            Si True, transforme les tirets internes en underscores (_) pour préserver
            l'unité des mots composés (ex: "arc-en-ciel" -> "arc_en_ciel"). (par défaut False).
        remove_isolated_numbers : bool, optional
            Si True, supprime tous les nombres isolés du texte (ex: '24', '1815') 
            pour ne garder que le contenu textuel (par défaut True).

        Returns:
        --------
        str
            Le texte nettoyé et normalisé.
        """
        
        # 1. Mise en minuscules
        text = text.lower()
        
        # 2. Suppression des marqueurs d'italique Gutenberg (_mot_ -> mot)
        text = re.sub(r'_([^_]+)_', r'\1', text)
        
        # 3. Remplacement des sauts de ligne et tabulations par des espaces
        text = re.sub(r'[\n\r\t]+', ' ', text)
        
        # 4. Gestion des mots composés (Tirets -> Underscores) monte-Cristo -> monte_Cristo
        if preserve_compound_words:
            text = re.sub(r'(?<=[a-zàâçéèêëîïôûùüÿñæœ])-(?=[a-zàâçéèêëîïôûùüÿñæœ])', '_', text)
        
        # 5. Suppression des nombres isolés
        if remove_isolated_numbers:
            text = re.sub(r'\b\d+\b', ' ', text)
        
        # 6. Suppression de la ponctuation et des caractères spéciaux
        #    On adapte dynamiquement le regex pour autoriser l'underscore (_) uniquement si demandé
        allowed_chars = "a-zàâçéèêëîïôûùüÿñæœ'"
        if preserve_compound_words:
            allowed_chars += "_"
        if not remove_isolated_numbers:
            allowed_chars += "0-9"
            
        regex_pattern = f"[^{allowed_chars} ]"
        text = re.sub(regex_pattern, ' ', text)
        
        # 7. Normalisation des apostrophes typographiques
        text = re.sub(r"[''`]", "'", text)
        
        # 8. Suppression des espaces multiples 
        text = re.sub(r'\s+', ' ', text)

        # 9. Suppression des espaces en début et fin
        text = text.strip()
        return text