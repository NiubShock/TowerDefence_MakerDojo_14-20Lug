# Tower Defence
## Intro
Questo codice è il risultato del corso di python base svolto dal 14 al 20 luglio nel camping estivo MakerDojo.
## Struttura
Il codice si basa su una classe base chiamata "sprite_render" che permette di posizionare e stampare a schermo uno sprite.
La classe "enemy" sfruttta la classe "sprite_render" per aggiungere le caratteristiche dei nemici agli sprite, come vita, punti e gold.
La classe "tower_AoE" rappresenta la torre che spara a 360 gradi, questo è l'unico tipo di torre presente al momento.
La classe "towers" è utilizzata per gestire tutte le torri che vengono posizionate
Infine, la classe "gioco" gestisce la lista di nemici, di towers e le fasi di gioco
## Note Importanti
È necessario sistemare le path delle immagini per far partire il codice
