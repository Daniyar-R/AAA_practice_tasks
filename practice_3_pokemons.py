class BasePokemon:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __str__(self):
        return f"{self.name}/{self.category}"


class EmojiMixin:
    name: str
    poketype: str

    def __str__(self):
        emoji_dict = {"grass": "🌿", "fire": "🔥", "water": "🌊", "electric": "⚡"}
        emoji_poketype = emoji_dict[self.poketype]
        return f"{self.name}/{emoji_poketype}"


class Pokemon(EmojiMixin, BasePokemon):
    def __init__(self, name, category, weaknesses, poketype):
        self.weaknesses = weaknesses
        self.poketype = poketype
        super().__init__(name, category)


base_charmander = BasePokemon(name="Charmander", category="Lizard")
print(base_charmander)

charmander = Pokemon(
    name="Charmander",
    category="Lizard",
    weaknesses=("water", "ground", "rock"),
    poketype="fire",
)


print(charmander)
