# Ajout de contexte à un LLM

Quand on crée une application qui interagit avec un modèle de langage (LLM), le "contexte" correspond aux informations envoyées au modèle dans le prompt. Ce contexte n'est pas conservé par le modèle après la requête. Il faut donc le fournir de nouveau à chaque appel si l'on souhaite que le LLM s'en souvienne.

Ainsi, créer une app ne modifie pas le LLM lui-même : on ajoute simplement un contexte temporaire lors des requêtes.
