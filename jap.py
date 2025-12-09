import genanki
import random
import os


# ============================
#   CONFIGURAÇÃO DO DECK
# ============================

kanji_deck = genanki.Deck(
    2055010191,
    "JLPT N5 — Kanji Completo (Com vocabulário)"
)

# ============================
#   MODELO DAS CARTAS
# ============================

kanji_model = genanki.Model(
    1607392319,
    "Kanji N5 Completo Model",
    fields=[
        {"name": "Kanji"},
        {"name": "Significado"},
        {"name": "Onyomi"},
        {"name": "Kunyomi"},
        {"name": "Vocabulario"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": """
                <div style="font-size: 80px; text-align:center;">
                    {{Kanji}}
                </div>
            """,
            "afmt": """
                {{FrontSide}}
                <hr>
                <div style="font-size: 30px;">
                    <b>Significado:</b> {{Significado}}<br><br>
                    <b>Onyomi:</b> {{Onyomi}}<br><br>
                    <b>Kunyomi:</b> {{Kunyomi}}<br><br>
                    <b>Vocabulário:</b><br>
                    <div style="font-size: 22px;">{{Vocabulario}}</div>
                </div>
            """,
        }
    ],
)


kanji_list = [
    # Números
    {"kanji":"一", "meaning":"um / um (número)", "onyomi":"いち", "kunyomi":"ひとつ", "vocab":"一人（ひとり） — uma pessoa"},
    {"kanji":"二", "meaning":"dois", "onyomi":"に", "kunyomi":"ふたつ", "vocab":"二人（ふたり） — duas pessoas"},
    {"kanji":"三", "meaning":"três", "onyomi":"さん", "kunyomi":"みっつ", "vocab":"三日（みっか） — dia 3 / três dias"},
    {"kanji":"四", "meaning":"quatro", "onyomi":"し / よん", "kunyomi":"よっつ", "vocab":"四日（よっか） — dia 4"},
    {"kanji":"五", "meaning":"cinco", "onyomi":"ご", "kunyomi":"いつつ", "vocab":"五日（いつか） — dia 5 / cinco dias"},
    {"kanji":"六", "meaning":"seis", "onyomi":"ろく", "kunyomi":"むっつ", "vocab":"六日（むいか） — dia 6"},
    {"kanji":"七", "meaning":"sete", "onyomi":"しち / なな", "kunyomi":"ななつ", "vocab":"七日（なのか） — dia 7"},
    {"kanji":"八", "meaning":"oito", "onyomi":"はち", "kunyomi":"やっつ", "vocab":"八日（ようか） — dia 8"},
    {"kanji":"九", "meaning":"nove", "onyomi":"きゅう / く", "kunyomi":"ここのつ", "vocab":"九日（ここのか） — dia 9"},
    {"kanji":"十", "meaning":"dez", "onyomi":"じゅう", "kunyomi":"とお / とう", "vocab":"十日（とおか） — dia 10 / dez dias"},
    {"kanji":"百", "meaning":"cem / cento", "onyomi":"ひゃく", "kunyomi":"—", "vocab":"百円（ひゃくえん） — 100 ienes"},
    {"kanji":"千", "meaning":"mil", "onyomi":"せん", "kunyomi":"ち", "vocab":"千円（せんえん） — 1000 ienes"},
    {"kanji":"万", "meaning":"dez mil", "onyomi":"まん", "kunyomi":"—", "vocab":"一万円（いちまんえん） — 10.000 ienes"},
    {"kanji":"億", "meaning":"cem milhões", "onyomi":"おく", "kunyomi":"—", "vocab":"一億円（いちおくえん） — 100 milhões de ienes"},

    # Tempo / Data / Hora
    {"kanji":"日", "meaning":"dia / sol", "onyomi":"にち / じつ", "kunyomi":"ひ / か", "vocab":"日曜日（にちようび） — domingo"},
    {"kanji":"週", "meaning":"semana", "onyomi":"しゅう", "kunyomi":"—", "vocab":"来週（らいしゅう） — semana que vem"},
    {"kanji":"月", "meaning":"mês / lua", "onyomi":"げつ / がつ", "kunyomi":"つき", "vocab":"月曜日（げつようび） — segunda-feira"},
    {"kanji":"年", "meaning":"ano", "onyomi":"ねん", "kunyomi":"とし", "vocab":"今年（ことし） — este ano"},
    {"kanji":"時", "meaning":"hora / tempo", "onyomi":"じ", "kunyomi":"とき", "vocab":"何時（なんじ） — que horas?"},
    {"kanji":"間", "meaning":"intervalo / período", "onyomi":"かん", "kunyomi":"あいだ / ま", "vocab":"時間（じかん） — tempo / horas"},
    {"kanji":"分", "meaning":"minuto / parte / entender", "onyomi":"ぶん / ふん / ぶ", "kunyomi":"わかる", "vocab":"二分（にふん） — dois minutos"},
    {"kanji":"午", "meaning":"meio-dia / meridiano", "onyomi":"ご", "kunyomi":"—", "vocab":"午前（ごぜん） — manhã / A.M."},
    {"kanji":"前", "meaning":"antes / frente", "onyomi":"ぜん", "kunyomi":"まえ", "vocab":"前回（ぜんかい） — última vez"},
    {"kanji":"後", "meaning":"depois / atrás", "onyomi":"ご / こう", "kunyomi":"あと / うし", "vocab":"後で（あとで） — depois"},
    {"kanji":"今", "meaning":"agora / presente", "onyomi":"こん", "kunyomi":"いま", "vocab":"今（いま） — agora"},
    {"kanji":"先", "meaning":"antes / precedente", "onyomi":"せん", "kunyomi":"さき", "vocab":"先週（せんしゅう） — semana passada"},
    {"kanji":"来", "meaning":"vir / próximo", "onyomi":"らい", "kunyomi":"くる / きます", "vocab":"来月（らいげつ） — próximo mês"},
    {"kanji":"毎", "meaning":"cada / todo", "onyomi":"まい", "kunyomi":"ごと", "vocab":"毎日（まいにち） — todo dia"},
# Pessoas / lugares / coisas
{"kanji":"人", "meaning":"pessoa", "onyomi":"じん / にん", "kunyomi":"ひと", "vocab":"日本人（にほんじん） — pessoa japonesa"},
{"kanji":"男", "meaning":"homem", "onyomi":"だん / なん", "kunyomi":"おとこ", "vocab":"男の子（おとこのこ） — menino"},
{"kanji":"女", "meaning":"mulher", "onyomi":"じょ", "kunyomi":"おんな", "vocab":"女の子（おんなのこ） — menina"},
{"kanji":"子", "meaning":"criança / filho(a)", "onyomi":"し", "kunyomi":"こ", "vocab":"子供（こども） — criança"},
{"kanji":"母", "meaning":"mãe", "onyomi":"ぼ", "kunyomi":"はは", "vocab":"母（はは） — mãe"},
{"kanji":"父", "meaning":"pai", "onyomi":"ふ", "kunyomi":"ちち", "vocab":"父（ちち） — pai"},
{"kanji":"友", "meaning":"amigo", "onyomi":"ゆう", "kunyomi":"とも", "vocab":"友達（ともだち） — amigo"},
{"kanji":"本", "meaning":"livro / origem", "onyomi":"ほん", "kunyomi":"もと", "vocab":"本（ほん） — livro"},
{"kanji":"気", "meaning":"espírito / energia / clima", "onyomi":"き", "kunyomi":"—", "vocab":"元気（げんき） — saudável / animado"},
{"kanji":"生", "meaning":"vida / viver", "onyomi":"せい / しょう", "kunyomi":"い(きる) / う(まれる)", "vocab":"生徒（せいと） — estudante"},
{"kanji":"車", "meaning":"carro / veículo", "onyomi":"しゃ", "kunyomi":"くるま", "vocab":"車（くるま） — carro"},
{"kanji":"語", "meaning":"língua / palavra", "onyomi":"ご", "kunyomi":"かた(る)", "vocab":"日本語（にほんご） — língua japonesa"},
{"kanji":"耳", "meaning":"orelha", "onyomi":"じ", "kunyomi":"みみ", "vocab":"耳（みみ） — orelha"},
{"kanji":"手", "meaning":"mão", "onyomi":"しゅ", "kunyomi":"て", "vocab":"手紙（てがみ） — carta"},
{"kanji":"足", "meaning":"pé / perna", "onyomi":"そく", "kunyomi":"あし / た(す)", "vocab":"足（あし） — perna / pé"},
{"kanji":"目", "meaning":"olho", "onyomi":"もく", "kunyomi":"め", "vocab":"目（め） — olho"},
{"kanji":"口", "meaning":"boca / entrada", "onyomi":"こう", "kunyomi":"くち", "vocab":"入口（いりぐち） — entrada"},
{"kanji":"店", "meaning":"loja", "onyomi":"てん", "kunyomi":"みせ", "vocab":"喫茶店（きっさてん） — cafeteria"},
{"kanji":"駅", "meaning":"estação (trem, metrô)", "onyomi":"えき", "kunyomi":"—", "vocab":"駅（えき） — estação"},
{"kanji":"道", "meaning":"estrada / caminho", "onyomi":"どう", "kunyomi":"みち", "vocab":"道（みち） — estrada / caminho"},
{"kanji":"国", "meaning":"país", "onyomi":"こく", "kunyomi":"くに", "vocab":"外国（がいこく） — país estrangeiro"},
{"kanji":"学", "meaning":"estudo", "onyomi":"がく", "kunyomi":"まな(ぶ)", "vocab":"学校（がっこう） — escola"},
{"kanji":"校", "meaning":"escola", "onyomi":"こう", "kunyomi":"—", "vocab":"学校（がっこう） — escola"},
{"kanji":"名", "meaning":"nome", "onyomi":"めい / みょう", "kunyomi":"な", "vocab":"名前（なまえ） — nome"},
{"kanji":"円", "meaning":"iene / círculo", "onyomi":"えん", "kunyomi":"まる(い)", "vocab":"円（えん） — iene / círculo"},
{"kanji":"半", "meaning":"metade", "onyomi":"はん", "kunyomi":"なか(ば)", "vocab":"半分（はんぶん） — metade"},
{"kanji":"全", "meaning":"todo / completo", "onyomi":"ぜん", "kunyomi":"まった(く) / すべて", "vocab":"全部（ぜんぶ） — todo / tudo"},
{"kanji":"何", "meaning":"o que / quantos", "onyomi":"か", "kunyomi":"なに / なん", "vocab":"何（なに） — o que?"},

# Natureza / direções / elementos
{"kanji":"火", "meaning":"fogo", "onyomi":"か", "kunyomi":"ひ", "vocab":"火曜日（かようび） — terça-feira"},
{"kanji":"水", "meaning":"água", "onyomi":"すい", "kunyomi":"みず", "vocab":"水（みず） — água"},
{"kanji":"木", "meaning":"árvore / madeira", "onyomi":"もく", "kunyomi":"き", "vocab":"木（き） — árvore / madeira"},
{"kanji":"金", "meaning":"ouro / metal / dinheiro", "onyomi":"きん", "kunyomi":"かね", "vocab":"お金（おかね） — dinheiro"},
{"kanji":"土", "meaning":"terra / solo", "onyomi":"ど / と", "kunyomi":"つち", "vocab":"土曜日（どようび） — sábado"},
{"kanji":"海", "meaning":"mar / oceano", "onyomi":"かい", "kunyomi":"うみ", "vocab":"海外（かいがい） — exterior / ultramar"},
{"kanji":"川", "meaning":"rio", "onyomi":"せん", "kunyomi":"かわ", "vocab":"川（かわ） — rio"},
{"kanji":"山", "meaning":"montanha", "onyomi":"さん", "kunyomi":"やま", "vocab":"山（やま） — montanha"},
{"kanji":"花", "meaning":"flor", "onyomi":"か", "kunyomi":"はな", "vocab":"花（はな） — flor"},
{"kanji":"天", "meaning":"céu / céu acima", "onyomi":"てん", "kunyomi":"あめ / あま", "vocab":"天気（てんき） — tempo (clima)"},
{"kanji":"空", "meaning":"céu / vazio", "onyomi":"くう", "kunyomi":"そら / あ(ける)", "vocab":"空港（くうこう） — aeroporto"},
{"kanji":"晴", "meaning":"ensolarado / claro", "onyomi":"せい", "kunyomi":"は(れ)", "vocab":"晴れ（はれ） — céu claro / sol"},
{"kanji":"雨", "meaning":"chuva", "onyomi":"う", "kunyomi":"あめ", "vocab":"雨（あめ） — chuva"},
{"kanji":"雪", "meaning":"neve", "onyomi":"せつ", "kunyomi":"ゆき", "vocab":"雪（ゆき） — neve"},
{"kanji":"雲", "meaning":"nuvem", "onyomi":"うん", "kunyomi":"くも", "vocab":"曇り（くもり） — nublado"},
{"kanji":"風", "meaning":"vento", "onyomi":"ふう", "kunyomi":"かぜ", "vocab":"風（かぜ） — vento"},
{"kanji":"電", "meaning":"eletricidade", "onyomi":"でん", "kunyomi":"—", "vocab":"電気（でんき） — eletricidade / luz"},
{"kanji":"外", "meaning":"fora / exterior", "onyomi":"がい", "kunyomi":"そと / はず(れる)", "vocab":"外国（がいこく） — país estrangeiro"},
{"kanji":"内", "meaning":"dentro / interior", "onyomi":"ない", "kunyomi":"うち", "vocab":"内（うち） — casa / dentro"},
{"kanji":"上", "meaning":"acima / em cima", "onyomi":"じょう", "kunyomi":"うえ / あ(げる)", "vocab":"上（うえ） — cima"},
{"kanji":"下", "meaning":"abaixo / embaixo", "onyomi":"か / げ", "kunyomi":"した / くだ(る)", "vocab":"下（した） — baixo / debaixo"},
{"kanji":"右", "meaning":"direita", "onyomi":"ゆう", "kunyomi":"みぎ", "vocab":"右（みぎ） — direita"},
{"kanji":"左", "meaning":"esquerda", "onyomi":"さ", "kunyomi":"ひだり", "vocab":"左（ひだり） — esquerda"},
{"kanji":"中", "meaning":"meio / dentro", "onyomi":"ちゅう / じゅう", "kunyomi":"なか", "vocab":"中学校（ちゅうがっこう） — colégio / escola média"},
{"kanji":"北", "meaning":"norte", "onyomi":"ほく", "kunyomi":"きた", "vocab":"北海道（ほっかいどう） — Hokkaido (região)"},
{"kanji":"西", "meaning":"oeste", "onyomi":"せい / さい", "kunyomi":"にし", "vocab":"西（にし） — oeste"},
{"kanji":"東", "meaning":"leste / leste-oriente", "onyomi":"とう", "kunyomi":"ひがし", "vocab":"東京（とうきょう） — Tóquio"},
{"kanji":"南", "meaning":"sul", "onyomi":"なん", "kunyomi":"みなみ", "vocab":"南（みなみ） — sul"},

# Verbos comuns
{"kanji":"見", "meaning":"ver", "onyomi":"けん", "kunyomi":"みる", "vocab":"見る（みる） — ver / assistir"},
{"kanji":"聞", "meaning":"ouvir / escutar", "onyomi":"もん / ぶん", "kunyomi":"きく", "vocab":"聞く（きく） — ouvir / escutar"},
{"kanji":"書", "meaning":"escrever", "onyomi":"しょ", "kunyomi":"かく", "vocab":"書く（かく） — escrever"},
{"kanji":"言", "meaning":"dizer / falar", "onyomi":"げん", "kunyomi":"いう", "vocab":"言う（いう） — dizer"},
{"kanji":"話", "meaning":"falar / conversar", "onyomi":"わ", "kunyomi":"はなす", "vocab":"話す（はなす） — falar"},
{"kanji":"読", "meaning":"ler", "onyomi":"どく", "kunyomi":"よむ", "vocab":"読む（よむ） — ler"},
{"kanji":"行", "meaning":"ir", "onyomi":"こう", "kunyomi":"いく / おこなう", "vocab":"行く（いく） — ir"},
{"kanji":"買", "meaning":"comprar", "onyomi":"ばい", "kunyomi":"かう", "vocab":"買う（かう） — comprar"},
{"kanji":"出", "meaning":"sair / sair-algo", "onyomi":"しゅつ", "kunyomi":"でる / だす", "vocab":"出る（でる） — sair"},
{"kanji":"入", "meaning":"entrar / inserir", "onyomi":"にゅう", "kunyomi":"はいる / いれる", "vocab":"入る（はいる） — entrar"},
{"kanji":"食", "meaning":"comer", "onyomi":"しょく", "kunyomi":"たべる", "vocab":"食べる（たべる） — comer"},
{"kanji":"飲", "meaning":"beber", "onyomi":"いん", "kunyomi":"のむ", "vocab":"飲む（のむ） — beber"},
{"kanji":"休", "meaning":"descansar / descansar-algo", "onyomi":"きゅう", "kunyomi":"やすむ / やすみ", "vocab":"休む（やすむ） — descansar"},
{"kanji":"会", "meaning":"encontrar / reunião", "onyomi":"かい", "kunyomi":"あう", "vocab":"会う（あう） — encontrar"},

# Adjetivos / adj-kanjis comuns
{"kanji":"多", "meaning":"muito / muitos", "onyomi":"た", "kunyomi":"おおい", "vocab":"多い（おおい） — muitos / numeroso"},
{"kanji":"少", "meaning":"pouco / poucos", "onyomi":"しょう", "kunyomi":"すこし / すくない", "vocab":"少し（すこし） — um pouco"},
{"kanji":"古", "meaning":"velho / antigo", "onyomi":"こ", "kunyomi":"ふるい", "vocab":"古い（ふるい） — velho"},
{"kanji":"新", "meaning":"novo", "onyomi":"しん", "kunyomi":"あたらしい", "vocab":"新しい（あたらしい） — novo"},
{"kanji":"大", "meaning":"grande", "onyomi":"だい / たい", "kunyomi":"おおきい", "vocab":"大きい（おおきい） — grande"},
{"kanji":"小", "meaning":"pequeno", "onyomi":"しょう", "kunyomi":"ちいさい", "vocab":"小さい（ちいさい） — pequeno"},
{"kanji":"長", "meaning":"longo / comprido", "onyomi":"ちょう", "kunyomi":"ながい", "vocab":"長い（ながい） — longo"},
{"kanji":"短", "meaning":"curto", "onyomi":"たん", "kunyomi":"みじかい", "vocab":"短い（みじかい） — curto"},
{"kanji":"遠", "meaning":"longe / distante", "onyomi":"えん", "kunyomi":"とおい", "vocab":"遠い（とおい） — longe"},
{"kanji":"近", "meaning":"perto / próximo", "onyomi":"きん / こん", "kunyomi":"ちかい", "vocab":"近い（ちかい） — perto"},
{"kanji":"白", "meaning":"branco / claro", "onyomi":"はく", "kunyomi":"しろ / しろい", "vocab":"白い（しろい） — branco"},
{"kanji":"黒", "meaning":"preto / escuro", "onyomi":"こく", "kunyomi":"くろ / くろい", "vocab":"黒い（くろい） — preto"},
{"kanji":"高", "meaning":"alto / caro", "onyomi":"こう", "kunyomi":"たかい", "vocab":"高い（たかい） — caro / alto"},
{"kanji":"安", "meaning":"barato / seguro / tranquilo", "onyomi":"あん", "kunyomi":"やすい", "vocab":"安い（やすい） — barato / econômico"},

]

# ============================
# PARTE 3 — Criar deck e exportar
# ============================


# Criar ID único para o baralho
deck_id = random.randrange(1 << 30, 1 << 31)

# Criar o baralho
my_deck = genanki.Deck(
    deck_id,
    "JLPT N5 — Kanji Completo"
)

# Modelo da carta (Front/Back)
kanji_model = genanki.Model(
    random.randrange(1 << 30, 1 << 31),
    'Kanji Model',
    fields=[
        {'name': 'Kanji'},
        {'name': 'Meaning'},
        {'name': 'Onyomi'},
        {'name': 'Kunyomi'},
        {'name': 'Vocab'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<div style="font-size: 80px; text-align: center;">{{Kanji}}</div>',
            'afmt': '''
            <div style="font-size: 80px; text-align: center;">{{Kanji}}</div>
            <hr>
            <p><b>Significado:</b> {{Meaning}}</p>
            <p><b>Onyomi:</b> {{Onyomi}}</p>
            <p><b>Kunyomi:</b> {{Kunyomi}}</p>
            <p><b>Vocabulário:</b><br>{{Vocab}}</p>
            '''
        },
    ]
)




# Adicionar cada kanji como nota
for item in kanji_list:
    note = genanki.Note(
        model=kanji_model,
        fields=[
            item["kanji"],
            item["meaning"],
            item["onyomi"],
            item["kunyomi"],
            item["vocab"]
        ]
    )
    my_deck.add_note(note)

# Gerar o arquivo .apkg
output_file = "JLPT_N5_Kanji.apkg"
genanki.Package(my_deck).write_to_file(output_file)

print(f"Arquivo '{output_file}' gerado com sucesso!")
