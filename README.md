![backend workflow](https://github.com/shizzeer/spotify_party/actions/workflows/backend-ci.yml/badge.svg)
![frontend workflow](https://github.com/shizzeer/spotify_party/actions/workflows/frontend-ci.yml/badge.svg)

<p align="center">
  <a href="" rel="noopener">
 <img src="./frontend/src/assets/logo.svg" alt="Project logo"></a>
</p>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![GitHub Issues](https://img.shields.io/github/issues/shizzeer/spotify_party)](https://github.comshizzeer/spotify_party/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.comshizzeer/spotify_party/pulls)
  [![File count](https://img.shields.io/github/directory-file-count/shizzeer/spotify_party)]() 

</div>

## Opis projektu

SpotifyParty to innowacyjna aplikacja, która umożliwia użytkownikom Spotify połączenie swoich gustów muzycznych, aby stworzyć unikalne, spersonalizowane playlisty. Aplikacja umożliwia użytkownikom dołączanie do "pokoju", które są prowadzone przez gospodarza. Gospodarz to osoba, która decyduje się udostępnić swoje konto Spotify, umożliwiając tworzenie playlisty.

Użytkownicy, włączając gospodarza, mają możliwość wyboru swoich ulubionych playlist, albumów, artystów, a nawet gatunków muzycznych z ich kont na Spotify. Dodatkowo, każdy użytkownik może wybrać jedną, specjalną piosenkę - "must-have song", która bezwarunkowo zostanie dodana do końcowej playlisty.

SpotifyParty wykorzystuje specjalny algorytm, który analizuje wybory użytkowników, identyfikuje podobieństwa w preferencjach muzycznych, a następnie tworzy playlistę na koncie gospodarza. Playlisty są tworzone na podstawie wspólnych wyborów przynajmniej dwóch uczestników, z wyjątkiem wyboru "must-have song".

Wynikowa playlista jest dostępna na platformie Spotify, gdzie może być odtwarzana przez wszystkich uczestników pokoju. Aplikacja SpotifyParty stawia na interakcję i wspólne doświadczenie muzyczne, umożliwiając tworzenie spersonalizowanych, dynamicznych playlist, które idealnie pasują do każdego nastroju i okazji.

## Instrukcje instalacji

SpotifyParty jest aplikacją opartą na **Dockerze** , co oznacza, że wszystkie wymagane zależności są automatycznie instalowane. Aby zainstalować i uruchomić SpotifyParty, wykonaj następujące kroki: 

1. Upewnij się, że masz zainstalowany Docker na swoim komputerze. Jeśli nie, możesz go pobrać i zainstalować stąd: [Docker](https://www.docker.com/products/docker-desktop)

2. Sklonuj repozytorium SpotifyParty na swój lokalny komputer za pomocą polecenia git:

    ```bash

    git clone https://github.com/shizzeer/spotify_party.git
    ```

3. Przejdź do katalogu projektu:

    ```bash

    cd spotify_party
    ```

4. Zbuduj obraz Docker. Teraz, gdy jesteś w folderze projektu, możesz zbudować obraz Docker. Użyj polecenia docker build, podając jako argument kropkę (co oznacza "bieżący folder"):

    ```bash

    docker build -t spotifyparty .
    ```

    Tutaj "spotifyparty" to nazwa, którą nadajesz obrazowi Docker.

5. Uruchom kontener Docker. Po zbudowaniu obrazu, możesz go uruchomić za pomocą polecenia docker run. Poniższe polecenie uruchomi kontener w tle (-d)

    ```bash

    docker run -d spotifyparty
    ```
 
6. Sprawdź, czy aplikacja działa. Otwórz przeglądarkę internetową i wpisz `127.0.0.1:3000` w pasku adresu. Powinieneś zobaczyć działającą aplikację SpotifyParty.

## Przykłady użycia

### 1. Wybór roli

Po wejściu na stronę główną aplikacji SpotifyParty, użytkownik decyduje, jaką rolę chce pełnić - gospodarza lub użytkownika. Wybór dokonuje się poprzez kliknięcie jednego z dwóch kafelków.

### 2. Autoryzacja Spotify

Po wybraniu odpowiedniej roli, użytkownik jest przekierowany na stronę OAuth Spotify, gdzie loguje się na swoje konto i wyraża zgodę na poświadczenie uprawnień aplikacji.

### 3. Tworzenie lub dołączanie do pokoju

Po pomyślnej autoryzacji, użytkownik jest przekierowywany na odpowiednią stronę:

- **Jeśli jest gospodarzem** : Na stronie generowany jest nowy 6-znakowy kod pokoju, który jest wyświetlany centralnie na ekranie. Gospodarz powinien udostępnić ten kod innym użytkownikom.
- **Jeśli jest użytkownikiem** : Po zalogowaniu pokazywany jest pop-up z polem do wpisania kodu pokoju udostępnionego przez gospodarza.

### 4. Wybór gustu muzycznego

Zarówno gospodarz, jak i użytkownicy, przechodzą przez proces wyboru gustu muzycznego. Wybór jest zatwierdzany poprzez kliknięcie przycisku "Next" na każdym etapie. Użytkownikom prezentowane są kolejno:
- Ich playlisty
- Zapisane albumy
- Najczęściej słuchani artyści
- Gatunki muzyczne

Wybór odbywa się poprzez kliknięcie kafelka. Na przedostatnim etapie użytkownikowi ukazuje się wyszukiwarka, w której może wyszukać "must-have song". Po wybraniu piosenki, użytkownik przechodzi do ekranu "Enjoy the music!", gdzie czeka na utworzenie playlisty przez gospodarza.

Gospodarz, po tym samym procesie wyboru, ma dodatkowo przycisk "Create the playlist", który pozwala na utworzenie końcowej playlisty.

## Instrukcje kontrybucji

Cieszymy się, że jesteś zainteresowany przyczynieniem się do SpotifyParty! Poniżej znajdują się instrukcje, które pomogą Ci w tym procesie.

### Zgłaszanie błędów

Jeśli napotkasz błąd podczas korzystania z SpotifyParty, prosimy o zgłoszenie go poprzez system zgłaszania błędów GitHub (issues). Prosimy o dostarczenie jak najwięcej informacji, takich jak kroki do odtworzenia błędu, oczekiwane i rzeczywiste wyniki, oraz informacje o Twoim środowisku (np. wersja przeglądarki).

### Propozycje nowych funkcji

Jeśli masz pomysł na nową funkcję, którą chciałbyś zobaczyć w SpotifyParty, prosimy o zgłoszenie go poprzez system zgłaszania błędów GitHub (issues). Prosimy o szczegółowy opis tej funkcji i dlaczego uważasz, że będzie ona wartościowa.

### Przesyłanie zmian

Jeśli chcesz przyczynić się do kodu SpotifyParty, prosimy o przestrzeganie następujących kroków:

1. Utwórz fork repozytorium SpotifyParty na swoim koncie GitHub.
2. Utwórz nowy branch dla Twoich zmian.
3. Dodaj i zatwierdź (commit) swoje zmiany na tym branchu.
4. Utwórz pull request na GitHubie, aby przesłać swoje zmiany do głównego repozytorium SpotifyParty.

Prosimy o dostarczenie jak najwięcej informacji w Twoim pull requeście, takich jak co zmieniłeś, dlaczego, i jakie testy przeprowadziłeś, aby upewnić się, że Twoje zmiany są bezpieczne i nie wprowadzają nowych błędów.

### Testowanie

Prosimy o przetestowanie swoich zmian przed przesłaniem ich do SpotifyParty. Jeśli Twoje zmiany wprowadzają nową funkcjonalność, prosimy o dodanie odpowiednich testów, które pokazują, że ta funkcjonalność działa poprawnie.

### Formatowanie kodu i dokumentacji

Prosimy o przestrzeganie ustalonych wytycznych dotyczących formatowania kodu i dokumentacji. Kod powinien być napisany w sposób zrozumiały i łatwy do czytania, z odpowiednimi komentarzami tam, gdzie jest to potrzebne. Dokumentacja powinna być jasna i precyzyjna

Jeśli jesteś nowy w Git i GitHub, zalecamy zapoznanie się z [dokumentacją Git](https://git-scm.com/doc) i [dokumentacją GitHub](https://docs.github.com/en/github), które zawierają wiele przydatnych informacji i poradników.

## Informacje o licencji

Ten projekt jest licencjonowany na podstawie licencji MIT. Oznacza to, że możesz korzystać z tego kodu do dowolnych celów, pod warunkiem, że zachowasz informacje o prawach autorskich i licencji.

Pamiętaj, że korzystając ze Spotify API, musisz również przestrzegać warunków ich licencji. Więcej informacji znajdziesz na stronie [Spotify Developer Terms of Service](https://developer.spotify.com/terms/)

## Informacje kontaktowe

Jeśli masz pytania lub problemy związane z SpotifyParty, skontaktuj się z nami za pośrednictwem GitHuba.

- Link do profilu na GitHubie: 
    ### [MSZUDYPK](https://github.com/MSZUDYPK)
    ### [shizzeer](https://github.com/shizzeer)
    ### [Grz3hu](https://github.com/Grz3hu)
    ### [jakubszpilowski](https://github.com/jakubszpilowski)
- Link do systemu zgłaszania błędów na GitHubie: [github.com/shizzeer/spotifyparty/issues](https://github.com/shizzeer/spotify_party/issues)


## FAQ

1. **Czy mogę korzystać z SpotifyParty bez konta Spotify?**

    Nie, korzystanie z SpotifyParty wymaga konta na platformie Spotify. Jest to konieczne, ponieważ gust muzyczny użytkownika jest pobierany bezpośrednio z jego konta przy użyciu Spotify API. Bez konta Spotify, aplikacja nie będzie w stanie uzyskać tych informacji i stworzyć spersonalizowanej playlisty.

2. **Czy SpotifyParty jest dostępne w moim języku?**

    Obecnie, SpotifyParty jest dostępne tylko w języku angielskim. Zarówno interfejs aplikacji, jak i kod źródłowy z komentarzami, są napisane w tym języku. Pracujemy nad dodaniem więcej języków w przyszłości.

3. **Czy mogę dodać więcej niż jedną piosenkę "must-have" do playlisty?**

    Nie, w obecnej wersji SpotifyParty, użytkownik może wybrać tylko jedną piosenkę "must-have". Ta piosenka jest gwarantowana do dodania do końcowej playlisty. Pozwala to na utrzymanie zrównoważonej i różnorodnej playlisty, która odzwierciedla gusty wszystkich uczestników.

4. **Co się stanie, jeśli gospodarz opuści pokój?**

    Na tym etapie rozwoju aplikacji, jeśli gospodarz opuści pokój, pokój zostanie zamknięty i nie będzie możliwości powrotu do niego. Za każdym razem, gdy gospodarz tworzy pokój, generowany jest nowy, unikalny kod pokoju.

5. **Czy mogę zobaczyć, kto dodał jaką piosenkę do playlisty?**

    W obecnej wersji SpotifyParty, wszystkie piosenki w playliście są dodawane przez gospodarza. Nie ma możliwości zobaczenia, który użytkownik wybrał konkretną piosenkę. Pracujemy nad dodaniem tej funkcji w przyszłych aktualizacjach.

6. **Czy mogę korzystać z SpotifyParty, jeśli nie mam premium na Spotify?**

    Tak, SpotifyParty jest dostępne dla wszystkich użytkowników Spotify, niezależnie od tego, czy mają konto premium, czy nie. Posiadanie konta premium nie ma wpływu na dostępność ani funkcjonalność aplikacji.

Jeśli masz więcej pytań, które nie zostały tutaj poruszone, skontaktuj się z nami za pośrednictwem GitHuba. Możesz również odwiedzić [Spotify API Documentation](https://developer.spotify.com/documentation/web-api/) dla więcej informacji na temat Spotify API.
